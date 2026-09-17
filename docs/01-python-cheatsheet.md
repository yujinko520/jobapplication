# 01. 코테용 Python 치트시트

Python을 다뤄봤어도 **코테에서 쓰는 Python은 조금 다릅니다.**
여기 있는 것만 알면 90% 이상의 문제를 풀 수 있습니다.

## 1. 리스트

```python
arr = [3, 1, 4, 1, 5]

arr.append(9)          # 뒤에 추가          O(1)
arr.pop()              # 뒤에서 꺼내기      O(1)
arr.pop(0)             # 앞에서 꺼내기      O(n) ← 느림! deque 쓰세요
arr.insert(0, 7)       # 앞에 삽입          O(n) ← 느림!
arr.remove(1)          # 값 1을 "하나만" 삭제 O(n)
len(arr), sum(arr), max(arr), min(arr)
arr.count(1)           # 1이 몇 개          O(n)
arr.index(4)           # 4의 위치 (없으면 ValueError)
1 in arr               # 포함 여부          O(n) ← set이면 O(1)
```

### 슬라이싱

```python
arr[2:5]     # 2 이상 5 미만
arr[:3]      # 처음 3개
arr[-3:]     # 마지막 3개
arr[::-1]    # 뒤집기 (자주 씀!)
arr[::2]     # 2칸씩
```

### 리스트 컴프리헨션 — 코테에서 제일 자주 씁니다

```python
squares = [x * x for x in range(10)]
evens   = [x for x in arr if x % 2 == 0]
pairs   = [(i, j) for i in range(3) for j in range(3)]

# 2차원 배열 만들기 ★ 함정 주의
board = [[0] * m for _ in range(n)]   # ✅ 올바름
board = [[0] * m] * n                 # ❌ 같은 행을 n번 참조! 한 칸 바꾸면 전부 바뀜
```

`[[0] * m] * n` 버그는 정말 자주 나옵니다. 꼭 위쪽 방식으로 쓰세요.

## 2. 문자열

문자열은 **불변(immutable)** 입니다. `s[0] = 'a'` 안 됩니다.

```python
s = "Hello World"

s.split()              # ['Hello', 'World']  (공백 기준)
s.split(',')           # 쉼표 기준
''.join(['a','b'])     # 'ab'   ← 문자열 += 반복보다 훨씬 빠름
s.strip()              # 양끝 공백 제거
s.rstrip()             # 오른쪽만 (입력 받을 때 필수)
s.replace('l', 'L')
s.upper(), s.lower()
s.isdigit(), s.isalpha()
s.startswith('He'), s.endswith('ld')
s.find('lo')           # 위치, 없으면 -1
ord('a'), chr(97)      # 문자 ↔ 아스키 (97 ↔ 'a', 65 ↔ 'A')
```

> **문자열을 반복해서 `+=` 하지 마세요.** 매번 새 문자열을 만들어서 O(n²)입니다.
> 리스트에 모았다가 마지막에 `''.join()` 하세요.

## 3. dict / set — "탐색을 O(1)로" 만드는 도구

```python
d = {}
d['a'] = 1
d.get('b', 0)          # 없으면 0 반환 (KeyError 방지)
d.keys(), d.values(), d.items()
for k, v in d.items(): ...
'a' in d               # O(1) ★

s = set([1, 2, 2, 3])  # {1, 2, 3}  중복 자동 제거
s.add(4); s.discard(1) # discard는 없어도 에러 안 남
a & b, a | b, a - b    # 교집합, 합집합, 차집합
```

**"리스트에서 `in`으로 찾고 있다면 set으로 바꿔라"** — 시간초과 해결의 절반입니다.

### collections

```python
from collections import defaultdict, Counter, deque

# defaultdict: 없는 키를 자동 초기화
graph = defaultdict(list)
graph[1].append(2)            # graph[1]이 없어도 에러 안 남

cnt = defaultdict(int)
cnt['a'] += 1                 # 0에서 시작

# Counter: 개수 세기
c = Counter("hello")          # {'l': 2, 'h': 1, 'e': 1, 'o': 1}
c.most_common(2)              # [('l', 2), ('h', 1)] 상위 2개

# deque: 양쪽에서 O(1)  ← BFS의 필수품
q = deque([1, 2, 3])
q.append(4); q.appendleft(0)
q.pop();     q.popleft()      # ★ list.pop(0)은 O(n), deque.popleft()는 O(1)
```

## 4. 정렬

```python
arr.sort()                       # 제자리 정렬 (원본 변경)
new = sorted(arr)                # 새 리스트 반환
arr.sort(reverse=True)           # 내림차순

# key: 정렬 기준
students.sort(key=lambda x: x[1])              # 두 번째 원소 기준
students.sort(key=lambda x: (-x[1], x[0]))     # 점수 내림차순, 같으면 이름 오름차순 ★
words.sort(key=len)                            # 길이순
```

`key=lambda x: (-a, b)` 패턴(다중 조건 정렬)은 시험에 정말 자주 나옵니다.

## 5. 수학 / 진법

```python
a // b          # 몫 (내림). -7 // 2 == -4 주의!
a % b           # 나머지
divmod(a, b)    # (몫, 나머지) 동시에
abs(-3)
pow(2, 10)      # 1024
pow(2, 10, 7)   # 2^10 % 7  (거듭제곱 나머지, 빠름)
10 ** 9 + 7     # MOD 자주 쓰이는 값

import math
math.gcd(12, 18)        # 최대공약수 6
math.lcm(4, 6)          # 최소공배수 12 (3.9+)
math.sqrt(16)           # 4.0  (실수! 정수 필요하면 int(x**0.5))
math.ceil(7/2)          # 4  (올림)
math.inf                # 무한대 (최솟값 찾을 때 초기값)

bin(10)         # '0b1010'
int('1010', 2)  # 10
format(10, 'b') # '1010'  (접두사 없이)
```

## 6. itertools — 완전탐색의 친구

```python
from itertools import permutations, combinations, product

list(permutations([1,2,3], 2))   # 순열: (1,2) (1,3) (2,1) (2,3) (3,1) (3,2)
list(combinations([1,2,3], 2))   # 조합: (1,2) (1,3) (2,3)
list(product([0,1], repeat=3))   # 중복순열: (0,0,0) (0,0,1) ... 8가지
```

"모든 경우를 다 해보면 되는데 n이 작다" → 이 셋 중 하나입니다.

## 7. heapq — 우선순위 큐 (항상 최솟값이 먼저)

```python
from heapq import heappush, heappop, heapify

h = []
heappush(h, 5); heappush(h, 1); heappush(h, 3)
heappop(h)      # 1  ← 항상 최솟값

heappush(h, -x)        # 최대 힙은 부호를 뒤집어서
heappush(h, (거리, 노드))  # 튜플이면 첫 원소 기준 정렬 → 다익스트라
```

## 8. 기타 자주 쓰는 것

```python
enumerate(arr)              # (인덱스, 값) 쌍
zip(a, b)                   # 두 리스트 짝짓기
list(zip(*matrix))          # 행렬 전치(transpose) ★ 회전 문제에 씀
any([...]), all([...])
bisect.bisect_left(arr, x)  # 정렬된 리스트에서 삽입 위치 (이분탐색)

from functools import lru_cache
@lru_cache(maxsize=None)    # 메모이제이션 자동화 (DP에 유용)
def f(n): ...
```

## 9. 실수하기 쉬운 지점 정리

| 실수 | 결과 | 해결 |
|---|---|---|
| `[[0]*m]*n` | 행이 전부 같이 바뀜 | `[[0]*m for _ in range(n)]` |
| 리스트에 `in` 사용 | 시간초과 | `set`으로 변환 |
| `list.pop(0)` 반복 | 시간초과 | `deque.popleft()` |
| 문자열 `+=` 반복 | 시간초과 | `''.join()` |
| `input()` 그대로 | 시간초과 | `sys.stdin.readline` |
| 재귀 DFS 깊이 | 런타임 에러 | `setrecursionlimit` 또는 스택 |
| `/` 와 `//` 혼동 | 실수/정수 오류 | 정수 나눗셈은 `//` |
| 반복문 안에서 `print` | 느림 | 모아서 한 번에 |

---

다음: [02. 시간복잡도](02-complexity.md)
