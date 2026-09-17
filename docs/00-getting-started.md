# 00. 시작하기 — 환경과 입출력

## 1. 환경 준비

**로컬 환경은 최소한만.** 코테는 대부분 웹 IDE에서 봅니다.

- Python 3.x (3.8 이상이면 충분)
- 에디터: VS Code (확장: Python)
- 그 외 라이브러리 설치 불필요. **표준 라이브러리만 씁니다.**
  (numpy, pandas는 대부분의 코테 환경에서 쓸 수 없다고 가정하세요)

실제 시험장에서 쓸 수 있는 건 이 정도입니다:

```python
import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from itertools import permutations, combinations, product
from functools import lru_cache
import math, bisect
```

이 7줄이 코테 Python의 전부입니다. 외워두세요.

## 2. 입력 받기 — 여기서 시간초과 나는 사람 진짜 많습니다

### 백준 (표준입력)

```python
import sys
input = sys.stdin.readline     # ★ 이 한 줄이 핵심
```

`input()`은 느립니다. 입력이 10만 줄이면 이것만으로 시간초과가 납니다.
`sys.stdin.readline`은 훨씬 빠르지만 **개행문자(`\n`)가 같이 딸려옵니다.**

- 숫자로 받을 땐 `int()`가 알아서 무시하니 상관없음
- 문자열로 받을 땐 **반드시 `.rstrip()`** 하세요

```python
import sys
input = sys.stdin.readline

n = int(input())                          # 정수 하나
a, b = map(int, input().split())          # 한 줄에 정수 둘
arr = list(map(int, input().split()))     # 한 줄에 정수 여러 개
s = input().rstrip()                      # 문자열 (개행 제거 필수!)

board = [list(map(int, input().split())) for _ in range(n)]   # n줄짜리 2차원 배열
grid = [input().rstrip() for _ in range(n)]                   # n줄짜리 문자열 격자
```

### 출력

```python
print(answer)
print(*arr)                      # 리스트를 공백으로 구분해 출력 → "1 2 3"
print('\n'.join(map(str, arr)))  # 줄바꿈으로 출력 (반복문 print보다 훨씬 빠름)
```

> **출력이 많으면 `print`를 반복 호출하지 마세요.** 결과를 리스트에 모았다가
> 마지막에 `'\n'.join()` 으로 한 번에 내보내는 게 수십 배 빠릅니다.

### 프로그래머스 (함수형)

입력을 직접 안 받습니다. 함수 인자로 들어옵니다.

```python
def solution(arr, k):
    answer = 0
    # ...
    return answer
```

`print()`로 출력하는 게 아니라 **`return`** 입니다. 헷갈리지 마세요.

## 3. 제출 전 체크리스트

- [ ] `input = sys.stdin.readline` 넣었나 (백준)
- [ ] 문자열 입력에 `.rstrip()` 했나
- [ ] 출력 형식이 문제와 정확히 같은가 (공백/줄바꿈/대소문자)
- [ ] 재귀를 쓴다면 `sys.setrecursionlimit(10**6)` 했나
- [ ] 디버깅용 `print` 다 지웠나

## 4. 자주 만나는 채점 결과

| 결과 | 뜻 | 보통 원인 |
|---|---|---|
| 맞았습니다!! | 통과 | 🎉 |
| 틀렸습니다 | 답이 다름 | 엣지 케이스(n=1, 빈 입력, 음수) 누락 |
| 시간 초과 | 너무 느림 | `input()` 그대로 씀 / 복잡도 잘못 잡음 |
| 메모리 초과 | 메모리 과다 | 불필요한 리스트 복사, 너무 큰 배열 |
| 런타임 에러 | 실행 중 죽음 | 인덱스 범위 초과, 0으로 나눔, **재귀 깊이 초과** |
| 출력 형식이 잘못되었습니다 | 형식 오류 | 공백/줄바꿈 차이 |

### 재귀 깊이 주의

Python 기본 재귀 한도는 **1000**입니다. DFS를 재귀로 짜면 금방 터집니다.

```python
import sys
sys.setrecursionlimit(10**6)
```

그래도 불안하면 **재귀 대신 스택(반복문)으로 DFS를 짜세요.**
(→ [docs/topics/05-bfs-dfs.md](topics/05-bfs-dfs.md))

## 5. 첫 제출 해보기

백준 [1000번 A+B](https://www.acmicpc.net/problem/1000):

```python
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
print(a + b)
```

이걸 제출해서 "맞았습니다!!"를 한 번 보고 나면 심리적 장벽이 사라집니다.
지금 하세요.

---

다음: [01. Python 치트시트](01-python-cheatsheet.md)
