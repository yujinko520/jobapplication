"""최단경로 / 유니온파인드 / 위상정렬 템플릿.

시간이 부족하면 dijkstra 하나만 확실히 익히세요.
"""

from collections import deque
from heapq import heappop, heappush

INF = float('inf')


def dijkstra(graph: dict[int, list[tuple[int, int]]], start: int, n: int) -> list[float]:
    """다익스트라 (BOJ 1753). graph[u] = [(v, weight), ...], 노드 번호 1..n

    반환: dist[1..n] (도달 불가는 INF). dist[0]은 사용하지 않습니다.

    >>> g = {1: [(2, 2), (3, 3)], 2: [(3, 4), (4, 5)], 3: [(4, 6)], 4: []}
    >>> dijkstra(g, 1, 4)[1:]
    [0, 2, 3, 7]
    """
    dist: list[float] = [INF] * (n + 1)
    dist[start] = 0
    pq: list[tuple[float, int]] = [(0, start)]      # (거리, 노드)

    while pq:
        d, cur = heappop(pq)
        if d > dist[cur]:                           # ★ 이미 더 짧은 경로가 확정됨
            continue
        for nxt, w in graph.get(cur, []):
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heappush(pq, (nd, nxt))
    return dist


def floyd_warshall(n: int, edges: list[tuple[int, int, int]]) -> list[list[float]]:
    """플로이드-워셜 (BOJ 11404): 모든 쌍 최단거리. 노드 1..n, V ≤ 500 권장.

    >>> d = floyd_warshall(3, [(1, 2, 4), (2, 3, 2), (1, 3, 9)])
    >>> d[1][3]
    6
    >>> d[3][1]
    inf
    """
    dist: list[list[float]] = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for a, b, w in edges:
        dist[a][b] = min(dist[a][b], w)             # 중복 간선은 최솟값

    for k in range(1, n + 1):                       # ★ 경유지 k가 가장 바깥!
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


class UnionFind:
    """서로소 집합 (유니온 파인드). 경로 압축 + union by size.

    >>> uf = UnionFind(5)
    >>> uf.union(1, 2)
    True
    >>> uf.union(2, 3)
    True
    >>> uf.same(1, 3)
    True
    >>> uf.same(1, 4)
    False
    >>> uf.union(1, 3)          # 이미 같은 집합 -> 사이클
    False
    """

    def __init__(self, n: int) -> None:
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # 경로 압축
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        """합쳤으면 True, 이미 같은 집합이면 False(= 사이클)."""
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def same(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


def kruskal_mst(n: int, edges: list[tuple[int, int, int]]) -> int:
    """최소 스패닝 트리의 가중치 합 (BOJ 1197). edges = [(a, b, weight), ...]

    >>> kruskal_mst(3, [(1, 2, 1), (2, 3, 2), (1, 3, 3)])
    3
    """
    uf = UnionFind(n)
    total = 0
    for w, a, b in sorted((w, a, b) for a, b, w in edges):   # 가중치 오름차순
        if uf.union(a, b):
            total += w
    return total


def topological_sort(n: int, edges: list[tuple[int, int]]) -> list[int]:
    """위상 정렬 (BOJ 2252). edges = [(a, b), ...] 는 "a가 b보다 앞".

    사이클이 있으면 빈 리스트를 반환합니다.

    >>> topological_sort(3, [(1, 3), (2, 3)])
    [1, 2, 3]
    >>> topological_sort(2, [(1, 2), (2, 1)])
    []
    """
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for a, b in edges:
        graph[a].append(b)
        indegree[b] += 1

    q = deque(i for i in range(1, n + 1) if indegree[i] == 0)
    order: list[int] = []
    while q:
        cur = q.popleft()
        order.append(cur)
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    return order if len(order) == n else []         # 사이클이면 전부 못 담음


def bfs_shortest_unweighted(graph: dict[int, list[int]], start: int, n: int) -> list[int]:
    """가중치가 없거나 전부 1이면 다익스트라 대신 **BFS**를 쓰세요. 더 빠릅니다.

    >>> g = {1: [2, 3], 2: [4], 3: [4], 4: []}
    >>> bfs_shortest_unweighted(g, 1, 4)[1:]
    [0, 1, 1, 2]
    """
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        cur = q.popleft()
        for nxt in graph.get(cur, []):
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return dist


if __name__ == "__main__":
    g = {1: [(2, 2), (3, 3)], 2: [(3, 4), (4, 5)], 3: [(4, 6)], 4: []}
    print("다익스트라 (1번 출발):", dijkstra(g, 1, 4)[1:])

    d = floyd_warshall(3, [(1, 2, 4), (2, 3, 2), (1, 3, 9)])
    print("플로이드 1->3:", d[1][3])

    uf = UnionFind(5)
    uf.union(1, 2); uf.union(3, 4)
    print("유니온파인드 1~2 같은 집합?", uf.same(1, 2), "/ 1~3?", uf.same(1, 3))

    print("크루스칼 MST:", kruskal_mst(3, [(1, 2, 1), (2, 3, 2), (1, 3, 3)]))
    print("위상정렬:", topological_sort(4, [(1, 2), (1, 3), (2, 4), (3, 4)]))
