# BFS / DFS — 그래프 탐색 ★ 최빈출

> **한 줄 요약**: 코테에서 가장 많이 나옵니다. **여기를 못 넘으면 합격이 안 됩니다.**

이 문서만큼은 완전히 소화하고 넘어가세요.
BFS/DFS 문제를 30문제쯤 풀면 "아 이거 BFS네"가 문제 읽자마자 보입니다.

## 1. 언제 쓰나 — 문제 속 신호

- "미로에서 **최단 거리**" → **BFS** (가중치 없는 최단거리 = BFS)
- "섬의 **개수**", "덩어리 세기", "연결 요소" → BFS 또는 DFS (아무거나)
- "모든 경로를 다 확인" → DFS
- "n번 퍼진 뒤의 상태" (바이러스, 토마토 익히기) → BFS (레벨 단위)

**가중치 없는 최단거리는 무조건 BFS**입니다. DFS로 최단거리를 구하려 하면 안 됩니다.

## 2. 그래프를 코드로 표현하기

### 인접 리스트 (대부분 이걸 씁니다)
```python
from collections import defaultdict
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)      # ★ 무방향 그래프면 양쪽 다!
```

### 격자(2차원 배열)도 그래프입니다
```python
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
```
"미로", "지도", "섬" 문제는 전부 격자 그래프입니다. 간선이 상하좌우로 암시된 것뿐이에요.

## 3. BFS 템플릿 ★ 외우세요

```python
from collections import deque

def bfs(start):
    q = deque([start])
    visited = {start}                      # ★ 넣을 때 방문 표시!
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if nxt not in visited:
                visited.add(nxt)           # ★ 여기서 표시 (꺼낼 때 X)
                q.append(nxt)
```

> **가장 흔한 버그**: 큐에서 **꺼낼 때** 방문 표시를 하면, 같은 노드가 큐에 여러 번
> 들어가서 느려지거나 틀립니다. **큐에 넣는 순간 표시**하세요.

### 격자 BFS + 최단거리

```python
from collections import deque

def bfs(board, n, m, sx, sy):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    dist = [[-1] * m for _ in range(n)]
    dist[sx][sy] = 0
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and board[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist
```

`dist` 배열이 **방문 체크와 거리 저장을 동시에** 합니다 (-1 = 미방문). 자주 쓰는 트릭이에요.

### 다중 시작점 BFS

"모든 토마토에서 동시에 익어간다" → 시작점을 **전부 큐에 미리 넣고** 시작합니다.

```python
q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))
            dist[i][j] = 0
# 이후 동일한 BFS
```

## 4. DFS 템플릿

### 재귀 버전 (짧지만 깊이 제한 주의)

```python
import sys
sys.setrecursionlimit(10 ** 6)      # ★ 필수

visited = set()
def dfs(cur):
    visited.add(cur)
    for nxt in graph[cur]:
        if nxt not in visited:
            dfs(nxt)
```

### 스택 버전 (안전. 깊이 걱정 없음)

```python
def dfs(start):
    stack = [start]
    visited = set()
    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)
        for nxt in graph[cur]:
            if nxt not in visited:
                stack.append(nxt)
```

**노드가 10만 개 넘으면 재귀 대신 스택 버전을 쓰세요.** Python 재귀는 잘 터집니다.

## 5. 대표 응용: 연결 요소 개수 (섬 세기)

```python
count = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            bfs(i, j)          # 한 덩어리를 전부 방문 처리
            count += 1         # 덩어리 하나 발견
```

"섬의 개수", "단지 번호 붙이기", "그림 개수" 전부 이 골격입니다.

> 실행 가능한 전체 코드: [`algo/bfs_dfs.py`](../../algo/bfs_dfs.py)
> (`python3 -m algo.bfs_dfs` 로 바로 돌려볼 수 있습니다)

## 6. BFS vs DFS 정리

| | BFS | DFS |
|---|---|---|
| 자료구조 | 큐 (deque) | 스택 / 재귀 |
| 탐색 순서 | 가까운 것부터 | 깊이 먼저 |
| **최단거리** | ✅ 구할 수 있음 | ❌ 안 됨 |
| 메모리 | 넓으면 많이 씀 | 깊으면 많이 씀 |
| 경로 전체 탐색 | 불편 | ✅ 편함 |

## 7. 디버깅 체크리스트

문제가 안 풀릴 때 여기부터 보세요.

- [ ] 무방향 그래프인데 한 방향만 넣지 않았나
- [ ] 큐에 **넣을 때** 방문 표시했나 (꺼낼 때 X)
- [ ] 경계 검사 `0 <= nx < n and 0 <= ny < m` 했나
- [ ] 시작점의 거리를 0으로 초기화했나 (1이 아니라)
- [ ] 노드 번호가 1부터인데 배열을 `n`이 아니라 `n+1`로 잡았나
- [ ] 재귀 DFS면 `setrecursionlimit` 했나

## 8. 추천 문제 — 이 순서대로 푸세요 ★

| 문제 | 난이도 | 포인트 |
|---|---|---|
| [BOJ 1260 DFS와 BFS](https://www.acmicpc.net/problem/1260) | 실버2 | 둘 다 기본 ★ 필수 |
| [BOJ 2606 바이러스](https://www.acmicpc.net/problem/2606) | 실버3 | 연결 요소 |
| [BOJ 2667 단지번호붙이기](https://www.acmicpc.net/problem/2667) | 실버1 | 격자 덩어리 세기 ★ |
| [BOJ 2178 미로 탐색](https://www.acmicpc.net/problem/2178) | 실버1 | 격자 최단거리 ★★ |
| [BOJ 7576 토마토](https://www.acmicpc.net/problem/7576) | 골드5 | 다중 시작점 BFS ★★ |
| [BOJ 1012 유기농 배추](https://www.acmicpc.net/problem/1012) | 실버2 | 덩어리 세기 |
| [BOJ 2606 / 7562 나이트의 이동](https://www.acmicpc.net/problem/7562) | 실버1 | 이동 방향 8개 |
| [BOJ 1697 숨바꼭질](https://www.acmicpc.net/problem/1697) | 실버1 | 격자가 아닌 BFS ★ |
| [BOJ 2206 벽 부수고 이동하기](https://www.acmicpc.net/problem/2206) | 골드3 | 상태를 하나 더 (3차원 방문) |

마지막 두 문제(1697, 2206)까지 풀면 BFS는 확실히 넘긴 겁니다.
