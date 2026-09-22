from typing import List
import abc


class SearchResult:

    # Результат поиска пути

    def __init__(self, path: List[str], visited_pages: int):
        self.path = path
        self.visited_pages = visited_pages


class LinkProvider(abc.ABC):

    # Базовый класс для получения ссылок из статей

    @abc.abstractmethod
    def get_links(self, title: str) -> List[str]:
        raise NotImplementedError()


class AsyncLinkProvider(abc.ABC):

    # Асинхронный базовый класс для получения ссылок из статей

    @abc.abstractmethod
    async def get_links(self, title: str) -> List[str]:
        raise NotImplementedError()