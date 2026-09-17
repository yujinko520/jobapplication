"""이분 탐색 / 파라메트릭 서치 템플릿."""

import bisect
from typing import Callable


def binary_search(arr: list[int], target: int) -> int:
    """정렬된 배열에서 target의 인덱스. 없으면 -1.

    >>> binary_search([1, 3, 5, 7, 9], 7)
    3
    >>> binary_search([1, 3, 5, 7, 9], 4)
    -1
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:                      # ★ 이 조합만 쓰면 무한루프가 없습니다
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def count_in_range(arr: list[int], low: int, high: int) -> int:
    """정렬된 배열에서 low 이상 high 이하인 원소의 개수. bisect로 두 줄.

    >>> count_in_range([1, 2, 2, 3, 5, 5, 5, 8], 2, 5)
    6
    >>> count_in_range([1, 2, 2, 3], 4, 9)
    0
    """
    return bisect.bisect_right(arr, high) - bisect.bisect_left(arr, low)


def parametric_max(lo: int, hi: int, possible: Callable[[int], bool]) -> int:
    """possible(x)가 True인 가장 큰 x를 찾습니다.

    (x가 작을수록 True인 단조 구조를 가정 — 파라메트릭 서치의 표준형)

    >>> parametric_max(1, 100, lambda x: x * x <= 50)
    7
    """
    answer = lo - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if possible(mid):
            answer = mid                 # 가능하니 기록하고
            lo = mid + 1                 # 더 크게 시도
        else:
            hi = mid - 1                 # 불가능하니 줄임
    return answer


def parametric_min(lo: int, hi: int, possible: Callable[[int], bool]) -> int:
    """possible(x)가 True인 가장 작은 x. (x가 클수록 True인 구조)

    >>> parametric_min(1, 100, lambda x: x * x >= 50)
    8
    """
    answer = hi + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if possible(mid):
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer


def max_lan_length(lines: list[int], need: int) -> int:
    """랜선 자르기 (BOJ 1654): need개 이상 만들 수 있는 최대 길이.

    >>> max_lan_length([802, 743, 457, 539], 11)
    200
    """
    def can_make(length: int) -> bool:
        return sum(x // length for x in lines) >= need

    return parametric_max(1, max(lines), can_make)


def max_tree_cut_height(trees: list[int], need: int) -> int:
    """나무 자르기 (BOJ 2805): need 이상 가져갈 수 있는 절단기 최대 높이.

    >>> max_tree_cut_height([20, 15, 10, 17], 7)
    15
    """
    def can_take(height: int) -> bool:
        return sum(max(0, t - height) for t in trees) >= need

    return parametric_max(0, max(trees), can_take)


def max_router_gap(houses: list[int], routers: int) -> int:
    """공유기 설치 (BOJ 2110): 가장 인접한 두 공유기 거리의 최댓값.

    >>> max_router_gap([1, 2, 8, 4, 9], 3)
    3
    """
    houses = sorted(houses)

    def can_place(gap: int) -> bool:
        """간격을 gap 이상으로 두고 routers개를 놓을 수 있는가"""
        count, last = 1, houses[0]
        for h in houses[1:]:
            if h - last >= gap:
                count += 1
                last = h
        return count >= routers

    return parametric_max(1, houses[-1] - houses[0], can_place)


def lis_length(arr: list[int]) -> int:
    """가장 긴 증가 부분 수열의 길이 — O(n log n) (이분탐색 응용).

    >>> lis_length([10, 20, 10, 30, 20, 50])
    4
    >>> lis_length([])
    0
    """
    tails: list[int] = []                # tails[i] = 길이 i+1 수열의 마지막 값 최솟값
    for x in arr:
        pos = bisect.bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
    return len(tails)


if __name__ == "__main__":
    print("이분탐색 [1,3,5,7,9]에서 7:", binary_search([1, 3, 5, 7, 9], 7))
    print("2~5 범위 개수:", count_in_range([1, 2, 2, 3, 5, 5, 5, 8], 2, 5))
    print("랜선 자르기:", max_lan_length([802, 743, 457, 539], 11))
    print("나무 자르기:", max_tree_cut_height([20, 15, 10, 17], 7))
    print("공유기 설치:", max_router_gap([1, 2, 8, 4, 9], 3))
    print("LIS 길이:", lis_length([10, 20, 10, 30, 20, 50]))
