# 해시 (dict / set)

> **한 줄 요약**: "찾는 데 오래 걸린다" → dict나 set에 넣어라. O(n) → O(1).

가장 배우기 쉬우면서 **시간초과를 가장 많이 해결해 주는** 도구입니다.

## 핵심 아이디어

```python
# ❌ O(n²) — 매번 리스트 전체를 훑음
for x in arr:
    if x in other_list:    # O(n)
        ...

# ✅ O(n)
other = set(other_list)
for x in arr:
    if x in other:         # O(1)
        ...
```

리스트에서 `in`을 쓰고 있다면 거의 항상 set으로 바꿀 수 있습니다.

## 패턴 1. 개수 세기

```python
from collections import Counter

cnt = Counter(arr)
cnt['a']              # 없어도 0 반환 (KeyError 없음)
cnt.most_common(1)    # [('a', 5)] 가장 많은 것

# 두 배열의 공통 원소 개수
common = Counter(a) & Counter(b)
```

```python
from collections import defaultdict
cnt = defaultdict(int)
for x in arr:
    cnt[x] += 1
```

## 패턴 2. 그룹핑 (같은 성질끼리 묶기)

```python
from collections import defaultdict

# 애너그램 그룹핑: 정렬한 문자열을 키로
groups = defaultdict(list)
for word in words:
    key = ''.join(sorted(word))
    groups[key].append(word)
```

**"어떤 걸 key로 삼을까"** 를 정하는 게 해시 문제의 전부입니다.

## 패턴 3. 두 수의 합 (Two Sum)

```python
# arr에서 합이 target인 두 수가 있는가? O(n)
seen = set()
for x in arr:
    if target - x in seen:
        return True
    seen.add(x)
return False
```

"본 적 있는 값"을 저장해 두고 **짝을 찾는** 전형적인 패턴입니다.

## 패턴 4. 중복 / 등장 여부

```python
len(arr) != len(set(arr))     # 중복이 있는가
set(a) == set(b)              # 원소 구성이 같은가
set(a) - set(b)               # a에만 있는 것
```

## 패턴 5. 인덱스 기억하기

```python
pos = {v: i for i, v in enumerate(arr)}   # 값 → 인덱스
```

## 주의: 해시에 넣을 수 있는 것

`set`/`dict`의 키는 **불변(hashable)** 이어야 합니다.

```python
s.add((1, 2))        # ✅ 튜플 OK
s.add([1, 2])        # ❌ TypeError: unhashable type: 'list'
s.add(frozenset(x))  # ✅ set을 키로 쓰고 싶으면 frozenset
```

2차원 좌표를 방문 체크할 때 `visited.add((x, y))` 처럼 **튜플**로 넣습니다.

> 실행 가능한 코드: [`algo/sorting_hash.py`](../../algo/sorting_hash.py)

## 추천 문제

| 문제 | 난이도 | 포인트 |
|---|---|---|
| [BOJ 10815 숫자 카드](https://www.acmicpc.net/problem/10815) | 실버5 | set의 위력 체감 ★ |
| [BOJ 1764 듣보잡](https://www.acmicpc.net/problem/1764) | 실버4 | 교집합 |
| [BOJ 7785 회사에 있는 사람](https://www.acmicpc.net/problem/7785) | 실버5 | set 추가/삭제 |
| [프로그래머스 완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576) | Lv1 | Counter ★ |
| [프로그래머스 전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577) | Lv2 | 접두사 + 해시 |
| [프로그래머스 의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578) | Lv2 | 그룹핑 + 경우의 수 |
