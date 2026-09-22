from wikigame.bfs import find_path_bfs


class DummyProvider:
    def __init__(self, g: dict[str, list[str]]):
        self.g = g
        self.calls = 0

    def get_links(self, title: str) -> list[str]:
        self.calls += 1
        return self.g.get(title, [])


def test_respects_max_depth():
    g = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": [],
    }
    p = DummyProvider(g)
    res = find_path_bfs("A", "D", p, max_depth=2, max_pages=100)
    assert res is None


def test_respects_max_pages():
    # Граф устроен так, что чтобы дойти до "Z", нужно "развернуть" много вершин.
    g = {"S": [f"X{i}" for i in range(100)], "Z": []}
    for i in range(100):
        g[f"X{i}"] = ["Z"] if i == 99 else []

    p = DummyProvider(g)
    res = find_path_bfs("S", "Z", p, max_depth=2, max_pages=1)
    assert res is None
