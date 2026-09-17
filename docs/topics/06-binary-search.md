# 이분 탐색 (Binary Search)

> **한 줄 요약**: 정렬되어 있으면 O(log n). 그리고 **"답을 이분탐색"** 하는 게 진짜 시험 범위.

## 1. 기본형 — 정렬된 배열에서 값 찾기

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

**전제 조건: 배열이 정렬되어 있어야 합니다.** 안 되어 있으면 먼저 `sort()`.

## 2. bisect — 직접 구현하지 말고 이걸 쓰세요

```python
import bisect

bisect.bisect_left(arr, x)    # x가 들어갈 가장 왼쪽 위치 (x 이상이 시작되는 곳)
bisect.bisect_right(arr, x)   # x가 들어갈 가장 오른쪽 위치 (x 초과가 시작되는 곳)

# x의 개수
bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)

# a 이상 b 이하인 원소의 개수
bisect.bisect_right(arr, b) - bisect.bisect_left(arr, a)

bisect.insort(arr, x)         # 정렬 유지하며 삽입
```

"정렬된 배열에서 범위 개수 세기"는 `bisect` 두 줄로 끝납니다.

## 3. 파라메트릭 서치 ★ 실제 시험에 나오는 건 이것

**"최댓값의 최솟값", "최솟값의 최댓값", "가능한 최대 크기"** 라는 말이 나오면 90% 이 유형입니다.

아이디어: **정답 자체를 이분탐색합니다.**

> "길이 X로 자를 수 있나?" 라는 질문에 Yes/No로 답할 수 있고,
> X가 작으면 Yes, 크면 No처럼 **단조롭게** 바뀐다면 → X를 이분탐색

### 템플릿

```python
def parametric(lo, hi, possible):
    """possible(x)가 True인 x 중 최댓값을 찾는다.
    (x가 작을수록 True인 단조 구조라고 가정)"""
    answer = lo
    while lo <= hi:
        mid = (lo + hi) // 2
        if possible(mid):
            answer = mid        # 가능하니 기록하고
            lo = mid + 1        # 더 크게 시도
        else:
            hi = mid - 1        # 불가능하니 줄임
    return answer
```

### 예시: 랜선 자르기 (BOJ 1654)

N개의 랜선을 잘라서 M개 이상을 만들 때, 가능한 최대 길이는?

```python
def max_len(lines, m):
    def count(length):
        return sum(x // length for x in lines)

    lo, hi = 1, max(lines)
    answer = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if count(mid) >= m:     # mid 길이로 m개 이상 만들 수 있다
            answer = mid
            lo = mid + 1        # 더 길게 해보자
        else:
            hi = mid - 1
    return answer
```

핵심은 `count(mid)`라는 **판정 함수**를 만드는 것입니다.
"이 값이 가능한가?"만 판정할 수 있으면 나머지는 템플릿입니다.

→ 실행 코드: [`algo/binary_search.py`](../../algo/binary_search.py)

## 4. 무한 루프 피하기

이분탐색의 유일한 함정은 **무한 루프**입니다.

- `while lo <= hi` + `lo = mid + 1` / `hi = mid - 1` → 안전 (이 조합만 쓰세요)
- `while lo < hi` + `hi = mid` → 조건에 따라 무한 루프 위험

헷갈리면 **항상 위 조합만** 사용하세요. 한 가지만 확실히 외우는 게 낫습니다.

## 5. 문제에서 파라메트릭 서치를 알아채는 신호

- "가능한 **최대/최소** 값을 구하시오"
- "**적어도** M개 이상 만들 수 있는..."
- N이 크고(10^5~10^9), 답의 범위도 큰데 완전탐색은 불가능해 보임
- "X일 때 가능한지 확인하는 건 쉬움"

## 추천 문제

| 문제 | 난이도 | 포인트 |
|---|---|---|
| [BOJ 1920 수 찾기](https://www.acmicpc.net/problem/1920) | 실버4 | 기본 이분탐색 ★ |
| [BOJ 10816 숫자 카드 2](https://www.acmicpc.net/problem/10816) | 실버4 | bisect로 개수 세기 |
| [BOJ 2805 나무 자르기](https://www.acmicpc.net/problem/2805) | 실버2 | 파라메트릭 입문 ★★ |
| [BOJ 1654 랜선 자르기](https://www.acmicpc.net/problem/1654) | 실버2 | 파라메트릭 ★★ |
| [BOJ 2110 공유기 설치](https://www.acmicpc.net/problem/2110) | 골드4 | 판정 함수 설계 ★ |
| [BOJ 1300 K번째 수](https://www.acmicpc.net/problem/1300) | 골드2 | 난이도 있는 응용 |
