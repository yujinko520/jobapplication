"""[BOJ 2178] 미로 탐색 — 격자 BFS 최단거리 ★ 이 문제가 코테 BFS의 원형입니다

링크: https://www.acmicpc.net/problem/2178
유형: BFS (가중치 없는 최단거리)
제한: N, M <= 100  →  칸 1만 개. BFS O(NM)으로 충분

--- 설계 ---
1. 미로를 문자열 리스트로 읽는다 (각 글자가 0 또는 1)
2. (0,0)에서 BFS. dist 배열로 방문 체크 + 거리 저장을 동시에
3. dist[N-1][M-1] 출력 (시작 칸도 1로 세므로 dist[0][0] = 1)

--- 왜 DFS가 아니라 BFS인가 ---
가중치 없는 최단거리는 BFS만 정답을 보장합니다.
DFS는 먼저 도착한 경로가 최단이라는 보장이 없습니다.

--- 자주 하는 실수 ---
- 큐에서 꺼낼 때 방문 표시 → 같은 칸이 큐에 여러 번 들어감. **넣을 때 표시!**
- 시작 칸 거리를 0으로 둠 → 이 문제는 칸 수를 세므로 1
- 경계 검사 누락 → 런타임 에러
"""

import sys
from collections import deque

DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]


def solve(data: str) -> int:
    lines = data.strip().split('\n')
    n, m = map(int, lines[0].split())
    maze = [lines[i + 1].strip() for i in range(n)]

    dist = [[0] * m for _ in range(n)]     # 0 = 미방문
    dist[0][0] = 1
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()
        if (x, y) == (n - 1, m - 1):       # 도착하면 바로 반환 (BFS라 최단 보장)
            return dist[x][y]
        for d in range(4):
            nx, ny = x + DX[d], y + DY[d]
            if not (0 <= nx < n and 0 <= ny < m):    # ★ 경계 검사
                continue
            if dist[nx][ny] != 0 or maze[nx][ny] != '1':
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))             # ★ 넣을 때 이미 dist를 채웠음 = 방문 표시
    return -1


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    EXAMPLE1 = "4 6\n101111\n101010\n101011\n111011"
    EXAMPLE2 = "2 25\n1011101110111011101110111\n1110111011101110111011101"
    print("예제1 결과:", solve(EXAMPLE1), "/ 기대: 15")
    print("예제2 결과:", solve(EXAMPLE2), "/ 기대: 38")
