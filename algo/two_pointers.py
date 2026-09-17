"""투 포인터 / 슬라이딩 윈도우 / 누적합 템플릿."""

from collections import defaultdict


def two_sum_sorted(arr: list[int], target: int) -> tuple[int, int] | None:
    """정렬된 배열에서 합이 target인 두 인덱스 (양 끝에서 좁혀오기).

    >>> two_sum_sorted([1, 3, 4, 6, 8, 9], 10)
    (0, 5)
    >>> two_sum_sorted([1, 2, 3], 100) is None
    True
    """
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == target:
            return (lo, hi)
        elif s < target:
            lo += 1                      # 합을 키우려면 왼쪽을 오른쪽으로
        else:
            hi -= 1                      # 합을 줄이려면 오른쪽을 왼쪽으로
    return None


def closest_pair_sum(arr: list[int]) -> tuple[int, int]:
    """두 용액 (BOJ 2470): 합이 0에 가장 가까운 두 값.

    >>> closest_pair_sum([-99, -2, -1, 4, 98])
    (-99, 98)
    >>> closest_pair_sum([-2, 4, -99, -1, 98])
    (-99, 98)
    """
    a = sorted(arr)
    lo, hi = 0, len(a) - 1
    best = abs(a[lo] + a[hi])
    ans = (a[lo], a[hi])
    while lo < hi:
        s = a[lo] + a[hi]
        if abs(s) < best:
            best, ans = abs(s), (a[lo], a[hi])
        if s < 0:
            lo += 1
        elif s > 0:
            hi -= 1
        else:
            break
    return ans


def count_subarrays_with_sum(arr: list[int], target: int) -> int:
    """합이 정확히 target인 연속 부분수열의 개수 (양수 배열, BOJ 2003형).

    >>> count_subarrays_with_sum([1, 2, 3, 4, 2, 5, 3, 1, 1, 2], 5)
    3
    """
    left = 0
    total = 0
    count = 0
    for right in range(len(arr)):
        total += arr[right]
        while total > target and left <= right:
            total -= arr[left]           # 초과하면 왼쪽을 줄임
            left += 1
        if total == target:
            count += 1
    return count


def shortest_subarray_at_least(arr: list[int], target: int) -> int:
    """합이 target 이상인 가장 짧은 연속 부분수열의 길이 (BOJ 1806).

    없으면 0.

    >>> shortest_subarray_at_least([5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 15)
    2
    >>> shortest_subarray_at_least([1, 1, 1], 100)
    0
    """
    left = 0
    total = 0
    best = len(arr) + 1
    for right in range(len(arr)):
        total += arr[right]
        while total >= target:
            best = min(best, right - left + 1)
            total -= arr[left]
            left += 1
    return 0 if best == len(arr) + 1 else best


def window_max_sum(arr: list[int], k: int) -> int:
    """길이 k인 연속 구간 합의 최댓값 — 슬라이딩 윈도우 O(n).

    >>> window_max_sum([1, 2, 3, 4, 5], 2)
    9
    """
    window = sum(arr[:k])
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]    # ★ 하나 넣고 하나 빼기
        best = max(best, window)
    return best


def build_prefix(arr: list[int]) -> list[int]:
    """누적합 배열. prefix[i] = arr[0] + ... + arr[i-1]

    >>> build_prefix([1, 2, 3, 4])
    [0, 1, 3, 6, 10]
    """
    prefix = [0] * (len(arr) + 1)
    for i, x in enumerate(arr):
        prefix[i + 1] = prefix[i] + x
    return prefix


def range_sum(prefix: list[int], left: int, right: int) -> int:
    """누적합으로 구간 [left, right] 합을 O(1)에 (0-indexed, right 포함).

    >>> p = build_prefix([1, 2, 3, 4, 5])
    >>> range_sum(p, 1, 3)
    9
    """
    return prefix[right + 1] - prefix[left]


def build_prefix_2d(board: list[list[int]]) -> list[list[int]]:
    """2차원 누적합. S[i][j] = (0,0)~(i-1,j-1) 직사각형의 합

    >>> S = build_prefix_2d([[1, 2], [3, 4]])
    >>> S[2][2]
    10
    """
    n, m = len(board), len(board[0])
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            S[i+1][j+1] = board[i][j] + S[i][j+1] + S[i+1][j] - S[i][j]
    return S


def range_sum_2d(S: list[list[int]], x1: int, y1: int, x2: int, y2: int) -> int:
    """(x1,y1)~(x2,y2) 직사각형 합 (양끝 포함). 포함-배제 원리.

    >>> S = build_prefix_2d([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> range_sum_2d(S, 1, 1, 2, 2)
    28
    """
    return S[x2+1][y2+1] - S[x1][y2+1] - S[x2+1][y1] + S[x1][y1]


def count_subarrays_with_sum_any(arr: list[int], target: int) -> int:
    """합이 target인 부분배열 개수 — **음수가 섞여도** 되는 버전.

    투 포인터가 안 통할 때 쓰는 누적합 + 해시 조합입니다.

    >>> count_subarrays_with_sum_any([1, -1, 0], 0)
    3
    >>> count_subarrays_with_sum_any([3, 4, 7, 2], 7)
    2
    """
    seen: defaultdict[int, int] = defaultdict(int)
    seen[0] = 1                          # 빈 접두사
    running = 0
    count = 0
    for x in arr:
        running += x
        count += seen[running - target]  # 이전 접두사 중 차이가 target인 것들
        seen[running] += 1
    return count


if __name__ == "__main__":
    print("정렬 배열 두 수의 합 10:", two_sum_sorted([1, 3, 4, 6, 8, 9], 10))
    print("두 용액:", closest_pair_sum([-99, -2, -1, 4, 98]))
    print("합이 5인 구간 개수:", count_subarrays_with_sum([1, 2, 3, 4, 2, 5, 3, 1, 1, 2], 5))
    print("합 15 이상 최단 길이:", shortest_subarray_at_least([5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 15))
    p = build_prefix([1, 2, 3, 4, 5])
    print("누적합으로 [1,3] 구간합:", range_sum(p, 1, 3))
    S = build_prefix_2d([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("2D 누적합 (1,1)~(2,2):", range_sum_2d(S, 1, 1, 2, 2))
