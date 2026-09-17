"""DP 템플릿 — 코테 출제 유형 6가지.

DP는 코드보다 **dp[i]의 정의**가 핵심입니다. 각 함수의 docstring 첫 줄을 먼저 읽으세요.
"""

from functools import lru_cache


def climb_stairs(n: int) -> int:
    """[유형1 피보나치형] 1칸 또는 2칸씩 올라 n칸에 도달하는 경우의 수.

    dp[i] = i번째 칸에 도달하는 경우의 수 = dp[i-1] + dp[i-2]

    >>> [climb_stairs(k) for k in range(1, 7)]
    [1, 2, 3, 5, 8, 13]
    """
    if n <= 2:
        return max(n, 1)
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def min_steps_to_one(n: int) -> int:
    """[유형1] 1로 만들기 (BOJ 1463): /3, /2, -1 연산 최소 횟수.

    dp[i] = i를 1로 만드는 최소 연산 횟수

    >>> min_steps_to_one(10)
    3
    >>> min_steps_to_one(2)
    1
    >>> min_steps_to_one(1)
    0
    """
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1                       # 1 빼기
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    return dp[n]


def stairs_max_score(scores: list[int]) -> int:
    """[유형1] 계단 오르기 (BOJ 2579): 연속 3칸은 밟을 수 없음, 마지막 칸 필수.

    dp[i] = i번째 계단을 밟았을 때의 최대 점수

    >>> stairs_max_score([10, 20, 15, 25, 10, 20])
    75
    """
    n = len(scores)
    if n == 1:
        return scores[0]
    if n == 2:
        return scores[0] + scores[1]

    dp = [0] * n
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0], scores[1]) + scores[2]
    for i in range(3, n):
        # 직전 칸을 밟았으면 그 전전은 못 밟음 / 직전을 건너뛰었으면 자유
        dp[i] = max(dp[i - 3] + scores[i - 1], dp[i - 2]) + scores[i]
    return dp[n - 1]


def max_subarray_sum(arr: list[int]) -> int:
    """[유형2] 연속 부분합의 최댓값 (BOJ 1912, 카데인 알고리즘).

    dp[i] = i를 '반드시 포함'하는 연속 부분합의 최댓값

    >>> max_subarray_sum([10, -4, 3, 1, 5, 6, -35, 12, 21, -1])
    33
    >>> max_subarray_sum([-5, -3, -8])
    -3
    """
    best = cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)             # 앞을 버리고 새로 시작 vs 이어붙이기
        best = max(best, cur)
    return best


def lis_length_dp(arr: list[int]) -> int:
    """[유형3] 가장 긴 증가 부분 수열 — O(n²) 버전 (BOJ 11053).

    dp[i] = i로 끝나는 증가 수열의 최대 길이
    (n이 크면 algo.binary_search.lis_length 의 O(n log n) 버전을 쓰세요)

    >>> lis_length_dp([10, 20, 10, 30, 20, 50])
    4
    """
    if not arr:
        return 0
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def knapsack_01(items: list[tuple[int, int]], limit: int) -> int:
    """[유형4] 0/1 배낭 (BOJ 12865). items = [(무게, 가치), ...]

    dp[w] = 무게 w까지 담았을 때의 최대 가치
    ★ 각 물건을 한 번만 쓰려면 무게 루프를 **역순**으로 돕니다.

    >>> knapsack_01([(6, 13), (4, 8), (3, 6), (5, 12)], 7)
    14
    """
    dp = [0] * (limit + 1)
    for weight, value in items:
        for w in range(limit, weight - 1, -1):      # ★ 역순
            dp[w] = max(dp[w], dp[w - weight] + value)
    return dp[limit]


def knapsack_unbounded(items: list[tuple[int, int]], limit: int) -> int:
    """[유형4] 무한 배낭 (물건을 몇 개든 사용). 무게 루프가 **정순**.

    >>> knapsack_unbounded([(3, 6), (5, 12)], 10)
    24
    """
    dp = [0] * (limit + 1)
    for weight, value in items:
        for w in range(weight, limit + 1):          # ★ 정순
            dp[w] = max(dp[w], dp[w - weight] + value)
    return dp[limit]


def coin_change_min(coins: list[int], target: int) -> int:
    """[유형4 응용] target을 만드는 최소 동전 개수. 불가능하면 -1.

    >>> coin_change_min([2, 3, 5], 15)
    3
    >>> coin_change_min([5], 3)
    -1
    """
    INF = float('inf')
    dp = [INF] * (target + 1)
    dp[0] = 0
    for c in coins:
        for v in range(c, target + 1):
            dp[v] = min(dp[v], dp[v - c] + 1)
    return -1 if dp[target] == INF else int(dp[target])


def triangle_max_path(triangle: list[list[int]]) -> int:
    """[유형5] 정수 삼각형 (BOJ 1932): 위에서 아래로 내려가며 합 최대.

    dp[i][j] = (i,j)에 도달했을 때의 최대 합

    >>> triangle_max_path([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
    30
    """
    n = len(triangle)
    dp = [row[:] for row in triangle]
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] += dp[i - 1][0]
            elif j == i:
                dp[i][j] += dp[i - 1][i - 1]
            else:
                dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
    return max(dp[-1])


def grid_max_path(board: list[list[int]]) -> int:
    """[유형5] 격자에서 오른쪽/아래로만 이동해 (0,0)→(n-1,m-1) 최대 합.

    >>> grid_max_path([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    12
    """
    n, m = len(board), len(board[0])
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = board[0][0]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            best = float('-inf')
            if i > 0:
                best = max(best, dp[i - 1][j])
            if j > 0:
                best = max(best, dp[i][j - 1])
            dp[i][j] = int(best) + board[i][j]
    return dp[n - 1][m - 1]


def lcs_length(a: str, b: str) -> int:
    """[유형6] 최장 공통 부분 수열 (BOJ 9251).

    dp[i][j] = a[:i] 와 b[:j] 의 LCS 길이

    >>> lcs_length("ACAYKP", "CAPCAK")
    4
    >>> lcs_length("abc", "xyz")
    0
    """
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]


def fib_topdown(n: int) -> int:
    """Top-down(재귀 + 메모이제이션) 방식 예시. @lru_cache 한 줄이면 끝.

    >>> fib_topdown(30)
    832040
    """
    @lru_cache(maxsize=None)
    def f(k: int) -> int:
        if k <= 1:
            return k
        return f(k - 1) + f(k - 2)

    return f(n)


if __name__ == "__main__":
    print("계단 오르는 경우의 수 n=5:", climb_stairs(5))
    print("1로 만들기 10:", min_steps_to_one(10))
    print("계단 오르기 최대 점수:", stairs_max_score([10, 20, 15, 25, 10, 20]))
    print("연속 부분합 최대:", max_subarray_sum([10, -4, 3, 1, 5, 6, -35, 12, 21, -1]))
    print("LIS 길이:", lis_length_dp([10, 20, 10, 30, 20, 50]))
    print("0/1 배낭:", knapsack_01([(6, 13), (4, 8), (3, 6), (5, 12)], 7))
    print("정수 삼각형:", triangle_max_path([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
    print("LCS:", lcs_length("ACAYKP", "CAPCAK"))
