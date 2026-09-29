# 스택 / 큐 / 덱

> **한 줄 요약**: "직전 것과 비교해야 한다" → 스택. "먼저 온 순서대로" → 큐.

## 스택 (LIFO, 나중에 넣은 게 먼저 나옴)

Python은 그냥 **리스트**가 스택입니다.

```python
stack = []
stack.append(x)    # push  O(1)
stack.pop()        # pop   O(1)
stack[-1]          # top (peek)
if stack: ...      # 비었는지 확인 (pop 전에 항상!)
```

⚠️ 빈 스택에 `pop()` 하면 `IndexError`. **반드시 `if stack:` 으로 먼저 확인**하세요.

### 패턴 1. 괄호 짝 맞추기 (스택의 교과서)

```python
def is_valid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack        # 남은 게 있으면 짝이 안 맞음
```

### 패턴 2. 되돌리기 / 직전 상태

"마지막 것을 취소한다", "직전 문자와 같으면 지운다" → 전부 스택.

```python
# 연속 중복 제거 (짝지어 사라지기)
stack = []
for ch in s:
    if stack and stack[-1] == ch:
        stack.pop()
    else:
        stack.append(ch)
```

### 패턴 3. 다음 큰 수 (Monotonic Stack) — 골드권 단골

"오른쪽에서 자기보다 큰 첫 번째 수"를 **O(n)** 에 구합니다.

```python
def next_greater(arr):
    n = len(arr)
    res = [-1] * n
    stack = []                      # 인덱스를 저장
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            res[stack.pop()] = arr[i]
        stack.append(i)
    return res
```

각 원소가 push/pop 각 1번씩만 되므로 O(n)입니다. 이 아이디어는 꼭 이해하세요.
→ 실행 코드: [`algo/stack_queue.py`](../../algo/stack_queue.py)

## 큐 (FIFO, 먼저 넣은 게 먼저 나옴)

**반드시 `deque`를 쓰세요.** `list.pop(0)`은 O(n)이라 시간초과 납니다.

```python
from collections import deque

q = deque()
q.append(x)        # 뒤에 넣기    O(1)
q.popleft()        # 앞에서 빼기  O(1) ★
q[0]               # 맨 앞 보기
while q: ...
```

큐의 대표 용도는 **BFS**입니다. (→ [05-bfs-dfs.md](05-bfs-dfs.md))

## 덱 (양쪽에서 다 되는 큐)

```python
dq = deque()
dq.append(x);     dq.appendleft(x)
dq.pop();         dq.popleft()
dq.rotate(1)      # 오른쪽으로 회전 (회전 문제에 유용)
dq = deque(arr, maxlen=3)   # 크기 제한 (넘치면 반대쪽이 밀려남)
```

### 슬라이딩 윈도우 최댓값 (Monotonic Deque)

크기 k인 창을 옮기며 최댓값을 **O(n)** 에 구합니다.

```python
def sliding_max(arr, k):
    dq, res = deque(), []          # dq: 인덱스, 값이 내림차순
    for i, x in enumerate(arr):
        while dq and arr[dq[-1]] <= x:
            dq.pop()               # 나보다 작은 건 영원히 최댓값이 못 됨
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()           # 창 밖으로 나간 것 제거
        if i >= k - 1:
            res.append(arr[dq[0]])
    return res
```

## 우선순위 큐 (heapq)

"가장 작은/큰 것부터 꺼내야 한다" → 힙.

```python
from heapq import heappush, heappop, heapify

h = []
heappush(h, 3)
heappop(h)                 # 항상 최솟값  O(log n)
heapify(arr)               # 리스트를 힙으로 O(n)

heappush(h, -x)            # 최대 힙: 부호 반전
heappush(h, (우선순위, 데이터))   # 튜플이면 첫 원소 기준
```

용도: 다익스트라, "매번 가장 작은 것 두 개를 합치기"(카드 정렬), 중앙값 유지 등.

## 어떤 걸 쓸지 고르는 법

| 상황 | 자료구조 |
|---|---|
| 직전 것과 비교 / 되돌리기 / 괄호 | 스택 |
| 먼저 온 순서대로 처리 / 최단거리 탐색 | 큐 (deque) |
| 양쪽에서 넣고 빼기 / 슬라이딩 윈도우 | 덱 |
| 매번 최솟값(최댓값)이 필요 | 힙 (heapq) |

## 추천 문제 (프로그래머스)

| 문제 | 레벨 | 포인트 |
|---|---|---|
| [같은 숫자는 싫어](https://school.programmers.co.kr/learn/courses/30/lessons/12906) | Lv.1 | 스택 기본 ★ |
| [올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909) | Lv.2 | 괄호 짝 — 스택의 교과서 ★★ |
| [크레인 인형뽑기 게임](https://school.programmers.co.kr/learn/courses/30/lessons/64061) | Lv.2 | 스택 여러 개 다루기 ★ |
| [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586) | Lv.2 | 큐 처리 |
| [프린터](https://school.programmers.co.kr/learn/courses/30/lessons/42587) | Lv.2 | deque 회전 |
| [다리를 지나는 트럭](https://school.programmers.co.kr/learn/courses/30/lessons/42583) | Lv.2 | 큐 시뮬레이션 ★ |
| [주식가격](https://school.programmers.co.kr/learn/courses/30/lessons/42584) | Lv.2 | Monotonic Stack ★★ |
| [더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626) | Lv.2 | 힙(heapq) ★★ |
| [이중우선순위큐](https://school.programmers.co.kr/learn/courses/30/lessons/42628) | Lv.3 | 힙 두 개 (도전) |

> **주식가격**은 O(n²)로도 통과되지만, **스택으로 O(n)에 푸는 방법**을 꼭 익히세요.
> 이 아이디어가 Lv.3 이상에서 계속 나옵니다.
