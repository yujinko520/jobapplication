# 코딩테스트 대비 — 학습자 프로필 & 지도 지침

## 학습자 정보

- **시험일: 2026년 10월 24일 (토)** — 실제 학습 시작일 **2026-09-29**, 총 **25일**
- 학습 시간: **하루 2시간 확보 약속** (총 50시간). 이 예산에 맞춰 커리큘럼이 짜여 있음
- 언어: **Python 3** (문법은 다뤄봤음 / 기본 문법 강의는 불필요)
- **알고리즘은 노베이스** — 자료구조·복잡도·정형 풀이 패턴 전부 처음
- 목표: 국내 기업 코딩테스트 통과 — **프로그래머스 Lv.2 안정권 + Lv.3 일부**

### 학습자 선호 (본인이 직접 정한 것 — 존중할 것)

- **신규 문제를 먼저 풀고, 복습은 그 다음에 한다.** (2026-09-29 합의)
  → 문제를 낼 때 **신규 3문제부터** 제시한다. 복습을 앞세우지 않는다.
- 하루 **5문제**를 채운다. 2시간을 넘겨도 개수를 지킨다.
- 복습은 **같은 유형의 처음 보는 문제**로. 똑같은 문제를 다시 시키지 않는다.
- **플랫폼: 프로그래머스 단일** (백준은 2026-04-28 서비스 종료). 모든 문제는 프로그래머스 링크로 낸다

---

## 🧑‍🏫 Claude에게: 이 레포에서의 역할

이 레포에서 너는 **코딩테스트 과외 선생님**이다. 아래 규칙을 지킬 것.

### 기본 태도
1. **답을 먼저 주지 않는다.** 문제를 내고, 학습자가 시도한 뒤에 피드백한다.
   막혔다고 하면 **완성 코드가 아니라 힌트를 단계적으로** 준다 (힌트1 → 힌트2 → 그래도 막히면 풀이).
2. **"왜 이 알고리즘인가"를 항상 먼저 설명한다.** 코드보다 판단 근거가 중요하다.
   (제한 조건 N → 허용 복잡도 → 알고리즘 후보)
3. 학습자가 제출한 코드는 **정답 여부만 말하지 말고**, 시간복잡도·엣지케이스·
   더 파이썬다운 표현까지 같이 지적한다.
4. 노베이스이므로 **용어를 처음 쓸 때 반드시 풀어서 설명**한다.
5. 한국어로 대화한다.

### 세션 시작 시
1. 오늘 날짜를 확인하고 **D-day와 현재 단계**를 알려준다.
2. `docs/04-review-log.md`의 「복습 큐」를 확인해 **오늘의 복습 2문제를 미리 정해 둔다**
   (학습자에게는 신규가 끝난 뒤에 제시한다).
3. 커리큘럼의 **신규 3문제를 먼저** 제시한다. ← 학습자 선호
4. 신규가 끝나면 복습 2문제를 낸다.

> ❗ 복습은 **반드시 같은 날 안에** 끝낸다. 신규를 먼저 하는 대신,
> 신규 3문제가 끝나면 **지쳤더라도 복습 2문제를 반드시 제시한다.**
> "오늘은 여기까지 할까요?"라고 묻지 말고 복습 문제를 내라.
> 학습자가 직접 중단을 요청하면 그 사실을 복습 큐에 **이월**로 기록한다.

### 문제를 낼 때
- **하루 5문제 = 복습 2 + 신규 3.** 복습은 §4 풀에서 **지난 유형의 처음 보는 문제**로 고른다
  (똑같은 문제를 다시 시키지 않는다 — 응용이 되는지를 봐야 한다).
- 한 번에 전부 던지지 말고 **신규 3문제 먼저 → 끝나면 복습 2문제** 순서로 낸다 (학습자 선호).
- 항상 **백준/프로그래머스 실제 문제 링크**로 낸다. 가짜 문제를 지어내지 않는다.
- 난이도 순서대로: 쉬운 것 → 그날의 핵심 문제 → 살짝 어려운 것.

### 피드백할 때
- 잘한 부분을 먼저 구체적으로 짚는다 (막연한 칭찬 X).
- 틀렸으면 **어디서부터 틀렸는지**를 짚되, 고친 코드를 바로 주지 말고
  "여기서 n=1이면 어떻게 될까?" 처럼 스스로 찾게 유도한다.
- 같은 실수가 2번 반복되면 `docs/04-review-log.md`에 기록하도록 시킨다.

### 절대 하지 말 것
- ❌ 학습자가 시도하기 전에 완성 풀이 제공
- ❌ 남은 기간에 못 끝낼 분량을 던지기
- ❌ 세그먼트 트리, 네트워크 플로우 등 **시험 범위 밖 주제**로 시간 뺏기

---

## 1. 코딩테스트는 어떻게 나오는가

### 출제 형식 — 이제 사실상 하나

백준 종료 이후 국내 코테 연습·실전은 **프로그래머스 형식**으로 수렴했습니다.

```python
def solution(numbers, target):
    answer = 0
    # ...
    return answer        # ★ print가 아니라 return
```

- 입력을 직접 읽지 않는다. **함수 인자로 들어온다**
- 출력하지 않는다. **`return` 한다**
- `sys.stdin.readline` 같은 건 쓸 일이 없다

> **예외**: 삼성(SW Expert Academy)과 일부 자체 플랫폼은 여전히 표준입력형입니다.
> 지원처가 그쪽이면 [docs/00 부록](docs/00-getting-started.md)의 표준입력 템플릿만 훑으면 됩니다.
> 25일 플랜에서는 **프로그래머스형에만 집중**합니다.

### 난이도 기준 (프로그래머스)

| 레벨 | 수준 | 목표 |
|---|---|---|
| Lv.0 | 문법 연습 | 건너뜀 (Python 다뤄봤으므로) |
| Lv.1 | 기초 구현·해시 | **1주 안에 막힘없이** |
| **Lv.2** | 코테 주력 구간 | **여기가 합격선. 대부분의 시간을 여기에** |
| Lv.3 | 변별력 문제 | BFS/DFS·DP 쪽만 선별 도전 |
| Lv.4~5 | 버린다 | ❌ |

**"Lv.2를 40분 안에 혼자 푼다" = 통과권**입니다.

### 프로그래머스에서 문제 찾는 법

- **[고득점 Kit](https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit)** ← 유형별로 정리돼 있어 이 커리큘럼의 척추입니다
  (해시 / 스택·큐 / 힙 / 정렬 / 완전탐색 / 탐욕법 / DP / **DFS·BFS** / 이분탐색 / 그래프)
- [코딩테스트 연습](https://school.programmers.co.kr/learn/challenges) — 레벨·유형 필터
- 기업 기출은 "카카오 블라인드" 태그로 찾으면 실전 감각에 좋습니다

### 시험 스펙 (전형적)
- 문제 수 **3~5문제**, 시간 **2~3시간**
- 난이도 분포: 쉬움 1 + 중간 2 + 어려움 1~2
- **쉬움+중간 2개 = 3문제를 정확히 풀면 대부분 통과**
- 어려운 1문제는 대부분의 지원자가 못 풉니다. 여기 매달리면 떨어집니다

### 유형별 출제 비중 (국내 기업 기준 체감)

| 유형 | 비중 | 우선순위 |
|---|---|---|
| **BFS / DFS (그래프 탐색)** | ★★★★★ | 1순위. 안 나오는 시험이 드묾 |
| **구현 / 시뮬레이션** | ★★★★★ | 1순위. 알고리즘보다 꼼꼼함 |
| **해시(dict/set) / 정렬** | ★★★★ | 2순위. 배우기 쉽고 자주 나옴 |
| **DP** | ★★★★ | 2순위. 유형 6개만 |
| **이분탐색(파라메트릭)** | ★★★ | 3순위 |
| **투포인터 / 누적합** | ★★★ | 3순위 |
| **그리디** | ★★★ | 3순위 |
| **스택 / 큐 / 힙** | ★★★ | 3순위 |
| **다익스트라** | ★★ | 4순위 |
| 유니온파인드 / 위상정렬 | ★ | 여유 되면 |
| 세그먼트트리, 플로우, 기하 | ☆ | **버린다** |

> **BFS/DFS + 구현 + 해시/정렬 = 출제의 60% 이상.** 시간이 없으면 여기에 다 쏟으세요.

### 채점 방식
- 대부분 **테스트케이스별 부분 점수**가 있습니다
- 최적해를 몰라도 **완전탐색이라도 제출**하면 점수가 나옵니다
- 빈칸 제출이 최악입니다

---

## 2. 25일 커리큘럼 (9/29 시작 → 10/24 시험)

> **하루 5문제 = 복습 2 + 신규 3.** 아래는 **신규 3문제**만 적혀 있다.
> 복습 2문제는 **§4 유형별 복습 문제 풀**에서 그날 해당 유형의 안 푼 문제로 고른다.

| 단계 | 기간 | 일수 | 주제 |
|---|---|---|---|
| 1단계 | 9/29(화) ~ 10/2(금) | 4일 | 구현 + 완전탐색 + 시간복잡도 |
| 2단계 | 10/3(토) ~ 10/6(화) | 4일 | 정렬 + 해시 + 스택/큐/힙 |
| **3단계** | **10/7(수) ~ 10/14(수)** | **8일** | **BFS / DFS ★ 전체의 1/3** |
| 4단계 | 10/15(목) ~ 10/18(일) | 4일 | 이분탐색 + 투포인터 + 그리디 |
| 5단계 | 10/19(월) ~ 10/22(목) | 4일 | DP + 최단경로 |
| 6단계 | 10/23(금) | 1일 | 실전 모의고사 + 오답 복습 |
| — | **10/24(토)** | — | **시험** |

---

### 1단계 (9/29 ~ 10/2) — 구현·완전탐색

| 날짜 | 주제 | 신규 3문제 |
|---|---|---|
| ~~9/29 화~~ ✅ | 형식 적응 + 복잡도 | ~~두 개 뽑아서 더하기 / 모의고사 / 최소직사각형~~ **완료** |
| 9/30 수 | 시뮬레이션 (꼼꼼함) | [덧칠하기](https://school.programmers.co.kr/learn/courses/30/lessons/161989) Lv1 · [키패드 누르기](https://school.programmers.co.kr/learn/courses/30/lessons/67256) Lv1★ · [공원 산책](https://school.programmers.co.kr/learn/courses/30/lessons/172928) Lv1 |
| 10/1 목 | itertools 완전탐색 | [카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842) Lv2 · [소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839) Lv2★ · [할인 행사](https://school.programmers.co.kr/learn/courses/30/lessons/131127) Lv2 |
| 10/2 금 | 백트래킹 | [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) Lv2★ · [전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971) Lv2 · [행렬 테두리 회전하기](https://school.programmers.co.kr/learn/courses/30/lessons/77485) Lv2 |

문서: [docs/01](docs/01-python-cheatsheet.md), [docs/02](docs/02-complexity.md), [topics/01](docs/topics/01-implementation.md)
**통과 기준**: 제한 조건부터 확인하는 습관 + Lv.1을 20분 안에.

---

### 2단계 (10/3 ~ 10/6) — 정렬·해시·스택/큐/힙

| 날짜 | 주제 | 신규 3문제 |
|---|---|---|
| 10/3 토 | 정렬 `key` | [K번째수](https://school.programmers.co.kr/learn/courses/30/lessons/42748) Lv1 · [문자열 내 마음대로 정렬하기](https://school.programmers.co.kr/learn/courses/30/lessons/12915) Lv1 · [가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746) Lv2★ |
| 10/4 일 | 해시 | [완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576) Lv1★ · [폰켓몬](https://school.programmers.co.kr/learn/courses/30/lessons/1845) Lv1 · [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578) Lv2★ |
| 10/5 월 | 스택 / 큐 | [같은 숫자는 싫어](https://school.programmers.co.kr/learn/courses/30/lessons/12906) Lv1 · [올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909) Lv2★ · [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586) Lv2 |
| **10/6 화** | 힙 + **복습일** ★ | [더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626) Lv2★ **(신규 1개)** + **복습 4문제** |

문서: [topics/02](docs/topics/02-sorting.md), [topics/03](docs/topics/03-hash.md), [topics/04](docs/topics/04-stack-queue.md)
**통과 기준**: 리스트에 `in` 쓰다 막히면 set으로 바꾸는 반사신경.

---

### 3단계 (10/7 ~ 10/14) — **BFS / DFS 8일 ★★ 합격의 분기점**

| 날짜 | 주제 | 신규 3문제 |
|---|---|---|
| 10/7 수 | 그래프 표현 + BFS 템플릿 | [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) Lv3★ · [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) Lv2★ · [카카오프렌즈 컬러링북](https://school.programmers.co.kr/learn/courses/30/lessons/1829) Lv2 |
| 10/8 목 | DFS (재귀 + 스택) | [여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164) Lv3 · [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163) Lv3★ · [거리두기 확인하기](https://school.programmers.co.kr/learn/courses/30/lessons/81302) Lv2 |
| 10/9 금 | 격자 덩어리 세기 | [무인도 여행](https://school.programmers.co.kr/learn/courses/30/lessons/154540) Lv2★ · [리코쳇 로봇](https://school.programmers.co.kr/learn/courses/30/lessons/169199) Lv2 · [퍼즐 조각 채우기](https://school.programmers.co.kr/learn/courses/30/lessons/84021) Lv3(도전) |
| **10/10 토** | **격자 BFS 최단거리** ★★ | [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) Lv2★★ · [미로 탈출](https://school.programmers.co.kr/learn/courses/30/lessons/159993) Lv2★ · [경주로 건설](https://school.programmers.co.kr/learn/courses/30/lessons/67259) Lv3(도전) |
| 10/11 일 | 상태 전이 BFS | [가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189) Lv3★ · [순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191) Lv3 · [아이템 줍기](https://school.programmers.co.kr/learn/courses/30/lessons/87694) Lv3 |
| 10/12 월 | 그래프 응용 | [배달](https://school.programmers.co.kr/learn/courses/30/lessons/12978) Lv2★ · [합승 택시 요금](https://school.programmers.co.kr/learn/courses/30/lessons/72413) Lv3(도전) · [섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861) Lv3 |
| 10/13 화 | 심화 / 미완 정리 | [양과 늑대](https://school.programmers.co.kr/learn/courses/30/lessons/92343) Lv3(도전) + **앞에서 못 끝낸 문제 2개** |
| **10/14 수** | **3단계 전체 복습일** ★★ | **신규 없음 · 복습 5문제** + BFS 템플릿 빈 화면에서 치기 |

문서: [topics/05](docs/topics/05-bfs-dfs.md) / 코드: `algo/bfs_dfs.py`

**이 단계 통과 기준**: 빈 화면에서 BFS 템플릿을 **아무것도 안 보고** 칠 수 있다.
**10/10의 게임 맵 최단거리**가 이 유형의 원형이다 — 3단계 내내 **최소 3번** 다시 볼 것.

---

### 4단계 (10/15 ~ 10/18) — 이분탐색·투포인터·그리디

| 날짜 | 주제 | 신규 3문제 |
|---|---|---|
| 10/15 목 | 이분탐색 + `bisect` | [예산](https://school.programmers.co.kr/learn/courses/30/lessons/12982) Lv1 · [순위 검색](https://school.programmers.co.kr/learn/courses/30/lessons/72412) Lv2 · [입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238) Lv3★★ |
| 10/16 금 | **파라메트릭 서치** | [징검다리 건너기](https://school.programmers.co.kr/learn/courses/30/lessons/64062) Lv3★ · [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885) Lv2★ · [징검다리](https://school.programmers.co.kr/learn/courses/30/lessons/43236) Lv4(도전) |
| 10/17 토 | 투포인터 / 슬라이딩 | [연속 부분 수열 합의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/131701) Lv2 · [숫자 카드 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/135807) Lv2 · [보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258) Lv3★ |
| **10/18 일** | 그리디 + **복습일** ★ | [체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862) Lv1★ · [큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883) Lv2★ **(신규 2개)** + **복습 3문제** |

문서: [topics/06](docs/topics/06-binary-search.md), [topics/07](docs/topics/07-two-pointers.md), [topics/08](docs/topics/08-greedy.md)

> **입국심사**는 파라메트릭 서치의 교과서다. 하루를 써도 아깝지 않다.

---

### 5단계 (10/19 ~ 10/22) — DP + 최단경로

| 날짜 | 주제 | 신규 3문제 |
|---|---|---|
| 10/19 월 | DP 유형1 (피보나치형) | [피보나치 수](https://school.programmers.co.kr/learn/courses/30/lessons/12945) Lv2 · [멀리 뛰기](https://school.programmers.co.kr/learn/courses/30/lessons/12914) Lv2 · [2 x n 타일링](https://school.programmers.co.kr/learn/courses/30/lessons/12900) Lv2★ |
| 10/20 화 | **DP 유형5 (2차원)** ★ | [땅따먹기](https://school.programmers.co.kr/learn/courses/30/lessons/12913) Lv2★★ · [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105) Lv3★★ · [등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898) Lv3★ |
| 10/21 수 | DP 심화 + 그리디 | [조이스틱](https://school.programmers.co.kr/learn/courses/30/lessons/42860) Lv2 · [단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884) Lv3★★ · [N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895) Lv3(도전) |
| **10/22 목** | **전 범위 복습일** ★ | **신규 없음 · 복습 5문제** (BFS 2 + DP 2 + 약한 유형 1) |

문서: [topics/09](docs/topics/09-dp.md), [topics/10](docs/topics/10-graph-advanced.md)

> **DP가 막히면 미련 없이 BFS/DFS 복습으로 전환한다.**
> 못 푸는 DP 1문제보다 확실히 푸는 BFS 1문제가 점수에 유리하다.

---

### 6단계 (10/23 금) — 실전 리허설

- **2시간 타이머**: 안 풀어본 **Lv.1 + Lv.2 + Lv.2(또는 Lv.3)** 3문제 연속.
  처음 5분은 전체 훑고 푸는 순서 정하기
- **저녁**: `docs/04-review-log.md`의 🔴 **반복 실수**만 정독 + [실전 전략](docs/03-exam-day.md)
- **새 알고리즘 공부 금지.** 일찍 잘 것

### 10/24 (토) — 시험 🎯

---

### 밀렸을 때 잘라내는 순서

1. (도전) 표시 문제 — 전부 생략 가능
2. 합승 택시 요금 / 양과 늑대 / N으로 표현
3. 그리디
4. 투포인터
5. DP 유형1 (2차원만 남김)

**절대 못 버리는 것**: 구현·완전탐색 / 정렬·해시 / **BFS·DFS** / **복습 2문제**

---

## 3. 복습 설계 — **유사 문제로 응용력 확인** ★ 커리큘럼의 절반

**25일 벼락치기의 최대 실패 요인은 "앞에서 푼 걸 시험날 까먹는 것"이다.**
그런데 **똑같은 문제를 다시 푸는 건 기억 테스트일 뿐 응용 테스트가 아니다.**
외운 코드를 재생하는 것과, 처음 보는 문제에서 그 유형을 알아보는 것은 전혀 다르다.

### 복습 = 같은 유형의 **처음 보는 문제**

| 주기 | 방식 |
|---|---|
| **D+3** | 그 유형의 **다른 문제** 1개 — 비슷한 난이도 |
| **D+7** | 그 유형의 **또 다른 문제** 1개 — 한 단계 위 난이도 |
| 유사 문제에서 막히면 | **그때** 원본 문제와 오답노트로 돌아간다 |

- **자력으로 푼 유형** → D+7에 유사 문제 1개
- **힌트/답을 보고 푼 유형** → D+3, D+7 둘 다 (유사 문제 2개)
- 유사 문제도 막히면 → 그 유형은 **아직 안 익은 것**. 문서 재독 + 1문제 추가

> 학습자가 "이거 아까 그거랑 똑같네"라고 **스스로 알아채면 성공**이다.
> 그게 시험장에서 필요한 유일한 능력이다.

### 복습 문제는 「유형별 복습 풀」에서 고른다

아래 **§4 유형별 복습 문제 풀**에 유형마다 문제가 쌓여 있다.
매일 복습 시간에는 **그날 해당하는 유형에서 아직 안 푼 문제 2개**를 고른다.

### 고정 복습일 (신규 문제 없이 복습만)

| 날짜 | 복습 범위 |
|---|---|
| **10/6 (화)** | 1·2단계 전체 — 구현·완전탐색·정렬·해시·스택큐 |
| **10/14 (수)** | **3단계 BFS/DFS 전체** ★ 가장 중요 |
| **10/18 (일)** | 4단계 + 3단계에서 막혔던 BFS 유형 |
| **10/22 (목)** | 5단계 + 전 범위 훑기 |
| **10/23 (금)** | 🔴 반복 실수 + 실전 모의고사 |

> 진도가 밀렸다는 이유로 복습일을 건너뛰지 않는다. 그게 제일 손해다.

### 복습 방법

❌ 코드를 읽으면서 "아 맞다" 하고 넘어가기 → 아무것도 안 남는다
✅ **빈 화면에서 새 문제를 처음부터 푼다.** 막히면 그때 노트를 본다

> **BFS 템플릿만은 예외**: 3단계(10/7~10/14) 내내 **매일 한 번씩 손으로 친다.**
> "보면 이해된다"와 "빈 화면에서 칠 수 있다"는 전혀 다른 상태다.

---

## 4. 유형별 복습 문제 풀

복습 시간에 여기서 **아직 안 푼 문제**를 골라 푼다. 위에서부터 난이도 순.

### 완전탐색 / 조합·순열
[삼총사](https://school.programmers.co.kr/learn/courses/30/lessons/131705)(Lv1) · [소수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12977)(Lv1) · [모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840)(Lv1) ·
[최소직사각형](https://school.programmers.co.kr/learn/courses/30/lessons/86491)(Lv1) · [카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842)(Lv2) · [소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839)(Lv2) ·
[피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946)(Lv2) · [할인 행사](https://school.programmers.co.kr/learn/courses/30/lessons/131127)(Lv2) · [전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971)(Lv2)

### 구현 / 시뮬레이션
[덧칠하기](https://school.programmers.co.kr/learn/courses/30/lessons/161989)(Lv1) · [공원 산책](https://school.programmers.co.kr/learn/courses/30/lessons/172928)(Lv1) · [바탕화면 정리](https://school.programmers.co.kr/learn/courses/30/lessons/161990)(Lv1) ·
[기사단원의 무기](https://school.programmers.co.kr/learn/courses/30/lessons/136798)(Lv1) · [3진법 뒤집기](https://school.programmers.co.kr/learn/courses/30/lessons/68935)(Lv1) · [옹알이(2)](https://school.programmers.co.kr/learn/courses/30/lessons/133499)(Lv1) ·
[카드 뭉치](https://school.programmers.co.kr/learn/courses/30/lessons/159994)(Lv1) · [키패드 누르기](https://school.programmers.co.kr/learn/courses/30/lessons/67256)(Lv1) · [둘만의 암호](https://school.programmers.co.kr/learn/courses/30/lessons/155652)(Lv1) ·
[대충 만든 자판](https://school.programmers.co.kr/learn/courses/30/lessons/160586)(Lv1) · [숫자 짝꿍](https://school.programmers.co.kr/learn/courses/30/lessons/131128)(Lv1) · [신규 아이디 추천](https://school.programmers.co.kr/learn/courses/30/lessons/72410)(Lv1) ·
[스킬트리](https://school.programmers.co.kr/learn/courses/30/lessons/49993)(Lv2) · [괄호 회전하기](https://school.programmers.co.kr/learn/courses/30/lessons/76502)(Lv2) · [행렬 테두리 회전하기](https://school.programmers.co.kr/learn/courses/30/lessons/77485)(Lv2)

### 정렬
[K번째수](https://school.programmers.co.kr/learn/courses/30/lessons/42748)(Lv1) · [문자열 내 마음대로 정렬하기](https://school.programmers.co.kr/learn/courses/30/lessons/12915)(Lv1) ·
[실패율](https://school.programmers.co.kr/learn/courses/30/lessons/42889)(Lv1) · [명예의 전당(1)](https://school.programmers.co.kr/learn/courses/30/lessons/138477)(Lv1) ·
[H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747)(Lv2) · [가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746)(Lv2) · [튜플](https://school.programmers.co.kr/learn/courses/30/lessons/64065)(Lv2)

### 해시 (dict / set / Counter)
[완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576)(Lv1) · [폰켓몬](https://school.programmers.co.kr/learn/courses/30/lessons/1845)(Lv1) · [추억 점수](https://school.programmers.co.kr/learn/courses/30/lessons/176963)(Lv1) ·
[전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577)(Lv2) · [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578)(Lv2) · [오픈채팅방](https://school.programmers.co.kr/learn/courses/30/lessons/42888)(Lv2) ·
[메뉴 리뉴얼](https://school.programmers.co.kr/learn/courses/30/lessons/72411)(Lv2) · [베스트앨범](https://school.programmers.co.kr/learn/courses/30/lessons/42579)(Lv3)

### 스택 / 큐 / 힙
[같은 숫자는 싫어](https://school.programmers.co.kr/learn/courses/30/lessons/12906)(Lv1) · [크레인 인형뽑기 게임](https://school.programmers.co.kr/learn/courses/30/lessons/64061)(Lv2) ·
[올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909)(Lv2) · [짝지어 제거하기](https://school.programmers.co.kr/learn/courses/30/lessons/12973)(Lv2) · [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586)(Lv2) ·
[프린터](https://school.programmers.co.kr/learn/courses/30/lessons/42587)(Lv2) · [다리를 지나는 트럭](https://school.programmers.co.kr/learn/courses/30/lessons/42583)(Lv2) · [주식가격](https://school.programmers.co.kr/learn/courses/30/lessons/42584)(Lv2) ·
[더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626)(Lv2) · [이중우선순위큐](https://school.programmers.co.kr/learn/courses/30/lessons/42628)(Lv3)

### BFS / DFS ★ 가장 많이 쌓아둘 것
[타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165)(Lv2) · [카카오프렌즈 컬러링북](https://school.programmers.co.kr/learn/courses/30/lessons/1829)(Lv2) ·
[무인도 여행](https://school.programmers.co.kr/learn/courses/30/lessons/154540)(Lv2) · [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844)(Lv2) ·
[미로 탈출](https://school.programmers.co.kr/learn/courses/30/lessons/159993)(Lv2) · [리코쳇 로봇](https://school.programmers.co.kr/learn/courses/30/lessons/169199)(Lv2) ·
[거리두기 확인하기](https://school.programmers.co.kr/learn/courses/30/lessons/81302)(Lv2) · [전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971)(Lv2) ·
[네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)(Lv3) · [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163)(Lv3) · [여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164)(Lv3) ·
[가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189)(Lv3) · [순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191)(Lv3) ·
[아이템 줍기](https://school.programmers.co.kr/learn/courses/30/lessons/87694)(Lv3) · [경주로 건설](https://school.programmers.co.kr/learn/courses/30/lessons/67259)(Lv3) ·
[퍼즐 조각 채우기](https://school.programmers.co.kr/learn/courses/30/lessons/84021)(Lv3) · [양과 늑대](https://school.programmers.co.kr/learn/courses/30/lessons/92343)(Lv3)

### 이분탐색 / 파라메트릭
[순위 검색](https://school.programmers.co.kr/learn/courses/30/lessons/72412)(Lv2) · [입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238)(Lv3) · [징검다리 건너기](https://school.programmers.co.kr/learn/courses/30/lessons/64062)(Lv3)

### 투포인터 / 슬라이딩 윈도우
[연속 부분 수열 합의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/131701)(Lv2) · [숫자 카드 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/135807)(Lv2) ·
[보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258)(Lv3)

### 그리디
[체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862)(Lv1) · [예산](https://school.programmers.co.kr/learn/courses/30/lessons/12982)(Lv1) · [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885)(Lv2) ·
[큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883)(Lv2) · [조이스틱](https://school.programmers.co.kr/learn/courses/30/lessons/42860)(Lv2) ·
[단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884)(Lv3) · [섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861)(Lv3)

### DP
[피보나치 수](https://school.programmers.co.kr/learn/courses/30/lessons/12945)(Lv2) · [멀리 뛰기](https://school.programmers.co.kr/learn/courses/30/lessons/12914)(Lv2) · [2 x n 타일링](https://school.programmers.co.kr/learn/courses/30/lessons/12900)(Lv2) ·
[땅따먹기](https://school.programmers.co.kr/learn/courses/30/lessons/12913)(Lv2) · [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105)(Lv3) · [등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898)(Lv3) ·
[N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895)(Lv3)

### 최단경로
[배달](https://school.programmers.co.kr/learn/courses/30/lessons/12978)(Lv2) · [가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189)(Lv3) · [합승 택시 요금](https://school.programmers.co.kr/learn/courses/30/lessons/72413)(Lv3)

> ⚠️ 링크가 404면 Claude에게 알릴 것 — 문제 ID를 바로 고친다.

---

## 5. 하루 루틴 — **하루 5문제 고정**

| 순서 | 할 일 |
|---|---|
| 1 | 오늘 유형 문서 훑기 (10분. 길게 읽지 말 것) |
| 2 | **신규 3문제** (**30분 룰** 적용) ← 학습자 선호: 신규 먼저 |
| 3 | **복습 2문제** — §4 풀에서 지난 유형의 **처음 보는 문제** ★ |
| 4 | `docs/04-review-log.md` 기록 |

**하루 5문제 = 신규 3 + 복습 2. 학습자 합의사항이다.**

- **2시간을 넘겨도 5문제를 채운다.** 시간이 아니라 **문제 수가 기준**이다
- 신규를 먼저 하되, **복습 2문제는 같은 날 안에 반드시 끝낸다.**
  머리가 맑을 때 새 유형을 배우고, 남은 힘으로 아는 유형을 확인하는 순서다
- 3단계 후반(Lv.3 BFS)은 3시간 이상 걸릴 수 있다. 그래도 5문제를 지킨다
- 단, **30분 룰은 유지**한다. 한 문제에 30분 넘으면 풀이를 보고 → 이해하고 → 다시 구현.
  막힌 채로 1시간을 버티는 건 5문제를 채우는 게 아니라 하루를 버리는 것이다

## 6. 문제 푸는 표준 절차 (항상 이 순서로)

1. **제한 조건(N)부터 본다** → 허용 복잡도 계산 → 알고리즘 후보 추리기
2. **입출력 예제를 손으로 따라간다** → 문제를 진짜 이해했는지 확인
3. **주석으로 설계를 먼저 쓴다** (코드 금지)
   ```python
   # 1. 그래프를 인접리스트로 만든다
   # 2. 1번 노드에서 BFS
   # 3. dist 배열의 최댓값 출력
   ```
4. **구현한다**
5. **제출 전 엣지케이스 체크**: n=1 / 전부 같은 값 / 음수 / 답이 없는 경우

> 3번(설계를 먼저 쓰기)을 건너뛰는 게 초보자 실패의 1순위 원인입니다.

---

## 7. N 보고 알고리즘 고르기 (외울 표)

| N | 허용 복잡도 | 알고리즘 |
|---|---|---|
| ≤ 10 | O(N!) | 순열 완전탐색 |
| ≤ 20 | O(2^N) | 부분집합, 비트마스크 |
| ≤ 100 | O(N³) | 3중 루프, 플로이드 |
| ≤ 1,000 | O(N²) | 2중 루프, 기본 DP |
| ≤ 100,000 | O(N log N) | **정렬, 이분탐색, 힙** |
| ≤ 1,000,000 | O(N) | 투포인터, 해시, BFS/DFS |
| ≥ 10,000,000 | O(log N) | 수학, 이분탐색 |

**N이 작으면 "다 해봐도 된다"는 힌트**입니다. 어려운 알고리즘을 찾지 마세요.

---

## 8. 시간이 없으니 버릴 것

한 달로는 전부 못 합니다. **아래는 과감히 버리세요.**

- ❌ 세그먼트 트리 / 펜윅 트리
- ❌ 네트워크 플로우
- ❌ 기하 알고리즘 (CCW, 볼록껍질)
- ❌ 문자열 알고리즘 (KMP, 트라이) — 여유 있으면 트라이만
- ❌ 벨만-포드, MST (크루스칼은 코드 짧으니 여유되면)
- ❌ 정렬 알고리즘 직접 구현 (면접용으로만 개념 알기)

대신 **BFS/DFS와 구현에 그 시간을 전부 쓰세요.** 점수 기대값이 훨씬 높습니다.

---

## 9. 레포 사용법

```bash
pytest -q                    # 템플릿 코드 검증 (전부 통과해야 정상)
python3 -m algo.graph        # 알고리즘 템플릿 실행해 보기
```

| 디렉토리 | 용도 |
|---|---|
| `docs/` | 유형별 학습 가이드 (읽는 순서대로 번호) |
| `algo/` | 검증된 알고리즘 템플릿 — **복붙 말고 보고 다시 치기** |
| `practice/` | 대표 문제 패턴 풀이 예제 |
| `tests/` | 위 코드들의 정답 검증 |
| `docs/04-review-log.md` | **오답노트 — 가장 중요** |

---

## 10. 진도 체크 (직접 갱신)

- [ ] 1단계 (~10/2): 입출력 + 복잡도 + 완전탐색
- [ ] 2단계 (~10/6): 정렬 + 해시 + 스택/큐
- [ ] 3단계 (~10/14): **BFS / DFS** ★★ 최우선
- [ ] 4단계 (~10/18): 이분탐색 + 투포인터 + 그리디
- [ ] 5단계 (~10/22): DP 유형 2개
- [ ] 6단계 (10/23): 모의고사 2시간 3문제
- [ ] 10/24 시험

**합격 신호**: 프로그래머스 **Lv.2를 아무 도움 없이 40분 안에** 풀 수 있으면 통과권입니다.
Lv.3 DFS/BFS까지 풀리면 상위권입니다.
