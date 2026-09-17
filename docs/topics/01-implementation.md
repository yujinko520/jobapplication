# 구현 / 완전탐색 (Brute Force)

> **한 줄 요약**: 다 해본다. N이 작으면 이게 정답이다.

## 언제 쓰나

- 제한이 `N ≤ 10~20` 처럼 유난히 작을 때
- "모든 경우의 수 중 최댓값/최솟값" 을 물을 때
- 문제에 특별한 성질이 안 보이고 그냥 시키는 대로 하면 될 때 (= 구현 문제)

초보자가 가장 많이 하는 실수: **N이 작은데 어려운 알고리즘을 찾으려 함.**
N ≤ 20이면 다 해보라는 뜻입니다.

## 패턴 1. 반복문 완전탐색

```python
# 배열에서 세 수를 골라 합이 M 이하인 최댓값 (N ≤ 100)
best = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            s = arr[i] + arr[j] + arr[k]
            if s <= m:
                best = max(best, s)
```

## 패턴 2. itertools (제일 빠르고 안전)

```python
from itertools import permutations, combinations, product

# 순열: 순서가 중요 (1,2) ≠ (2,1)
for p in permutations(arr, 3): ...

# 조합: 순서 무관, 뽑기만
for c in combinations(arr, 3): ...

# 중복순열: 각 칸에 0 또는 1을 n번 (2^n 가지)
for p in product([0, 1], repeat=n): ...
```

**어떤 걸 쓸지 고르는 법**
- "순서를 바꾸면 다른 경우" → `permutations`
- "뽑기만 하면 됨" → `combinations`
- "각 자리에 여러 선택지, 중복 허용" → `product`

## 패턴 3. 비트마스크 부분집합 (N ≤ 20)

```python
n = len(arr)
for mask in range(1 << n):              # 0 ~ 2^n - 1
    subset = [arr[i] for i in range(n) if mask & (1 << i)]
    # subset 처리
```

`mask & (1 << i)` = "i번째 원소를 선택했는가". 2^20 = 약 100만이라 충분히 돕니다.

## 패턴 4. 백트래킹 (가지치기)

완전탐색인데 **가망 없는 가지를 미리 잘라내는** 것.

```python
def backtrack(depth, current):
    if depth == n:
        answer.append(current[:])   # ★ 복사해서 저장 (안 하면 다 같은 값)
        return
    for x in candidates:
        if not promising(x):        # 가지치기
            continue
        current.append(x)
        backtrack(depth + 1, current)
        current.pop()               # ★ 되돌리기 (backtrack의 핵심)
```

**"넣고 → 재귀 → 빼기"** 3단계가 백트래킹의 전부입니다.
→ 실행 가능한 코드: [`algo/backtracking.py`](../../algo/backtracking.py)

## 시뮬레이션(구현) 문제 팁

"로봇이 명령대로 움직인다", "배열을 회전시킨다" 같은 문제는
알고리즘이 아니라 **꼼꼼함** 시험입니다.

```python
# 상하좌우 이동 (격자 문제의 표준)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for d in range(4):
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:     # ★ 경계 검사 항상!
        ...
```

```python
# 90도 시계방향 회전
rotated = [list(row) for row in zip(*board[::-1])]
```

- 방향 배열(`dx`, `dy`)은 **손가락이 기억할 때까지** 쓰세요
- 경계 검사 `0 <= nx < n and 0 <= ny < m` 를 빼먹으면 런타임 에러
- 문제를 **작은 함수로 쪼개세요** (move, rotate, check) — 한 함수에 다 넣으면 디버깅 불가

## 추천 문제

| 문제 | 난이도 | 포인트 |
|---|---|---|
| [BOJ 2798 블랙잭](https://www.acmicpc.net/problem/2798) | 브론즈2 | 3중 반복문 첫걸음 |
| [BOJ 2231 분해합](https://www.acmicpc.net/problem/2231) | 브론즈2 | 범위 잡기 |
| [BOJ 15649 N과 M(1)](https://www.acmicpc.net/problem/15649) | 실버3 | 백트래킹 입문 ★ |
| [BOJ 14500 테트로미노](https://www.acmicpc.net/problem/14500) | 골드5 | 구현 + 완전탐색 |
| [BOJ 14888 연산자 끼워넣기](https://www.acmicpc.net/problem/14888) | 실버1 | 순열 완전탐색 ★ |
| [BOJ 14889 스타트와 링크](https://www.acmicpc.net/problem/14889) | 실버1 | 조합 |

> **N과 M 시리즈(15649~15656)를 전부 푸세요.** 백트래킹 감각이 확실히 잡힙니다.
