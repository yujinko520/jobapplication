# 그리디 (탐욕법)

> **한 줄 요약**: "매 순간 최선"을 고르는 방법. **문제는 "그게 정말 최선인가"를 증명하는 것.**

## 1. 그리디란

지금 당장 제일 좋아 보이는 걸 고르고 뒤돌아보지 않습니다.

```python
# 거스름돈: 큰 동전부터
coins = [500, 100, 50, 10]
count = 0
for c in coins:
    count += money // c
    money %= c
```

이게 통하는 이유: 500원은 100원 5개로 정확히 나눠지기 때문(배수 관계).
**동전이 [500, 400, 100] 이면 그리디는 틀립니다.** (800원 → 그리디 500+100×3=4개, 최적 400×2=2개)

## 2. 그리디를 써도 되는지 판단하는 법

이게 그리디의 전부입니다. 코드는 쉽고 **판단이 어렵습니다.**

**실전 판단법 3가지:**

1. **작은 반례를 직접 만들어 보기** — 5분 안에 반례가 안 나오면 대개 맞습니다
2. **N이 아주 클 때** (10^5 이상) — DP나 완전탐색이 불가능하니 그리디일 확률이 높음
3. **"정렬하면 뭔가 보이는가"** — 그리디 문제의 절반은 정렬이 첫 단계

> 시험장에서 엄밀히 증명할 시간은 없습니다.
> **작은 예제 2~3개로 검증하고 제출**하는 게 현실적인 전략입니다.

## 3. 대표 패턴

### 패턴 A. 회의실 배정 (끝나는 시간 기준 정렬) ★ 최빈출

```python
# 최대한 많은 회의를 배정
meetings.sort(key=lambda x: (x[1], x[0]))    # ★ 끝나는 시간 기준!
count, end = 0, 0
for s, e in meetings:
    if s >= end:
        count += 1
        end = e
```

**시작 시간이 아니라 끝나는 시간 기준**입니다.
빨리 끝날수록 다음 회의를 넣을 여지가 많아지니까요.

### 패턴 B. 큰 것부터 / 작은 것부터

```python
# 가장 큰 수 만들기, 최소 비용 만들기 등
arr.sort(reverse=True)
```

"두 개를 합칠 때마다 비용 발생 → 총 비용 최소화" 같은 문제는 **작은 것부터 합칩니다** (힙 사용).

```python
from heapq import heappush, heappop, heapify
heapify(arr)
total = 0
while len(arr) > 1:
    a, b = heappop(arr), heappop(arr)
    total += a + b
    heappush(arr, a + b)
```

### 패턴 C. 배열 재배치로 최대/최소 만들기

```python
# 두 배열을 짝지어 곱의 합을 최소로
a.sort()
b.sort(reverse=True)
result = sum(x * y for x, y in zip(a, b))
```

작은 것 ↔ 큰 것을 짝지으면 합이 최소가 됩니다 (재배열 부등식).

### 패턴 D. 뒤에서부터 생각하기

앞에서 보면 안 보이는데 뒤에서 보면 명확해지는 문제가 많습니다.
(예: "마지막에 남는 것", "역순으로 되돌리기")

## 4. 그리디 vs DP 구분

| | 그리디 | DP |
|---|---|---|
| 판단 | 지금 최선을 고르면 전체 최선 | 지금 선택이 미래에 영향, 다 따져봐야 함 |
| N 크기 | 매우 큼 (10^5~) | 보통 (10^3~10^4) |
| 반례 | 없음 | 그리디로는 반례 존재 |
| 복잡도 | O(n log n) 정도 | O(n²), O(nk) 등 |

**헷갈리면**: 반례를 만들어 보세요. 반례가 있으면 DP, 없으면 그리디.

## 추천 문제 (프로그래머스)

| 문제 | 레벨 | 포인트 |
|---|---|---|
| [체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862) | Lv.1 | 그리디 입문 ★ |
| [큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883) | Lv.2 | 그리디 + 스택 ★★ |
| [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885) | Lv.2 | 정렬 후 양끝 ★ |
| [조이스틱](https://school.programmers.co.kr/learn/courses/30/lessons/42860) | Lv.2 | 반례가 많은 그리디 (주의) |
| [섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861) | Lv.3 | 크루스칼 MST |
| [단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884) | Lv.3 | 구간 끝점 정렬 ★★ |

> **단속카메라**가 예전 "회의실 배정"과 같은 골격입니다.
> **끝나는 지점 기준 정렬** — 이 한 줄이 이 유형의 90%예요.
>
> **조이스틱**은 그리디 반례를 체험하는 용도입니다. 틀려도 괜찮으니 꼭 한 번 부딪혀 보세요.
