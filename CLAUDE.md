# 코딩테스트 대비 — 학습자 프로필 & 지도 지침

## 학습자 정보

- **시험일: 2026년 10월 24일 (토)** — 실제 학습 시작일 **2026-09-29**, 총 **25일**
- 학습 시간: **하루 2시간 확보 약속** (총 50시간). 이 예산에 맞춰 커리큘럼이 짜여 있음
- 언어: **Python 3** (문법은 다뤄봤음 / 기본 문법 강의는 불필요)
- **알고리즘은 노베이스** — 자료구조·복잡도·정형 풀이 패턴 전부 처음
- 목표: 국내 기업 코딩테스트 통과 — **프로그래머스 Lv.2 안정권 + Lv.3 일부**
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
- 오늘 날짜를 확인하고 **D-day와 현재 주차**를 먼저 알려준다.
- 아래 커리큘럼에서 **오늘 할 분량**을 제시한다.
- `docs/04-review-log.md`에 복습 대상이 있으면 그것부터 시킨다.

### 문제를 낼 때
- 한 번에 **2~3문제씩만** 낸다 (10개씩 내면 부담돼서 아무것도 안 함).
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

> 하루 2시간 × 25일 = **총 50시간**. 이건 "전 범위 학습"이 아니라 **점수 기대값 최적화** 플랜이다.
> 시간 예산이 빠듯하므로 **하루라도 밀리면 BFS/DFS가 아닌 쪽을 잘라낸다.**

### 단계별 시간 배분 (일수 = 그 유형의 중요도)

| 단계 | 기간 | 일수 | 주제 |
|---|---|---|---|
| 1단계 | 9/29(화) ~ 10/2(금) | 4일 | 입출력 + 시간복잡도 + 구현/완전탐색 |
| 2단계 | 10/3(토) ~ 10/6(화) | 4일 | 정렬 + 해시 + 스택/큐/힙 |
| **3단계** | **10/7(수) ~ 10/14(수)** | **8일** | **BFS / DFS ★ 전체의 1/3을 여기에** |
| 4단계 | 10/15(목) ~ 10/18(일) | 4일 | 이분탐색 + 투포인터/누적합 + 그리디 |
| 5단계 | 10/19(월) ~ 10/22(목) | 4일 | DP (유형 3개만) + 다익스트라(여유시) |
| 6단계 | 10/23(금) | 1일 | 실전 모의고사 + 오답 복습 |
| — | **10/24(토)** | — | **시험** |

---

### 1단계 (9/29 ~ 10/2) — 기반 4일

| 날짜 | 할 것 | 문서 |
|---|---|---|
| 9/29 화 | 프로그래머스 `solution()` 형식 적응 + **N 보고 알고리즘 고르는 표 암기** | [docs/00](docs/00-getting-started.md), [docs/02](docs/02-complexity.md) |
| 9/30 수 | 코테용 Python 문법 (deque/Counter/정렬 key) + 구현 | [docs/01](docs/01-python-cheatsheet.md), [topics/01](docs/topics/01-implementation.md) |
| 10/1 목 | 완전탐색 + itertools (순열/조합/중복순열) | [topics/01](docs/topics/01-implementation.md) |
| 10/2 금 | 백트래킹 (넣고→재귀→빼기) | [topics/01](docs/topics/01-implementation.md) |

**필수 문제 (8개)** — Lv.1 → Lv.2 순서대로:
[두 개 뽑아서 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/68644)(Lv1),
[최소직사각형](https://school.programmers.co.kr/learn/courses/30/lessons/86491)(Lv1),
[모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840)(Lv1)★,
[덧칠하기](https://school.programmers.co.kr/learn/courses/30/lessons/161989)(Lv1),
[키패드 누르기](https://school.programmers.co.kr/learn/courses/30/lessons/67256)(Lv1, 구현),
[카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842)(Lv2)★,
[소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839)(Lv2, 순열)★,
[피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946)(Lv2, 백트래킹)★

**이 단계 통과 기준**: 문제를 보면 제한 조건부터 확인하고, Lv.1을 20분 안에 푼다.

---

### 2단계 (10/3 ~ 10/6) — 자료구조 4일

프로그래머스 **고득점 Kit**의 해시 / 정렬 / 스택·큐 / 힙 파트를 그대로 따라갑니다.

| 날짜 | 할 것 | 문서 |
|---|---|---|
| 10/3 토 | 정렬 `key` (다중 조건) | [topics/02](docs/topics/02-sorting.md) |
| 10/4 일 | 해시 (dict/set/Counter/defaultdict) | [topics/03](docs/topics/03-hash.md) |
| 10/5 월 | 스택 + 큐(deque) | [topics/04](docs/topics/04-stack-queue.md) |
| 10/6 화 | 힙(heapq) | [topics/04](docs/topics/04-stack-queue.md) |

**필수 문제 (10개)**:
[완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576)(Lv1, 해시)★,
[K번째수](https://school.programmers.co.kr/learn/courses/30/lessons/42748)(Lv1, 정렬),
[같은 숫자는 싫어](https://school.programmers.co.kr/learn/courses/30/lessons/12906)(Lv1, 스택),
[전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577)(Lv2, 해시),
[의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578)(Lv2, 해시)★,
[가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746)(Lv2, 정렬 key)★,
[H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747)(Lv2, 정렬),
[올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909)(Lv2, 스택)★,
[기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586)(Lv2, 큐),
[더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626)(Lv2, 힙)★

**이 단계 통과 기준**: "리스트에서 `in` 쓰면 시간초과" → set으로 바꾸는 반사신경.

---

### 3단계 (10/7 ~ 10/14) — **BFS / DFS 8일 ★★ 여기가 합격의 전부**

전체 25일 중 8일을 여기 씁니다. 프로그래머스 Lv.2~Lv.3 변별력 문제의 핵심 축이고,
출제 비중이 압도적이라 **투자 대비 회수가 가장 큽니다.**

| 날짜 | 할 것 |
|---|---|
| 10/7 수 | 그래프 표현(인접리스트) + BFS 템플릿 **손으로 3번 쓰기** |
| 10/8 목 | DFS (재귀 + 스택 두 버전) |
| 10/9 금 | 격자 탐색 — 덩어리 세기 (연결 요소) |
| 10/10 토 | 격자 BFS — **최단거리** ★ 가장 중요한 하루 |
| 10/11 일 | 단계가 나뉜 BFS (중간 지점 경유) |
| 10/12 월 | 격자가 아닌 BFS (상태 전이·단어 변환형) |
| 10/13 화 | 상태를 하나 더 얹는 BFS (3차원 방문 배열) |
| 10/14 수 | **전체 복습** — 앞의 문제 중 막혔던 것 재구현 |

문서: [topics/05](docs/topics/05-bfs-dfs.md) / 코드: `algo/bfs_dfs.py`

**필수 문제 (12개 + 도전 2개, 하루 2개꼴)**:
[타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165)(Lv2, DFS)★,
[카카오프렌즈 컬러링북](https://school.programmers.co.kr/learn/courses/30/lessons/1829)(Lv2, 덩어리),
[무인도 여행](https://school.programmers.co.kr/learn/courses/30/lessons/154540)(Lv2, 덩어리)★,
[게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844)(Lv2, 격자 최단거리)★★,
[미로 탈출](https://school.programmers.co.kr/learn/courses/30/lessons/159993)(Lv2, 단계 BFS)★,
[리코쳇 로봇](https://school.programmers.co.kr/learn/courses/30/lessons/169199)(Lv2, BFS 변형),
[전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971)(Lv2, 탐색),
[네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)(Lv3, 연결 요소)★,
[단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163)(Lv3, 상태 BFS)★,
[여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164)(Lv3, DFS+백트래킹),
[가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189)(Lv3, BFS)★,
[순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191)(Lv3, 그래프)

도전(여유 있을 때만): [경주로 건설](https://school.programmers.co.kr/learn/courses/30/lessons/67259)(Lv3), [아이템 줍기](https://school.programmers.co.kr/learn/courses/30/lessons/87694)(Lv3)

**이 단계 통과 기준**: 빈 화면에서 BFS 템플릿을 **아무것도 안 보고** 칠 수 있다.
여기까지 왔으면 시험은 이미 절반 이상 잡은 겁니다.

---

### 4단계 (10/15 ~ 10/18) — 탐색 최적화 + 그리디 4일

| 날짜 | 할 것 | 문서 |
|---|---|---|
| 10/15 목 | 이분탐색 기본 + `bisect` | [topics/06](docs/topics/06-binary-search.md) |
| 10/16 금 | **파라메트릭 서치** ("최댓값의 최솟값") | [topics/06](docs/topics/06-binary-search.md) |
| 10/17 토 | 투포인터 + 슬라이딩 윈도우 | [topics/07](docs/topics/07-two-pointers.md) |
| 10/18 일 | 그리디 | [topics/08](docs/topics/08-greedy.md) |

**필수 문제 (10개)**:
[체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862)(Lv1, 그리디)★,
[큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883)(Lv2, 그리디+스택)★,
[구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885)(Lv2, 정렬+투포인터)★,
[조이스틱](https://school.programmers.co.kr/learn/courses/30/lessons/42860)(Lv2, 그리디),
[연속 부분 수열 합의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/131701)(Lv2, 투포인터),
[순위 검색](https://school.programmers.co.kr/learn/courses/30/lessons/72412)(Lv2, 이분탐색+해시),
[단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884)(Lv3, 구간 그리디)★★,
[보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258)(Lv3, 슬라이딩 윈도우)★,
[입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238)(Lv3, 파라메트릭)★★,
[징검다리 건너기](https://school.programmers.co.kr/learn/courses/30/lessons/64062)(Lv3, 파라메트릭)★

> **단속카메라**는 예전 "회의실 배정"과 같은 골격(끝나는 지점 기준 정렬)입니다.
> **입국심사**는 파라메트릭 서치의 교과서예요. 이 둘은 꼭 푸세요.

---

### 5단계 (10/19 ~ 10/22) — DP 4일 (범위 축소)

25일 플랜에서는 **DP 유형을 2개로 줄입니다.** 전부 하려다 아무것도 못 건지는 게 최악입니다.
(프로그래머스는 배낭 문제 출제가 드물어서 배낭은 후순위로 내렸습니다)

| 날짜 | 할 것 | 문서 |
|---|---|---|
| 10/19 월 | DP 개념 + **유형1 (피보나치형)** | [topics/09](docs/topics/09-dp.md) |
| 10/20 화 | **유형5 (2차원 격자 DP)** ★ 프로그래머스 최빈출 | [topics/09](docs/topics/09-dp.md) |
| 10/21 수 | 2차원 DP 심화 | [topics/09](docs/topics/09-dp.md) |
| 10/22 목 | 다익스트라 **(여유 있을 때만)** / 없으면 BFS 복습 | [topics/10](docs/topics/10-graph-advanced.md) |

**필수 문제 (8개)**:
[피보나치 수](https://school.programmers.co.kr/learn/courses/30/lessons/12945)(Lv2),
[2 x n 타일링](https://school.programmers.co.kr/learn/courses/30/lessons/12900)(Lv2)★,
[멀리 뛰기](https://school.programmers.co.kr/learn/courses/30/lessons/12914)(Lv2),
[땅따먹기](https://school.programmers.co.kr/learn/courses/30/lessons/12913)(Lv2, 2차원)★★,
[정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105)(Lv3, 2차원)★★,
[등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898)(Lv3, 2차원)★,
[N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895)(Lv3, 도전),
[배달](https://school.programmers.co.kr/learn/courses/30/lessons/12978)(Lv2, 다익스트라 — 여유시)

> **DP가 막히면 미련 없이 BFS/DFS 복습으로 전환하세요.**
> 못 푸는 DP 1문제보다 확실히 푸는 BFS 1문제가 점수에 유리합니다.

---

### 6단계 (10/23 금) — 실전 리허설 하루

- **오전/낮 (2시간)**: 타이머 켜고 **Lv.1 + Lv.2 + Lv.2(또는 Lv.3)** 3문제 연속.
  처음 5분은 전체 훑고 순서 정하기. 안 풀어본 문제로 고를 것
- **저녁 (1시간)**: `docs/04-review-log.md` 오답만 다시 풀기 + [실전 전략](docs/03-exam-day.md) 정독
- **새 알고리즘 공부 금지.** 일찍 잘 것

### 10/24 (토) — 시험 🎯

---

### 밀렸을 때 잘라내는 순서 (중요)

일정이 밀리는 건 정상입니다. 아래 순서대로 **위에서부터 버리세요.**

1. 다익스트라 (5단계 마지막 날)
2. DP 유형4 배낭
3. 그리디
4. 투포인터/누적합
5. 힙(heapq)

**절대 못 버리는 것**: 입출력 / 완전탐색 / 정렬·해시 / **BFS·DFS**

## 3. 하루 루틴 (2시간)

| 시간 | 할 일 |
|---|---|
| 10분 | 어제 틀린 문제 **1개 다시 풀기** (복습이 제일 강함) |
| 15분 | 오늘 유형 문서 읽기 |
| 80분 | 문제 2~3개 (**30분 룰** 적용) |
| 15분 | `docs/04-review-log.md` 오답노트 작성 |

25일밖에 없으므로 **문서를 오래 읽지 마세요.** 15분 읽고 바로 문제로 넘어가는 게 맞습니다.
개념은 문제를 풀면서 붙습니다.

### 30분 룰 ★
모르는 문제를 3시간 붙잡는 건 공부가 아니라 낭비입니다.

**30분 고민 → 안 풀리면 풀이를 본다 → 이해한다 → 창을 닫고 다시 직접 구현한다**

마지막 "닫고 다시 구현"을 안 하면 아무것도 안 남습니다. 이게 제일 중요합니다.

---

## 4. 문제 푸는 표준 절차 (항상 이 순서로)

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

## 5. N 보고 알고리즘 고르기 (외울 표)

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

## 6. 시간이 없으니 버릴 것

한 달로는 전부 못 합니다. **아래는 과감히 버리세요.**

- ❌ 세그먼트 트리 / 펜윅 트리
- ❌ 네트워크 플로우
- ❌ 기하 알고리즘 (CCW, 볼록껍질)
- ❌ 문자열 알고리즘 (KMP, 트라이) — 여유 있으면 트라이만
- ❌ 벨만-포드, MST (크루스칼은 코드 짧으니 여유되면)
- ❌ 정렬 알고리즘 직접 구현 (면접용으로만 개념 알기)

대신 **BFS/DFS와 구현에 그 시간을 전부 쓰세요.** 점수 기대값이 훨씬 높습니다.

---

## 7. 레포 사용법

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

## 8. 진도 체크 (직접 갱신)

- [ ] 1단계 (~10/2): 입출력 + 복잡도 + 완전탐색
- [ ] 2단계 (~10/6): 정렬 + 해시 + 스택/큐
- [ ] 3단계 (~10/14): **BFS / DFS** ★★ 최우선
- [ ] 4단계 (~10/18): 이분탐색 + 투포인터 + 그리디
- [ ] 5단계 (~10/22): DP 유형 2개
- [ ] 6단계 (10/23): 모의고사 2시간 3문제
- [ ] 10/24 시험

**합격 신호**: 프로그래머스 **Lv.2를 아무 도움 없이 40분 안에** 풀 수 있으면 통과권입니다.
Lv.3 DFS/BFS까지 풀리면 상위권입니다.
