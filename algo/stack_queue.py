"""스택 / 큐 / 덱 / 힙 템플릿."""

from collections import deque
from heapq import heapify, heappop, heappush


def is_balanced(s: str) -> bool:
    """괄호 짝 맞추기 (BOJ 9012형). 스택의 교과서 예제.

    >>> is_balanced("(())")
    True
    >>> is_balanced("(()")
    False
    >>> is_balanced("{[()]}")
    True
    >>> is_balanced(")(")
    False
    """
    pairs = {')': '(', ']': '[', '}': '{'}
    stack: list[str] = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack                 # 남은 게 있으면 짝이 안 맞음


def remove_adjacent_pairs(s: str) -> str:
    """인접한 같은 문자를 짝지어 지우기. '되돌리기' 패턴.

    >>> remove_adjacent_pairs("abbaca")
    'ca'
    >>> remove_adjacent_pairs("aabb")
    ''
    """
    stack: list[str] = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)


def next_greater(arr: list[int]) -> list[int]:
    """오큰수 (BOJ 17298) — Monotonic Stack. O(n).

    각 원소의 오른쪽에서 자기보다 큰 첫 번째 수. 없으면 -1.

    >>> next_greater([3, 5, 2, 7])
    [5, 7, 7, -1]
    >>> next_greater([9, 5, 4, 8])
    [-1, 8, 8, -1]
    """
    n = len(arr)
    res = [-1] * n
    stack: list[int] = []                 # 인덱스를 저장 (값이 아님!)
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            res[stack.pop()] = arr[i]     # 기다리던 원소들의 답이 확정됨
        stack.append(i)
    return res


def sliding_window_max(arr: list[int], k: int) -> list[int]:
    """크기 k 창의 최댓값들 — Monotonic Deque. O(n).

    >>> sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3)
    [3, 3, 5, 5, 6, 7]
    """
    dq: deque[int] = deque()              # 값이 내림차순이 되도록 인덱스를 유지
    res: list[int] = []
    for i, x in enumerate(arr):
        while dq and arr[dq[-1]] <= x:
            dq.pop()                      # 나보다 작은 건 영원히 최댓값이 못 됨
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()                  # 창 밖으로 나간 인덱스 제거
        if i >= k - 1:
            res.append(arr[dq[0]])
    return res


def josephus(n: int, k: int) -> list[int]:
    """요세푸스 문제 (BOJ 1158) — deque.rotate 활용.

    >>> josephus(7, 3)
    [3, 6, 2, 7, 5, 1, 4]
    """
    dq = deque(range(1, n + 1))
    res = []
    while dq:
        dq.rotate(-(k - 1))               # k번째가 맨 앞에 오도록 회전
        res.append(dq.popleft())
    return res


def merge_cards_min_cost(cards: list[int]) -> int:
    """카드 정렬하기 (BOJ 1715) — 작은 것부터 합치는 그리디 + 힙.

    두 묶음을 합칠 때마다 (a+b) 비용 발생. 총 비용의 최솟값.

    >>> merge_cards_min_cost([10, 20, 40])
    100
    >>> merge_cards_min_cost([5])
    0
    """
    if len(cards) <= 1:
        return 0
    h = cards[:]
    heapify(h)
    total = 0
    while len(h) > 1:
        a, b = heappop(h), heappop(h)     # 항상 가장 작은 둘
        total += a + b
        heappush(h, a + b)
    return total


def kth_smallest_stream(nums: list[int], k: int) -> list[int]:
    """스트림에서 매 시점의 k번째 작은 수 (최대 힙 활용 예시).

    힙에 k개만 유지하면서, 최대 힙으로 가장 큰 것을 버립니다.

    >>> kth_smallest_stream([5, 1, 4, 2, 3], 2)
    [5, 5, 4, 2, 2]
    """
    max_heap: list[int] = []              # 부호를 뒤집어 최대 힙처럼 사용
    res = []
    for x in nums:
        heappush(max_heap, -x)
        if len(max_heap) > k:
            heappop(max_heap)             # 가장 큰 것 제거
        res.append(-max_heap[0])
    return res


if __name__ == "__main__":
    print("괄호 검사 '{[()]}':", is_balanced("{[()]}"))
    print("인접 중복 제거 'abbaca':", remove_adjacent_pairs("abbaca"))
    print("오큰수 [3,5,2,7]:", next_greater([3, 5, 2, 7]))
    print("슬라이딩 최댓값 k=3:", sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print("요세푸스 (7,3):", josephus(7, 3))
    print("카드 정렬 [10,20,40]:", merge_cards_min_cost([10, 20, 40]))
