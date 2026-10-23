"""[프로그래머스] 전력망을 둘로 나누기 (86971) — Lv.2

링크: https://school.programmers.co.kr/learn/courses/30/lessons/86971
유형: 완전탐색 x DFS (그래프)
풀이: 2026-10-24 (시험 당일 아침, 학습자 작성)

--- 왜 이 알고리즘인가 (4단 판단) ---
1. "최소/최단"?        → '차이의 최솟값'이지만 거리가 아니다 → BFS 아님
2. 제한 N 작은가?       → n <= 100, 전선 = n-1개.
                          끊을 전선이 최대 99가지 x DFS(100) ~= 1만번 → ★ 다 해봐도 된다
3. 경로를 만들어야?     → 아님
4. N 크고 경우의 수?    → 아님
   ∴ 완전탐색 x DFS

--- 설계 ---
1. 전선을 하나씩 끊어본다 (skip)
2. skip 한 전선만 빼고 인접행렬을 '매번 새로' 만든다
3. 1번 노드에서 DFS → visited 의 True 개수 = 한쪽 덩어리 크기
4. 다른 쪽은 자동으로 n - size  →  차이 = abs(size - (n - size))
5. 그 최솟값

--- 핵심 ---
- 「네트워크」(43162)는 덩어리 '개수'를 셌다. 이 문제는 덩어리 '크기'를 센다
- sum(visited) : True 가 1로 계산되므로 개수가 바로 나온다
- graph/visited 를 for문 '안'에서 만들어야 한다 (도구 #27)
- 노드가 1번부터이므로 (n+1) x (n+1) 로 만들고 0행/0열은 버린다
  → n x n 으로도 되지만 모든 노드 번호에 -1 을 해야 해서 실수가 난다

--- 검증 (2026-10-24) ---
공식 예제 3개 (3 / 0 / 1) 통과
무작위 트리 5,000건 교차검증(BFS 독립 구현) 불일치 0건
n=100 (제한 최대) 31ms
"""
import sys
sys.setrecursionlimit(100000)


def solution(n, wires):
    answer = n                                        # 차이는 n보다 클 수 없다

    for skip in range(len(wires)):                    # 전선을 하나씩 끊어본다
        graph = [[0] * (n + 1) for i in range(n + 1)] # 매번 새로. 0행/0열은 안 쓴다
        for i, (x, y) in enumerate(wires):
            if i == skip:
                continue                              # skip 번째 전선만 제외
            graph[x][y] = 1
            graph[y][x] = 1                           # 양방향

        visited = [False] * (n + 1)

        def dfs(x):
            visited[x] = True                         # 들어오자마자 도장
            for y in range(n + 1):
                if graph[x][y] == 1 and not visited[y]:
                    dfs(y)

        dfs(1)                                        # 1번 노드에서 출발
        size = sum(visited)                           # True 개수 = 한쪽 덩어리 크기
        answer = min(answer, abs(size - (n - size)))

    return answer


if __name__ == "__main__":
    cases = [
        ((9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]), 3),
        ((4, [[1, 2], [2, 3], [3, 4]]), 0),
        ((7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]), 1),
        ((2, [[1, 2]]), 0),
    ]
    for args, expected in cases:
        got = solution(*args)
        print(f"n={args[0]:3d} -> {got}  (기대 {expected})  {'OK' if got == expected else 'FAIL'}")
