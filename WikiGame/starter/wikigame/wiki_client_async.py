from __future__ import annotations

import asyncio
import ssl
from typing import Any, Optional

import aiohttp

from .utils import normalize_title

API_URL_RU = "https://ru.wikipedia.org/w/api.php"


class WikiClientAsync:
    """
    Асинхронный клиент MediaWiki API (русская Википедия).

    Демонстрирует:
    - asyncio + aiohttp
    - ограничение конкурентности
    - мягкий rate limit (опционально)
    - кеширование в памяти
    """

    def __init__(
        self,
        *,
        concurrency: int = 10,
        rps_delay: float = 0.0,
        user_agent: str = "WikiGameCourseBot/1.0 (edu)",
        verify_ssl: bool = True,
        ca_bundle: str | None = None,
    ):
        self.api_url = API_URL_RU
        self.concurrency = max(1, int(concurrency))
        self.rps_delay = max(0.0, float(rps_delay))
        self.headers = {"User-Agent": user_agent}

        self._sem = asyncio.Semaphore(self.concurrency)
        self._session: Optional[aiohttp.ClientSession] = None
        self.cache: dict[str, list[str]] = {}
        self._ssl: ssl.SSLContext | None = _build_ssl_context(verify_ssl=verify_ssl, ca_bundle=ca_bundle)

    async def __aenter__(self) -> "WikiClientAsync":
        connector = aiohttp.TCPConnector(limit=self.concurrency, limit_per_host=self.concurrency, ssl=self._ssl)
        self._session = aiohttp.ClientSession(headers=self.headers, connector=connector)
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if self._session is not None:
            await self._session.close()
            self._session = None

    async def _fetch_json(self, params: dict[str, Any]) -> dict[str, Any]:
        if self._session is None:
            raise RuntimeError("WikiClientAsync должен использоваться через 'async with'.")

        async with self._sem:
            async with self._session.get(
                self.api_url,
                params=params,
                timeout=aiohttp.ClientTimeout(total=20),
            ) as resp:
                resp.raise_for_status()
                data: dict[str, Any] = await resp.json()

        if self.rps_delay > 0:
            await asyncio.sleep(self.rps_delay)
        return data

    async def get_links(self, title: str, *, limit: int = 500) -> list[str]:
        title = normalize_title(title)
        if title in self.cache:
            return self.cache[title]

        params: dict[str, Any] = {
            "action": "query",
            "format": "json",
            "redirects": 1,
            "titles": title,
            "prop": "links",
            "plnamespace": 0,
            "pllimit": min(limit, 500),
        }

        links: list[str] = []
        while True:
            data = await self._fetch_json(params)

            pages = data.get("query", {}).get("pages", {})
            for _pageid, page in pages.items():
                for link in page.get("links", []):
                    link_title = link.get("title")
                    if isinstance(link_title, str):
                        links.append(link_title)

            cont = data.get("continue")
            if not cont:
                break
            params.update(cont)

        self.cache[title] = links
        return links


def _build_ssl_context(*, verify_ssl: bool, ca_bundle: str | None) -> ssl.SSLContext | None:
    if ca_bundle is not None and not verify_ssl:
        raise ValueError("Нельзя одновременно задать ca_bundle и verify_ssl=False.")

    if ca_bundle is not None:
        return ssl.create_default_context(cafile=ca_bundle)

    if not verify_ssl:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx

    return None
