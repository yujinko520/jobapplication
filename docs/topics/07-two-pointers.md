# 투 포인터 / 슬라이딩 윈도우 / 누적합

> **한 줄 요약**: O(n²) 이중 반복문을 O(n)으로 줄이는 세 가지 도구.

"연속된 구간"이라는 말이 나오면 이 셋 중 하나입니다.

## 1. 투 포인터

포인터 두 개를 움직여서 구간을 관리합니다.

### 유형 A. 양 끝에서 좁혀오기 (정렬된 배열)

```python
# 합이 target인 두 수 찾기 (arr는 정렬됨)
lo, hi = 0, len(arr) - 1
while lo < hi:
    s = arr[lo] + arr[hi]
    if s == target:
        return (lo, hi)
    elif s < target:
        lo += 1        # 합을 키우려면 왼쪽을 오른쪽으로
    else:
        hi -= 1        # 합을 줄이려면 오른쪽을 왼쪽으로
```

### 유형 B. 같은 방향 (구간 늘리고 줄이기)

```python
# 합이 정확히 target인 연속 부분수열의 개수 (양수 배열)
left = 0
total = 0
count = 0
for right in range(n):
    total += arr[right]
    while total > target:      # 초과하면 왼쪽을 줄임
        total -= arr[left]
        left += 1
    if total == target:
        count += 1
```

`right`는 앞으로만, `left`도 앞으로만 갑니다. 각각 최대 n번 → **O(n)**.

⚠️ 주의: 투 포인터는 보통 **원소가 모두 양수**여야 성립합니다.
음수가 섞이면 "왼쪽을 줄이면 합이 준다"가 깨져요. 그땐 누적합 + 해시를 씁니다.

## 2. 슬라이딩 윈도우 (크기가 고정된 구간)

```python
# 길이 k인 연속 구간의 최대 합
window = sum(arr[:k])
best = window
for i in range(k, n):
    window += arr[i] - arr[i - k]    # 하나 넣고 하나 빼기 ★
    best = max(best, window)
```

매번 `sum(arr[i:i+k])`을 부르면 O(nk)입니다.
**"들어온 것 더하고 나간 것 빼기"** 로 O(n)이 됩니다.

## 3. 누적합 (Prefix Sum)

구간 합을 **여러 번** 물어볼 때 씁니다.

```python
# prefix[i] = arr[0] + ... + arr[i-1]
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

# 구간 [l, r] 의 합 (0-indexed, r 포함)
total = prefix[r + 1] - prefix[l]
```

전처리 O(n), 질의당 **O(1)**. 질의가 10만 개여도 끄떡없습니다.

### 2차원 누적합

```python
# S[i][j] = (0,0) ~ (i-1, j-1) 직사각형의 합
S = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        S[i+1][j+1] = board[i][j] + S[i][j+1] + S[i+1][j] - S[i][j]

# (x1,y1) ~ (x2,y2) 직사각형 합
area = S[x2+1][y2+1] - S[x1][y2+1] - S[x2+1][y1] + S[x1][y1]
```

포함-배제 원리입니다. 그림을 한 번 그려보면 바로 이해됩니다.

## 4. 어떤 걸 쓸지

| 문제 표현 | 도구 |
|---|---|
| "합이 S 이상인 **가장 짧은** 연속 구간" | 투 포인터 (유형 B) |
| "길이 K인 구간 중 최대/최소" | 슬라이딩 윈도우 |
| "구간 합을 M번 질의" | 누적합 |
| "정렬된 배열에서 두 수의 합" | 투 포인터 (유형 A) |
| "합이 K인 부분배열 개수 (음수 포함)" | 누적합 + 해시 |

→ 실행 코드: [`algo/two_pointers.py`](../../algo/two_pointers.py)

## 추천 문제 (프로그래머스)

| 문제 | 레벨 | 포인트 |
|---|---|---|
| [연속 부분 수열 합의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/131701) | Lv.2 | 원형 배열 + 투포인터 ★ |
| [숫자 카드 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/135807) | Lv.2 | 수학 + 탐색 |
| [보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258) | Lv.3 | 슬라이딩 윈도우 최단 구간 ★★ |
| [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885) | Lv.2 | 정렬 + 양끝 포인터 ★ |

> **보석 쇼핑**이 이 유형의 대표입니다. "모든 종류를 포함하는 최단 구간" —
> 창을 늘렸다 줄이는 골격을 여기서 익히면 됩니다.
>
> 누적합은 프로그래머스 단독 출제가 드물지만, **다른 문제 안에서 부품으로** 자주 쓰입니다.
> 개념만 알고 넘어가세요.
