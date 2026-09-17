"""정렬 key 패턴과 해시(dict/set) 패턴 모음 — 2주차용."""

import bisect
from collections import Counter, defaultdict


def sort_multi_key(people: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """다중 조건 정렬: 점수 내림차순, 같으면 이름 오름차순. ★ 최빈출 패턴

    >>> sort_multi_key([("bob", 90), ("amy", 90), ("cho", 95)])
    [('cho', 95), ('amy', 90), ('bob', 90)]
    """
    return sorted(people, key=lambda x: (-x[1], x[0]))


def sort_stable_two_pass(people: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """문자열 내림차순이 섞여 '-' 트릭을 못 쓸 때: 안정 정렬을 2번 돌립니다.

    (2순위 기준으로 먼저, 1순위 기준으로 나중에)

    >>> sort_stable_two_pass([("bob", 90), ("amy", 90), ("cho", 95)])
    [('cho', 95), ('amy', 90), ('bob', 90)]
    """
    result = sorted(people, key=lambda x: x[0])              # 2순위: 이름 오름차순
    result.sort(key=lambda x: x[1], reverse=True)            # 1순위: 점수 내림차순
    return result


def counting_sort(nums: list[int], max_value: int) -> list[int]:
    """계수 정렬 O(N) — 값의 범위가 작고 입력이 아주 클 때 (BOJ 10989).

    >>> counting_sort([5, 2, 3, 1, 4, 2, 3, 5, 1, 7], 10)
    [1, 1, 2, 2, 3, 3, 4, 5, 5, 7]
    """
    cnt = [0] * (max_value + 1)
    for x in nums:
        cnt[x] += 1
    result = []
    for v in range(max_value + 1):
        result.extend([v] * cnt[v])
    return result


def compress_coordinates(arr: list[int]) -> list[int]:
    """좌표 압축: 값 대신 '순위'만 필요할 때 (BOJ 18870).

    >>> compress_coordinates([2, 4, -10, 4, -9])
    [2, 3, 0, 3, 1]
    """
    rank = {v: i for i, v in enumerate(sorted(set(arr)))}
    return [rank[x] for x in arr]


def group_anagrams(words: list[str]) -> list[list[str]]:
    """해시 그룹핑: 어떤 걸 key로 삼을지 정하는 게 전부입니다.

    >>> group_anagrams(["eat", "tea", "tan", "ate", "nat"])
    [['eat', 'tea', 'ate'], ['tan', 'nat']]
    """
    groups: defaultdict[str, list[str]] = defaultdict(list)
    for w in words:
        groups[''.join(sorted(w))].append(w)        # 정렬한 문자열을 key로
    return list(groups.values())


def has_two_sum(arr: list[int], target: int) -> bool:
    """정렬 없이 O(n)으로 두 수의 합 판정 — '본 적 있는 값'을 set에 저장.

    >>> has_two_sum([2, 7, 11, 15], 9)
    True
    >>> has_two_sum([1, 2, 3], 100)
    False
    """
    seen: set[int] = set()
    for x in arr:
        if target - x in seen:
            return True
        seen.add(x)
    return False


def not_finished(participant: list[str], completion: list[str]) -> str:
    """완주하지 못한 선수 (프로그래머스 Lv1) — Counter 뺄셈.

    >>> not_finished(["leo", "kiki", "eden"], ["eden", "kiki"])
    'leo'
    >>> not_finished(["mis", "mis", "ola"], ["ola", "mis"])
    'mis'
    """
    remain = Counter(participant) - Counter(completion)
    return next(iter(remain))


def exists_in_sorted(cards: list[int], queries: list[int]) -> list[int]:
    """숫자 카드 (BOJ 10815): 있으면 1, 없으면 0.

    set으로 해도 되고, 정렬 + bisect로도 됩니다. set이 더 빠릅니다.

    >>> exists_in_sorted([6, 3, 2, 10, -10], [10, 9, -5, 2, 3])
    [1, 0, 0, 1, 1]
    """
    have = set(cards)
    return [1 if q in have else 0 for q in queries]


def count_occurrences(cards: list[int], queries: list[int]) -> list[int]:
    """숫자 카드 2 (BOJ 10816): 각 질의 값이 몇 개인지.

    >>> count_occurrences([6, 3, 2, 10, 10, 10, -10, -10, 7, 3], [10, 9, -5, 2, 3, 4, 5, -10])
    [3, 0, 0, 1, 2, 0, 0, 2]
    """
    cnt = Counter(cards)
    return [cnt[q] for q in queries]


def count_in_sorted_range(arr: list[int], low: int, high: int) -> int:
    """정렬 + bisect로 범위 개수 세기 (Counter로 못 푸는 '범위' 질의용).

    >>> count_in_sorted_range([1, 2, 2, 3, 5, 5, 8], 2, 5)
    5
    """
    a = sorted(arr)
    return bisect.bisect_right(a, high) - bisect.bisect_left(a, low)


if __name__ == "__main__":
    print("다중조건 정렬:", sort_multi_key([("bob", 90), ("amy", 90), ("cho", 95)]))
    print("계수 정렬:", counting_sort([5, 2, 3, 1, 4], 5))
    print("좌표 압축:", compress_coordinates([2, 4, -10, 4, -9]))
    print("애너그램 그룹:", group_anagrams(["eat", "tea", "tan", "ate", "nat"]))
    print("두 수의 합 존재?:", has_two_sum([2, 7, 11, 15], 9))
    print("완주 못한 선수:", not_finished(["mis", "mis", "ola"], ["ola", "mis"]))
