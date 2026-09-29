# 정렬

> **한 줄 요약**: 정렬 알고리즘을 구현할 일은 거의 없다. **`key`를 잘 쓰는 게 전부다.**

퀵정렬/병합정렬을 직접 구현하는 문제는 코테에 잘 안 나옵니다.
(원리는 면접 대비로 알아두되, 실전에선 `sort()`를 씁니다)

## 기본

```python
arr.sort()                  # 제자리, 원본 변경, 반환값 None ★
new = sorted(arr)           # 새 리스트 반환 (원본 유지)
arr.sort(reverse=True)      # 내림차순
```

⚠️ `arr = arr.sort()` 는 `None`이 됩니다. 정말 자주 하는 실수예요.

## key — 핵심

```python
# 튜플/리스트의 특정 원소 기준
people.sort(key=lambda x: x[1])

# 다중 조건 ★★★ 제일 중요
# 점수 내림차순, 점수 같으면 이름 오름차순
people.sort(key=lambda x: (-x[1], x[0]))

# 문자열 길이순, 같으면 사전순
words.sort(key=lambda w: (len(w), w))

# dict를 값 기준으로 정렬
sorted(d.items(), key=lambda x: -x[1])
```

**숫자는 `-`를 붙여 내림차순, 문자열은 `-`를 못 붙임** → 문자열 내림차순이 섞이면
`reverse=True`로 한 번 정렬하고 다시 정렬하거나, 문자열을 뒤집는 트릭을 씁니다.
(Python의 `sort`는 **안정 정렬(stable)** 이라서 2단계 정렬이 가능합니다)

```python
# 이름 오름차순 + 점수 내림차순 (안정 정렬 활용)
people.sort(key=lambda x: x[0])              # 먼저 2순위 기준
people.sort(key=lambda x: x[1], reverse=True)  # 그 다음 1순위 기준
```

## 자주 나오는 정렬 응용

### 좌표 정렬
```python
points.sort(key=lambda p: (p[0], p[1]))   # x 오름차순, 같으면 y 오름차순
```

### 계수 정렬 (값의 범위가 작을 때, O(N))
```python
# 값의 범위는 좁은데 개수가 수백만인 경우
cnt = [0] * 10001
for x in nums:
    cnt[x] += 1
for v in range(10001):
    for _ in range(cnt[v]):
        print(v)
```
`sort()`가 효율성 테스트를 못 넘길 만큼 입력이 크면 이걸 씁니다. (실전 빈도는 낮음)

### 좌표 압축
값 자체가 아니라 **순위**만 필요할 때.
```python
sorted_unique = sorted(set(arr))
rank = {v: i for i, v in enumerate(sorted_unique)}
compressed = [rank[x] for x in arr]
```

## 알고리즘별 복잡도 (면접용)

| 알고리즘 | 평균 | 최악 | 안정성 |
|---|---|---|---|
| 버블/선택/삽입 | O(n²) | O(n²) | 삽입·버블만 안정 |
| 병합 정렬 | O(n log n) | O(n log n) | 안정 |
| 퀵 정렬 | O(n log n) | **O(n²)** | 불안정 |
| 힙 정렬 | O(n log n) | O(n log n) | 불안정 |
| Python `sort` (Timsort) | O(n log n) | O(n log n) | **안정** |

> 실행 가능한 코드: [`algo/sorting_hash.py`](../../algo/sorting_hash.py)

## 추천 문제 (프로그래머스)

| 문제 | 레벨 | 포인트 |
|---|---|---|
| [K번째수](https://school.programmers.co.kr/learn/courses/30/lessons/42748) | Lv.1 | 슬라이싱 + 정렬 기본 ★ |
| [문자열 내 마음대로 정렬하기](https://school.programmers.co.kr/learn/courses/30/lessons/12915) | Lv.1 | key 튜플 입문 ★ |
| [H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747) | Lv.2 | 정렬 후 관찰 |
| [가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746) | Lv.2 | 커스텀 key의 정수 ★★ |
| [전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577) | Lv.2 | 정렬하면 접두사가 이웃이 됨 |
| [메뉴 리뉴얼](https://school.programmers.co.kr/learn/courses/30/lessons/72411) | Lv.2 | 정렬 + 조합 (도전) |

> **가장 큰 수**가 이 유형의 핵심입니다. `key=lambda x: x*3` 이 왜 되는지 이해하면
> "정렬 기준을 만들어내는" 감각이 생깁니다. 30분 고민 후 풀이를 보세요.
