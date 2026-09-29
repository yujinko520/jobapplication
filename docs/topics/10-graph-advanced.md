# 최단경로 / 유니온파인드 / 위상정렬

> **한 줄 요약**: BFS로 안 되는 그래프 문제들. **시간이 없으면 다익스트라만.**

시험까지 시간이 빠듯하다면 **다익스트라 하나만** 확실히 하고 나머지는 "이런 게 있다" 수준으로 넘기세요.

## 1. 최단경로 알고리즘 고르기

| 상황 | 알고리즘 | 복잡도 |
|---|---|---|
| 간선 가중치가 **모두 1** | **BFS** | O(V+E) |
| 가중치가 양수, **한 점**에서 출발 | **다익스트라** | O(E log V) |
| 가중치에 **음수** 포함 | 벨만-포드 | O(VE) |
| **모든 쌍** 사이 거리 (V ≤ 500) | 플로이드-워셜 | O(V³) |

**가중치가 없거나 전부 1이면 다익스트라 쓰지 말고 BFS 쓰세요.** 더 빠르고 간단합니다.

## 2. 다익스트라 ★ 우선순위 큐 버전

```python
from heapq import heappush, heappop

def dijkstra(graph, start, n):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]                      # (거리, 노드)

    while pq:
        d, cur = heappop(pq)
        if d > dist[cur]:                  # ★ 이미 더 짧은 경로를 찾았으면 스킵
            continue
        for nxt, w in graph[cur]:
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heappush(pq, (nd, nxt))
    return dist
```

**핵심 포인트**
- 큐에 `(거리, 노드)` 순서로 넣어야 거리 기준 정렬됩니다
- `if d > dist[cur]: continue` 이 줄이 없으면 느려집니다 (필수)
- `visited` 배열 대신 이 조건으로 처리하는 게 관례입니다

그래프 입력:
```python
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    # 무방향이면 graph[b].append((a, w)) 도
```

→ 실행 코드: [`algo/graph.py`](../../algo/graph.py)

## 3. 플로이드-워셜 (모든 쌍, 3중 루프)

```python
INF = float('inf')
# dist[i][j] 초기화: 자기 자신 0, 간선 있으면 가중치, 없으면 INF

for k in range(1, n + 1):          # ★ 경유지 k가 가장 바깥
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

**k 루프가 가장 바깥**이어야 합니다. 순서 바꾸면 틀려요. V ≤ 500 정도까지만 가능.

## 4. 유니온 파인드 (서로소 집합)

"둘이 같은 그룹인가?", "사이클이 생기는가?"를 거의 O(1)에 판정합니다.

```python
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])    # 경로 압축
    return parent[x]

def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a == b:
        return False          # 이미 같은 집합 (= 사이클)
    parent[b] = a
    return True

parent = list(range(n + 1))    # 초기화: 각자 자기 자신이 부모
```

용도: 네트워크 연결 확인, 사이클 판정, 크루스칼 MST.

## 5. 위상 정렬 (순서가 있는 작업)

"A를 끝내야 B를 할 수 있다" 류의 순서 정하기.

```python
from collections import deque

indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
# a → b 간선마다: graph[a].append(b); indegree[b] += 1

q = deque([i for i in range(1, n + 1) if indegree[i] == 0])
order = []
while q:
    cur = q.popleft()
    order.append(cur)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

# len(order) < n 이면 사이클이 있어서 순서를 정할 수 없음
```

## 6. 우선순위 (시간이 부족할 때)

1. **다익스트라** — 반드시 (출제 빈도 높음)
2. 유니온 파인드 — 여유 되면 (코드가 짧아서 가성비 좋음)
3. 위상 정렬 — 여유 되면
4. 플로이드-워셜 — 코드가 4줄이라 부담 없음, 한 번만 보기
5. 벨만-포드 / MST — 시간 없으면 버려도 됨

## 추천 문제 (프로그래머스)

| 문제 | 레벨 | 포인트 |
|---|---|---|
| [배달](https://school.programmers.co.kr/learn/courses/30/lessons/12978) | Lv.2 | 다익스트라 입문 ★★ |
| [가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189) | Lv.3 | BFS로 충분 (가중치 없음) ★ |
| [순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191) | Lv.3 | 플로이드-워셜 / 도달 가능성 ★ |
| [합승 택시 요금](https://school.programmers.co.kr/learn/courses/30/lessons/72413) | Lv.3 | 다익스트라 여러 번 (도전) |
| [섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861) | Lv.3 | 크루스칼 + 유니온파인드 |

> **배달** 하나만 확실히 하세요. 다익스트라 템플릿을 그대로 쓰는 문제입니다.
> **가장 먼 노드**는 가중치가 없으니 **다익스트라 말고 BFS**로 푸는 게 맞습니다 —
> 이 판단을 할 수 있는지가 이 문서의 진짜 목적입니다.
