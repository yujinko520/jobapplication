"""[프로그래머스] 게임 맵 최단거리 (Lv.2) — 격자 BFS ★★ 이 유형의 원형

링크: https://school.programmers.co.kr/learn/courses/30/lessons/1844
유형: BFS (가중치 없는 최단거리)
제한: maps 최대 100 x 100  ->  칸 1만 개. BFS O(NM)으로 충분

--- 설계 ---
1. (0, 0)에서 출발해 (n-1, m-1)까지 BFS
2. dist 배열이 '방문 체크'와 '거리 저장'을 동시에 담당 (0 = 미방문)
3. 시작 칸을 1로 세므로 dist[0][0] = 1
4. 도착 못 하면 -1 반환

--- 왜 DFS가 아니라 BFS인가 ---
가중치 없는 최단거리는 BFS만 정답을 보장합니다.
BFS는 가까운 칸부터 훑으므로, 도착 칸에 처음 닿는 순간이 곧 최단입니다.
DFS는 먼저 도착한 경로가 최단이라는 보장이 없습니다.

--- 자주 하는 실수 ---
- 큐에서 꺼낼 때 방문 표시 -> 같은 칸이 큐에 여러 번 들어감. **넣을 때 표시!**
- 도달 불가능한 경우 -1 반환을 빼먹음
- 경계 검사 누락 -> 런타임 에러
"""

from collections import deque

DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]


def solution(maps: list[list[int]]) -> int:
    n, m = len(maps), len(maps[0])
    dist = [[0] * m for _ in range(n)]          # 0 = 아직 방문 안 함
    dist[0][0] = 1                              # 시작 칸도 1칸으로 셈
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()
        if (x, y) == (n - 1, m - 1):
            return dist[x][y]                   # BFS라 처음 닿는 순간이 최단

        for d in range(4):
            nx, ny = x + DX[d], y + DY[d]
            if not (0 <= nx < n and 0 <= ny < m):        # ★ 경계 검사
                continue
            if dist[nx][ny] != 0 or maps[nx][ny] == 0:   # 이미 방문 or 벽
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))                  # ★ 넣기 전에 dist를 채웠다 = 방문 표시

    return -1                                   # 큐가 비었는데 도착 못 함


if __name__ == "__main__":
    ex1 = [[1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1],
           [1, 0, 1, 1, 1],
           [1, 1, 1, 0, 1],
           [0, 0, 0, 0, 1]]
    ex2 = [[1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1],
           [1, 0, 1, 1, 1],
           [1, 1, 1, 0, 0],
           [0, 0, 0, 0, 1]]
    print("예제1:", solution(ex1), "/ 기대: 11")
    print("예제2:", solution(ex2), "/ 기대: -1")
