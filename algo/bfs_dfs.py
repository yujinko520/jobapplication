"""BFS / DFS 템플릿 — 코테 최빈출. 이 파일은 통째로 외울 가치가 있습니다."""

from collections import deque

# 격자 문제의 표준 방향 배열 (상, 하, 좌, 우)
DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]

# 8방향이 필요하면 이것을 씁니다
DX8 = [-1, -1, -1, 0, 0, 1, 1, 1]
DY8 = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs_order(graph: dict[int, list[int]], start: int) -> list[int]:
    """인접 리스트 그래프에서 BFS 방문 순서.

    >>> g = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]}
    >>> bfs_order(g, 1)
    [1, 2, 3, 4]
    """
    q = deque([start])
    visited = {start}                      # ★ 큐에 넣는 순간 방문 표시
    order = []
    while q:
        cur = q.popleft()
        order.append(cur)
        for nxt in graph.get(cur, []):
            if nxt not in visited:
                visited.add(nxt)           # ★ 꺼낼 때가 아니라 넣을 때!
                q.append(nxt)
    return order


def dfs_order_recursive(graph: dict[int, list[int]], start: int) -> list[int]:
    """재귀 DFS. 노드가 많으면 sys.setrecursionlimit 필요.

    >>> g = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]}
    >>> dfs_order_recursive(g, 1)
    [1, 2, 4, 3]
    """
    visited: set[int] = set()
    order: list[int] = []

    def dfs(cur: int) -> None:
        visited.add(cur)
        order.append(cur)
        for nxt in graph.get(cur, []):
            if nxt not in visited:
                dfs(nxt)

    dfs(start)
    return order


def dfs_order_stack(graph: dict[int, list[int]], start: int) -> list[int]:
    """스택 DFS. 재귀 깊이 걱정이 없어서 큰 그래프에 안전합니다.

    (재귀 버전과 같은 순서를 내려면 이웃을 역순으로 넣습니다)

    >>> g = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]}
    >>> dfs_order_stack(g, 1)
    [1, 2, 4, 3]
    """
    stack = [start]
    visited: set[int] = set()
    order: list[int] = []
    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)
        order.append(cur)
        for nxt in reversed(graph.get(cur, [])):
            if nxt not in visited:
                stack.append(nxt)
    return order


def grid_shortest_path(grid: list[list[int]], start=(0, 0), goal=None) -> int:
    """격자 최단거리 (프로그래머스 '게임 맵 최단거리' 형). 1=길, 0=벽. 칸 수를 셉니다.

    도달 불가면 -1.

    >>> maze = [[1, 0, 1, 1, 1, 1],
    ...         [1, 0, 1, 0, 1, 0],
    ...         [1, 0, 1, 0, 1, 1],
    ...         [1, 1, 1, 0, 1, 1]]
    >>> grid_shortest_path(maze)
    15
    """
    n, m = len(grid), len(grid[0])
    if goal is None:
        goal = (n - 1, m - 1)

    dist = [[-1] * m for _ in range(n)]
    sx, sy = start
    dist[sx][sy] = 1                       # 시작 칸도 1칸으로 셈 (문제 조건에 맞춰 조정)
    q = deque([(sx, sy)])

    while q:
        x, y = q.popleft()
        if (x, y) == goal:
            return dist[x][y]
        for d in range(4):
            nx, ny = x + DX[d], y + DY[d]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and grid[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return -1


def count_islands(grid: list[list[int]]) -> int:
    """연결 요소(덩어리) 개수 — 섬 세기 / 단지번호붙이기 (프로그래머스 '무인도 여행' / '카카오프렌즈 컬러링북' 형).

    >>> g = [[1, 1, 0, 0],
    ...      [1, 0, 0, 1],
    ...      [0, 0, 1, 1],
    ...      [0, 0, 1, 0]]
    >>> count_islands(g)
    2
    """
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] != 1 or visited[i][j]:
                continue
            # 덩어리 하나를 통째로 방문 처리
            visited[i][j] = True
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x + DX[d], y + DY[d]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            count += 1
    return count


def multi_source_bfs(grid: list[list[int]]) -> int:
    """다중 시작점 BFS — 토마토 익히기 (여러 지점에서 동시에 퍼지는 확산 문제 형).

    1=익은 토마토(시작점), 0=안 익음, -1=빈 칸.
    전부 익는 데 걸리는 일수를 반환. 불가능하면 -1.

    >>> multi_source_bfs([[0, 0, 0, 0, 0, 0],
    ...                   [0, 0, 0, 0, 0, 0],
    ...                   [0, 0, 0, 0, 0, 0],
    ...                   [0, 0, 0, 0, 0, 1]])
    8
    >>> multi_source_bfs([[0, -1], [-1, 1]])
    -1
    """
    n, m = len(grid), len(grid[0])
    dist = [[-1] * m for _ in range(n)]
    q: deque[tuple[int, int]] = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))           # ★ 시작점을 전부 미리 큐에 넣는다

    days = 0
    while q:
        x, y = q.popleft()
        days = max(days, dist[x][y])
        for d in range(4):
            nx, ny = x + DX[d], y + DY[d]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and grid[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 and dist[i][j] == -1:
                return -1                  # 못 익는 토마토가 남음
    return days


def bfs_on_numbers(start: int, target: int, limit: int = 100_000) -> int:
    """격자가 아닌 BFS — 숨바꼭질 (상태 전이 BFS — 프로그래머스 '단어 변환'과 같은 사고).

    x에서 x-1, x+1, 2x 로 이동할 때 target까지 최소 횟수.

    >>> bfs_on_numbers(5, 17)
    4
    >>> bfs_on_numbers(5, 5)
    0
    """
    if start >= target:
        return start - target              # 뒤로만 가야 하면 한 칸씩

    dist = [-1] * (limit + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        x = q.popleft()
        if x == target:
            return dist[x]
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= limit and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
    return -1


if __name__ == "__main__":
    g = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]}
    print("BFS 순서:", bfs_order(g, 1))
    print("DFS 순서(재귀):", dfs_order_recursive(g, 1))
    print("DFS 순서(스택):", dfs_order_stack(g, 1))

    maze = [[1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1]]
    print("미로 최단거리:", grid_shortest_path(maze))
    print("섬 개수:", count_islands([[1, 1, 0], [0, 0, 0], [0, 1, 1]]))
    print("숨바꼭질 5 -> 17:", bfs_on_numbers(5, 17))
