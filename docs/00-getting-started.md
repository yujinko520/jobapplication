# 00. 시작하기 — 프로그래머스 적응

> **2026년 4월 28일, 백준(BOJ)이 서비스를 종료했습니다.**
> 국내 코딩테스트 준비는 이제 **프로그래머스 단일 플랫폼**으로 수렴했습니다.
> 오히려 잘된 면이 있어요 — 네이버·카카오·라인이 **실제 시험에 쓰는 플랫폼이 프로그래머스**라,
> 연습 환경이 곧 실전 환경입니다.

## 1. 계정 만들기

[school.programmers.co.kr](https://school.programmers.co.kr/) 가입 → **코딩테스트 연습** 메뉴로.

주요 메뉴 두 개만 기억하면 됩니다.

| 메뉴 | 용도 |
|---|---|
| [고득점 Kit](https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | **유형별로 묶인 문제집. 이 커리큘럼의 척추** |
| [코딩테스트 연습](https://school.programmers.co.kr/learn/challenges) | 레벨·태그 필터로 문제 찾기 |

## 2. 환경 준비

로컬 환경은 최소한만. 실제 시험은 웹 IDE에서 봅니다.

- Python 3.x
- 에디터: VS Code (Python 확장)
- **표준 라이브러리만 씁니다.** numpy, pandas는 못 쓴다고 가정하세요

실전에서 쓸 수 있는 import는 이 정도가 전부입니다:

```python
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from itertools import permutations, combinations, product
from functools import lru_cache
import math, bisect, sys
```

## 3. 프로그래머스 문제 형식 ★ 이게 전부입니다

**입력을 읽지 않고, 출력하지 않습니다.**

```python
def solution(numbers, target):
    answer = 0
    # 여기를 채웁니다
    return answer          # ★ print가 아니라 return!
```

- 입력은 **함수 인자**로 들어옵니다
- 답은 **`return`** 합니다
- `input()`, `sys.stdin`, `print()` 는 쓸 일이 없습니다

### 반환 타입을 정확히 맞추세요

문제의 "return 형식"을 반드시 확인하세요. 여기서 틀리는 사람이 많습니다.

```python
return 3                    # 정수
return [1, 2, 3]            # 리스트 (튜플 X)
return "hello"              # 문자열
return [[1,2], [3,4]]       # 2차원 리스트
```

`sorted()`가 반환하는 리스트, `list(set(...))` 등은 괜찮지만
**튜플을 반환하면 틀립니다.** `list()`로 감싸세요.

### print는 디버깅용으로만

`print()`를 써도 채점에는 영향이 없지만(반환값으로만 채점), **제출 전에 지우세요.**
출력이 많으면 실행 시간이 늘어 시간초과가 날 수 있습니다.

## 4. 채점 결과 읽는 법

| 결과 | 뜻 | 보통 원인 |
|---|---|---|
| 통과 ✅ | 정답 | 🎉 |
| 실패 ❌ | 답이 다름 | 엣지 케이스 누락 (빈 배열, 원소 1개, 전부 같은 값) |
| **시간 초과** | 너무 느림 | 복잡도 잘못 잡음 / 리스트에 `in` / `pop(0)` |
| 런타임 에러 | 실행 중 죽음 | 인덱스 초과, 0으로 나눔, **재귀 깊이 초과** |

### 정확성 테스트 vs 효율성 테스트

프로그래머스 특유의 채점 구조입니다.

- **정확성 테스트**: 작은 입력. 답만 맞으면 통과
- **효율성 테스트**: 큰 입력. **복잡도가 맞아야 통과**

> 정확성은 다 통과인데 효율성만 실패 = **알고리즘은 맞는데 너무 느리다**는 뜻입니다.
> 완전탐색으로 짰다면 정렬/해시/이분탐색으로 바꿔야 합니다. → [docs/02](02-complexity.md)

효율성 테스트가 있는 문제는 **부분 점수를 주므로**, 최적해를 몰라도 일단 제출하세요.

### 재귀 깊이 주의

Python 기본 재귀 한도는 **1000**입니다. DFS를 재귀로 짜면 금방 터집니다.

```python
import sys
sys.setrecursionlimit(10 ** 6)
```

프로그래머스에서도 이 한 줄은 쓸 수 있습니다. 불안하면 **스택(반복문) DFS**를 쓰세요.
→ [topics/05](topics/05-bfs-dfs.md)

## 5. 제출 전 체크리스트

- [ ] `return` 했나 (`print` 아님)
- [ ] 반환 타입이 문제 요구와 같나 (리스트? 정수? 문자열?)
- [ ] 엣지 케이스: 원소 1개 / 빈 입력 / 전부 같은 값 / 최댓값
- [ ] 디버깅용 `print` 지웠나
- [ ] 재귀를 쓴다면 `setrecursionlimit` 했나

## 6. 첫 문제 풀어보기

[두 개 뽑아서 더하기 (Lv.1)](https://school.programmers.co.kr/learn/courses/30/lessons/68644)

```python
def solution(numbers):
    answer = set()
    # numbers에서 서로 다른 두 개를 골라 합을 모으고
    # 오름차순 리스트로 반환
    return answer
```

힌트: `combinations`를 쓰면 두 줄입니다. `set`은 마지막에 `sorted()`로 리스트를 만드세요.

---

## 부록. 표준입력형 (삼성 SWEA 등)

지원처가 **삼성(SW Expert Academy)** 이거나 자체 플랫폼이면 아직 표준입력형입니다.
25일 플랜에서는 다루지 않지만, 필요해지면 이것만 알면 됩니다.

```python
import sys
input = sys.stdin.readline          # 입력이 많으면 필수 (속도)

n = int(input())
a, b = map(int, input().split())
arr = list(map(int, input().split()))
s = input().rstrip()                # 문자열은 개행 제거 필수
board = [list(map(int, input().split())) for _ in range(n)]

print(answer)
print(*arr)                         # "1 2 3"
print('\n'.join(map(str, arr)))     # 반복 print보다 훨씬 빠름
```

알고리즘 자체는 **완전히 동일합니다.** 입출력 껍데기만 다릅니다.

---

다음: [01. Python 치트시트](01-python-cheatsheet.md)
