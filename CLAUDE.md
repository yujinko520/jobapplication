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

## 2. 커리큘럼 — 🚨 **2026-10-19 비상 재정비 (D-5)**

> ⚠️ **10/6~10/18 13일 공백 발생.** 실제 학습일은 **9/29, 9/30, 10/5 (3일 · 13문제)** 뿐이다.
> 남은 학습일은 **10/19 ~ 10/23 의 5일**이고, 10/24가 시험이다.
> **이전 버전(25일/19일 플랜)은 전부 무효다.** 아래가 유일한 확정 일정이다.

### 현재 보유 자산 (3일 · 13문제)

| 유형 | 상태 |
|---|---|
| 완전탐색 (조합·순열, itertools) | ✅ **됨** — 삼총사 1트, 카펫·소수 찾기 통과 |
| 구현·시뮬레이션 (격자 좌표, 방향 dict) | ✅ **됨** — 공원 산책·키패드·바탕화면 정리 |
| 그리디 (처리된 범위를 변수로) | 🟡 1문제만 (덧칠하기) |
| dict / set / sorted 기본기 | 🟡 써봤음. 유형으로 배운 적은 없음 |
| **BFS / DFS** | ❌ **전혀 안 봤음** ← 출제 비중 ★★★★★ |
| 스택·큐·힙 / 정렬 key / DP / 이분탐색 | ❌ 안 봤음 |

### 일정 — 🔻 **2026-10-20 23:15 재조정 (D-4, 남은 학습일 3일)**

> **10/19 밤 ~ 10/20 은 한 세션이었다.** 타겟 넘버·네트워크·무인도 여행 3문제를 그 세션에서 끝냈다.
> 즉 **10/20 슬롯이 10/19 분량에 쓰였고, 격자 BFS 최단거리는 아직 시작하지 않았다.**
> 남은 학습일은 **10/21, 10/22, 10/23 의 3일**이다.

| 날짜 | 주제 | 목표 | 왜 여기인가 |
|---|---|---|---|
| ~~10/19 밤~10/20~~ | ~~BFS/DFS 1일차~~ | 3문제 | ✅ **완료** — 재귀/그래프/격자 세 형태 |
| **10/21 (수)** | **격자 BFS 최단거리 (큐)** ★★ | 4~5 | **최대 관문.** 단일 최빈출 유형. 하루를 전부 쓴다 |
| **10/22 (목)** | **해시 + 정렬** + BFS 복습 2 | 5~6 | 가장 **저렴한 점수** + BFS 3번째 접촉 |
| **10/23 (금)** | **모의고사 1회 (2시간)** + 복기 + 치트시트 | 3 + 복기 | 타이머를 한 번은 켜봐야 한다 |
| **10/24 (토)** | — | **시험** 🎯 | |

#### 🚨 2026-10-22 22:00 최종 재조정 — **시험 구성 정보 입수 (D-2)**

> 학습자가 입수한 정보 (2026-10-22, 2차 갱신):
> **BFS/DFS 2문제 + DP 1문제**, 그리고 공부할 범위는
> **BFS/DFS · 그리디 · DP · 구현/시뮬레이션** 네 가지.
> ⚠️ 전해 들은 정보이므로 100% 확정은 아니다. 다만 BFS/DFS 비중(★★★★★)과 일치하므로
> **이 구성을 전제로 남은 시간을 배분한다.**

**4유형 현황 — 메울 곳은 둘뿐이다**

| 유형 | 상태 | 할 일 |
|---|---|---|
| **BFS / DFS** | ✅ **강함** (6문제: 재귀·그래프·격자·최단거리·미끄러짐) | 템플릿 암기 + 변종 2개 |
| **구현 / 시뮬레이션** | ✅ **확보** (덧칠하기·키패드·공원 산책·바탕화면 정리·카드 뭉치 등 9문제) | **신규 불필요.** 모의고사로 확인만 |
| **DP** | ❌ **공백** | 10/22 밤 1차원 + 10/23 오전 2차원 |
| **그리디** | 🟡 **1문제만** (9/30 덧칠하기 — 처리된 범위를 변수로) | 10/23 오후 2~3문제 ← **가장 싸다** |

> **그리디가 가장 싸게 메워진다**: 핵심 아이디어가 *"정렬하고 앞에서부터"* / *"양끝에서"* 두 개뿐이고,
> 「체육복」·「구명보트」가 각 15~20분이다. 「덧칠하기」로 패턴을 한 번 겪은 것도 있다.
> **DP가 제일 비싸다** — 그래서 오늘 밤부터 시작한다.

**이 정보가 바꾸는 것**

| 유형 | 기존 판단 | 변경 | 근거 |
|---|---|---|---|
| **BFS / DFS** | 확보 (6문제) | **유지 + 유지보수** | **2문제 = 점수의 대부분** |
| **DP** | ❌ 완전히 버림 | 🔺 **즉시 학습** | **1문제 출제.** 안 배우면 그 1문제가 0점 |
| **그리디** | ❌ 완전히 버림 | 🔺 **부활 (10/23 오후)** | 출제 범위에 포함. 학습 비용이 가장 낮다 |
| 해시 / 정렬 | 10/22 주력 | ❌ **삭제** | 출제 범위에 없음. 4유형에 시간을 전부 쓴다 |
| 스택·큐·힙 | 보너스 | ❌ **삭제** | 같은 이유 |
| 모의고사 2시간 | 10/23 고정 | 🔻 **90분으로 단축** | 아래 참고 |

**남은 시간은 두 덩어리뿐이다**

| 시점 | 가용 시간 | 할 일 |
|---|---|---|
| **10/22 밤 (22:00~)** | ~2시간 | **DP 1차원** — 오늘 밤 시작해야 자면서 정리된다 |
| **10/23 (금) 종일** | 풀타임 | DP 2차원 → BFS/DFS 유지보수 → **모의 90분** → 치트시트 정리 |
| **10/24 (토) 아침** | — | **`docs/05-exam-final-check.md` 한 장만.** 새 문제 금지 |

**모의고사를 2시간 → 90분으로 줄인 이유**

카카오 세트(신고 결과 받기·문자열 압축·튜플)는 **이번 시험 구성과 안 맞는다.**
세트를 **BFS 1 + DFS/BFS 1 + DP 1** 로 바꿔 **실제 출제 형태를 그대로 리허설**한다.
운영 감각(5분 훑기 → A부터 → 45분 룰)은 90분으로도 충분히 훈련된다.

---

### 10/22 (목) 밤 — **DP 1차원** ★ 완전 신규

| | 문제 | 레벨 | 역할 |
|---|---|---|---|
| 1 | [피보나치 수](https://school.programmers.co.kr/learn/courses/30/lessons/12945) | Lv2 | **점화식의 원형.** DP 3단계를 익힌다 |
| 2 | [멀리 뛰기](https://school.programmers.co.kr/learn/courses/30/lessons/12914) | Lv2 | ★ **1번과 점화식이 같다** — 이걸 깨닫는 게 목표 |
| 3 | [2 x n 타일링](https://school.programmers.co.kr/learn/courses/30/lessons/12900) | Lv2 | ★ **또 같은 점화식.** 문제만 다르게 보인다 |

> **오늘 밤의 목표는 3문제를 푸는 게 아니라 「점화식 세우는 3단계」가 손에 붙는 것**이다.
> 세 문제가 **전부 `dp[i] = dp[i-1] + dp[i-2]`** 라는 걸 보면 DP의 절반이 끝난다.
> 이월 복습(소수 만들기·피로도)은 **시간이 남을 때만.** DP가 우선이다.

---

### 10/23 (금) — DP 2차원 → BFS/DFS 유지보수 → 모의 90분

### 10/23 (금) — DP 2차원 → 그리디 → BFS/DFS 유지보수 → 모의 90분

| 순서 | 할 일 | 시간 | 비고 |
|---|---|---|---|
| **1** | **DP 2차원** — [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105) Lv3★★ · [땅따먹기](https://school.programmers.co.kr/learn/courses/30/lessons/12913) Lv2★★ | 2h | **Lv.2~3 DP 최빈출.** 「정수 삼각형」이 가장 전형적 |
| **2** | **그리디** — [체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862) Lv1★ · [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885) Lv2★ | 1h | 아이디어 2개: **"정렬하고 앞에서부터"** / **"양끝 투포인터"** |
| **3** | **빈 화면에서 BFS 큐 + DFS 템플릿 타이핑** | 20m | ★★ 안 보고 쳐야 한다 |
| **4** | **BFS/DFS 변종 2개** — [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163) Lv3★(상태 전이) · [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) Lv2★(백트래킹) | 1.5h | **2문제 출제 대비** |
| **5** | **모의고사 90분** (아래 세트) | 1.5h | 타이머. 중간에 멈추지 않는다 |
| **6** | 복기 + `docs/05-exam-final-check.md` **한 장으로 줄이기** | 1h | 현재 430줄 → 시험장에서 5분에 읽을 분량 |
| **7** | **새 문제 금지. 일찍 잘 것** | | |

**모의고사 세트 (🔒 10/23 저녁까지 열지 말 것) — 4유형을 한 세트로**

| | 문제 | 유형 | 난이도 배치 |
|---|---|---|---|
| A | [예산](https://school.programmers.co.kr/learn/courses/30/lessons/12982) Lv1 | **그리디** | 쉬움 — 먼저 푼다 |
| B | [거리두기 확인하기](https://school.programmers.co.kr/learn/courses/30/lessons/81302) Lv2 | **BFS/DFS + 구현** | 보통 |
| C | [등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898) Lv3★ | **격자 DP** (BFS와 생김새가 비슷해 혼동한다) | 어려움 |

> 🔴 **5번(모의)을 빼먹지 말 것.** 타이머를 한 번도 안 켜보고 시험장에 들어가는 게 최악이다.
> **시간이 부족할 때 자르는 순서: 4번 → 2문제에서 1문제 → 1번 땅따먹기.**
> **1(정수 삼각형)·2·3·5·6 은 지킨다.**
> ⚠️ `algo/dp.py`, `algo/two_pointers.py` 에 템플릿이 있다. **풀기 전에 열지 말 것.**

---

### 10/24 (토) 09:00 — 시험 🎯

**아침에 보는 것은 `docs/05-exam-final-check.md` 한 장뿐.** 새 문제 금지 (학습자 합의).

---

### 🔴 10/20에 추가로 버린 것

| 버린 것 | 근거 |
|---|---|
| ❌ **스택 / 큐 / 힙 전부** (올바른 괄호·기능개발·더 맵게) | 출제 ★★★. 해시·정렬(★★★★)이 더 싸다. 「올바른 괄호」만 여력 있으면 보너스 |
| ❌ **그리디 전부** (체육복·구명보트) | 9/30 「덧칠하기」로 패턴은 한 번 겪었다 |
| ❌ 10/19 잔여 (거리두기·전력망·단어 변환) | 격자 최단거리가 우선. 복습 슬롯에서만 선택적으로 |

> **남은 3일에서 더 밀리면 10/22 해시·정렬을 반으로 줄인다. 10/23 모의고사는 끝까지 건드리지 않는다.**

### 🔴 이번에 버린 것 (5일로는 불가능)

| 버린 것 | 근거 |
|---|---|
| ❌ **DP 전부** (1차원·2차원) | 점화식 세우기는 벼락치기 효율이 가장 낮다. 5일에 넣으면 BFS가 죽는다 |
| ❌ **다익스트라 / 이분탐색 / 투포인터 단독** | 출제 비중 ★★~★★★. BFS에 그 시간을 쓴다 |
| ❌ **Lv.3 DFS** (여행경로 · 순위 · 가장 먼 노드) | Lv.2 격자 BFS를 확실히 하는 게 기대 점수가 높다 |
| ❌ **백트래킹 단독일** | 「피로도」 1문제만 복습 슬롯에서 소화한다 |
| 🔻 **모의고사 4일 → 1일** | 아래 참고 |

> **「모의고사 4일은 절대 못 버린다」를 못 지켰다.** 5일에 BFS 3일 + 모의 4일은 물리적으로 불가능하다.
> 둘 중 하나를 고르면 **BFS가 먼저다** — 모의고사는 "아는 것을 꺼내는 훈련"이고,
> 지금은 **꺼낼 것 자체가 없다.** 단, **10/23 2시간 1회는 끝까지 지킨다.**
> 타이머를 한 번도 안 켜보고 시험장에 들어가는 것이 최악이다.

---

### 10/19 (월) — BFS/DFS 1일차 · **8문제**

**주제: 재귀 탐색 + 덩어리 세기 (flood fill)**

| | 문제 | 레벨 | 역할 |
|---|---|---|---|
| 1 | [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) | Lv2★ | **DFS 재귀 입문.** 10/5 도구 #20(깊이가 변하면 재귀)의 직속 후속 |
| 2 | [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) | Lv3★ | **탐색 템플릿 첫 적용.** 덩어리(연결요소) 개수 세기 |
| 3 | [무인도 여행](https://school.programmers.co.kr/learn/courses/30/lessons/154540) | Lv2★ | **격자 flood fill.** 9/30 공원 산책의 좌표 다루기가 그대로 쓰인다 |
| 4 | [거리두기 확인하기](https://school.programmers.co.kr/learn/courses/30/lessons/81302) | Lv2 | 격자 탐색 + 거리 제한 |
| 5 | [전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971) | Lv2 | 완전탐색 × 그래프 탐색 결합 |
| 6 | [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163) | Lv3★ | 격자가 아닌 **상태 전이** 탐색 (오늘 제일 어려움) |
| 🔁 7 | [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) | Lv2 | 복습 — 백트래킹 (10/6에 못 한 것) |
| 🔁 8 | [소수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12977) | Lv1 | 복습 — 조합 완전탐색 (삼총사 유형) |

> **필수선은 1~4번이다.** 오늘의 목표는 "4문제를 풀었다"가 아니라
> **「방문 표시 + 큐/재귀로 퍼뜨리기」가 손에 붙는 것**이다. 5~8번은 여력이 남을 때.

---

### 10/21 (수) — **격자 BFS 최단거리 (큐) ★★ 최대 관문**

| | 문제 | 레벨 | 역할 |
|---|---|---|---|
| 1 | [미로 탈출](https://school.programmers.co.kr/learn/courses/30/lessons/159993) | Lv2★ | **BFS 큐 템플릿 첫 적용.** 5자리 ID = Python 확실 |
| 2 | [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) | Lv2★★ | 격자 최단거리 표준형 ⚠️ **Python 지원 확인 필요(4자리 ID)** |
| 3 | [리코쳇 로봇](https://school.programmers.co.kr/learn/courses/30/lessons/169199) | Lv2 | "쭉 미끄러지는" 이동 — 응용 |
| 🔁 4 | [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) | Lv2 | 복습 — 백트래킹 (10/19 이월) |
| 🔁 5 | [소수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12977) | Lv1 | 복습 — 조합 (10/19 이월) |

> **1번을 「미로 탈출」로 바꿨다** — 「게임 맵 최단거리」(1844)의 Python 지원이 미확인이고,
> 관문을 언어 제한에 걸릴 수 있는 문제에 걸 수 없다. 1844가 되면 2번으로 바로 이어서 푼다.
>
> **필수선은 1~2번.** 최단거리 BFS 템플릿이 손에 붙는 것이 이 날의 전부다.
> **최단거리는 BFS만 가능하고 DFS로는 안 된다.** 그 이유를 설명할 수 있어야 한다.
> ⚠️ **`practice/pg_game_map_shortest.py`에 2번 풀이가 들어 있다. 직접 풀기 전에 열지 말 것.**

---

### 10/22 (목) — 해시 + 정렬 **(가장 저렴한 점수)** + BFS 복습

> 🔻 **10/21 조정: 이월된 복습 2문제를 먼저 푼다** (학습자 요청, 2026-10-21).
> 평소 규칙은 「신규 먼저」지만 **이월된 복습은 예외** — 하루 묵으면 더 식고, 어제 유형(탐색·완전탐색)의
> 연장이라 해시·정렬로 넘어가기 전에 닫는 게 낫다. Lv.1+Lv.2 라 30~40분이면 된다.
>
> | 🔁 0-1 | [소수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12977) Lv1 | 조합 완전탐색 — 삼총사 + `is_prime`(도구 #17) 조립 |
> | 🔁 0-2 | [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) Lv2★ | **DFS 백트래킹** — `visited=False` 되돌리기. 유일하게 안 해본 유형 |

| | 문제 | 레벨 | 역할 |
|---|---|---|---|
| 1 | [완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576) | Lv1★ | 해시 기본 — 개수 세기 (10/5 도구 #23) |
| 2 | [실패율](https://school.programmers.co.kr/learn/courses/30/lessons/42889) | Lv1 | 정렬 `key` (튜플 정렬) |
| 3 | [전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577) | Lv2★ | 해시 + 접두어 |
| 4 | [가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746) | Lv2★★ | **정렬 key 커스텀** — 유일한 새 개념 |
| 🔁 5 | **BFS 최단거리 1문제** (10/21에 안 푼 것) | Lv2 | ★ 빼먹지 말 것 |
| 🔁 6 | **빈 화면에서 BFS 큐 템플릿 타이핑** | — | ★★ 이 날의 통과 기준 |

> **필수선은 1~4번.** 여력이 남으면 [올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909)(스택, Lv2) 하나만 보너스.
> ⚠️ **「의상」(42578)은 내지 않는다** — `practice/pg_gym_clothes.py`에 풀이가 있다.
> ⚠️ `algo/sorting_hash.py`에 템플릿이 있다. **문제를 풀기 전에 열지 말 것.**

---

### 10/23 (금) — 모의고사 1회 (2시간) + 복기 + 마무리

**세트 (🔒 10/22까지 열어보지 말 것)**
[신고 결과 받기](https://school.programmers.co.kr/learn/courses/30/lessons/92334) Lv1 +
[문자열 압축](https://school.programmers.co.kr/learn/courses/30/lessons/60057) Lv2 +
[튜플](https://school.programmers.co.kr/learn/courses/30/lessons/64065) Lv2

| 순서 | 할 일 | 시간 |
|---|---|---|
| 1 | **타이머 2시간.** 처음 5분 전체 훑고 A/B/C 분류 → A부터 | 2h |
| 2 | 복기 — 못 푼 이유(유형 미인지 vs 구현 실패), 시간 배분 실패 | 1h |
| 3 | `docs/05-exam-final-check.md` **BFS 템플릿 칸 채우기** + 전체 정독 | 30m |
| 4 | **새 문제 금지. 일찍 잘 것** | |

> 규칙: 검색·힌트·오답노트 금지. **한 문제 45분 넘으면 넘어간다.** 빈칸 제출이 최악이다.

### 10/24 (토) — 시험 🎯

`docs/05-exam-final-check.md` **한 장만** 들고 간다.

---

### ⏱ 5일밖에 없으므로 바뀐 규칙

| | 평소 | 10/19~10/23 |
|---|---|---|
| 막혔을 때 | 30분 룰 | **25분 룰** — 넘으면 `algo/bfs_dfs.py` 등 템플릿을 보고 → 이해 → **덮고 다시 구현** |
| 힌트 | 단계적으로 아껴서 | **BFS는 개념 자체가 처음**이므로 "왜 큐인가 / 왜 방문 표시인가"는 **먼저 설명한다.** 코드는 여전히 직접 쓴다 |
| 복습 | 매일 2문제 | **유지** (버리면 BFS가 하루 만에 식는다) |
| 하루 문제 수 | 5 | **6~8** (학습자가 10/19에 8문제로 상향) |

> 각 날의 문제는 **우선순위 순서**로 적혀 있다. 시간이 부족하면 **뒤에서부터 버린다.**
> 1~4번(또는 표시된 필수선)까지가 그날의 핵심이다.

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

### 고정 복습일 — **10/19 재정비로 전부 삭제됨**

5일에는 신규 없이 복습만 하는 날을 둘 수 없다. 대신 **매일 복습 2문제**로 흡수한다.
단 하나만 남긴다: **10/22의 복습 2문제는 반드시 BFS**로 채운다 (3번째 접촉).

### ⚠️ 13일 공백(10/6~10/18)에 대한 보정

2주 만에 돌아오면 9/29~10/5 내용(완전탐색·구현)은 **식어 있다.**
그래서 **10/19~10/20의 복습 2문제는 1단계 유형**(조합 완전탐색·백트래킹)으로 채운다.
**10/21부터의 복습 2문제는 전부 BFS**다 — 새로 배운 것이 가장 빨리 식는다.

### 복습 방법

❌ 코드를 읽으면서 "아 맞다" 하고 넘어가기 → 아무것도 안 남는다
✅ **빈 화면에서 새 문제를 처음부터 푼다.** 막히면 그때 노트를 본다

> **BFS 템플릿만은 예외**: 10/19~10/23 **매일 한 번씩 빈 화면에서 손으로 친다.**
> "보면 이해된다"와 "빈 화면에서 칠 수 있다"는 전혀 다른 상태다.
> 5일짜리 플랜에서 이것 하나만 지켜져도 시험에서 BFS 1문제는 건진다.

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

### 🔒 모의고사 예약 (10/20~10/23) — **미리 풀지 말 것**

아래 11문제는 실전 모의고사용이다. 복습 문제로 고르지 않는다.
미리 풀어버리면 모의고사가 "아는 문제 다시 풀기"가 되어 의미가 없어진다.

신고 결과 받기(92334) · 문자열 압축(60057) · 튜플(64065) · 주차 요금 계산(92341) ·
캐시(17680) · 후보키(42890) · 파일명 정렬(17686) · 프렌즈4블록(17679) ·
자물쇠와 열쇠(60059) · 다트 게임(17682) · 뉴스 클러스터링(17677)

> ⚠️ 링크가 404면 Claude에게 알릴 것 — 문제 ID를 바로 고친다.

### 🚨 언어 지원 제한 — 구 「카카오 코드」 세트 (2026-10-20 발견)

**lesson ID가 4자리(1xxx)인 문제는 Python을 지원하지 않을 수 있다.** 2026-10-20에
「카카오프렌즈 컬러링북」(1829)이 **C / Java만 선택 가능**해서 커리큘럼에서 제외했다.

| ID | 문제 | 상태 |
|---|---|---|
| **1829** | 카카오프렌즈 컬러링북 | ❌ **Python 불가 — 제외 확정** |
| **1844** | 게임 맵 최단거리 | ⚠️ **확인 필요** ← 10/20 최대 관문. 불가면 「미로 탈출」(159993)로 대체 |
| **1845** | 폰켓몬 | ⚠️ 확인 필요 (해시 복습 풀에 있음) |

> Claude는 `school.programmers.co.kr` 에 접속할 수 없다(egress 차단). **언어 지원 여부는
> 학습자가 페이지에서 확인해주는 수밖에 없다.** 5자리 ID(4xxxx / 1xxxxx)는 신작이라 안전하다.
> 문제를 낼 때 **4자리 ID는 우선순위를 낮추고**, 꼭 내야 하면 대체 문제를 같이 제시한다.

---

## 5. 하루 루틴 — **10/19~10/23: 하루 6~8문제**

| 순서 | 할 일 |
|---|---|
| 1 | 오늘 유형 문서 훑기 (10분. 길게 읽지 말 것) |
| 2 | **신규 4~6문제** (**25분 룰** 적용) ← 학습자 선호: 신규 먼저 |
| 3 | **복습 2문제** — §4 풀에서 지난 유형의 **처음 보는 문제** ★ |
| 4 | `docs/04-review-log.md` 기록 |
| 5 | `docs/05-exam-final-check.md` 갱신 — **추가 + 삭제 둘 다** (아래 참고) |

**원래 합의는 하루 5문제(신규 3 + 복습 2)였다. 10/19 기준 6~8문제로 상향** (학습자 제안).
**복습 2문제는 그대로 유지한다** — 남은 5일에서 이걸 버리면 새로 배운 게 하루 만에 식는다.

### 📌 05번 치트시트 갱신 규칙 (매일, 04번 기록과 함께)

`docs/05-exam-final-check.md`는 **짧아야 가치가 있다.** 그래서 **추가만 하지 않고 지운다.**

1. **오늘 재발한 항목** → §1 표의 「연속 무사」를 **0일**로, 「틀린 횟수」를 +1
2. **오늘 안 나온 항목** → 「연속 무사」 **+1일** (학습일 기준. 쉰 날은 세지 않는다)
3. **졸업 조건을 채운 항목** → §1·§4에서 **그 자리에서 삭제**하고 §8에 한 줄 기록
   - 2회 이하 틀린 항목: **학습일 3일 연속** 무사
   - 3회 이상 틀린 항목(🔴): **학습일 5일 연속 + 모의고사 1회** 무사
   - §4 외울 코드: **빈 화면 재현 2회 연속** 성공 (`[2/2]`)
4. **새 반복 실수**(2회째)가 생기면 §1에 행을 추가한다
5. 졸업했다가 다시 틀리면 §1로 **복귀**시키고, 그때부터는 **무조건 5일 기준**

> ❗ **§3 증상 역색인 / §5 N→알고리즘 표 / §6 운영 규칙 / §4 BFS 템플릿은 졸업시키지 않는다.**
> 실수 목록이 아니라 시험장에서 눈으로 확인하는 조회표이기 때문이다.
>
> 상세 내용은 `04-review-log.md`에 영구 보존되므로, 05번에서 지워도 **잃는 것은 없다.**

- **2시간을 넘겨도 5문제를 채운다.** 시간이 아니라 **문제 수가 기준**이다
- 신규를 먼저 하되, **복습 2문제는 같은 날 안에 반드시 끝낸다.**
  머리가 맑을 때 새 유형을 배우고, 남은 힘으로 아는 유형을 확인하는 순서다
- 3단계 후반(Lv.3 BFS)은 3시간 이상 걸릴 수 있다. 그래도 5문제를 지킨다
- **25분 룰** (D-5라서 30분에서 단축). 넘으면 `algo/` 템플릿이나 풀이를 보고 → 이해하고 →
  **덮고 다시 구현.** 막힌 채로 1시간을 버티는 건 하루를 버리는 것이다.
  남은 5일에는 "한 문제를 혼자 뚫는 것"보다 **유형 수를 늘리는 것**이 기대 점수가 높다

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
| `docs/04-review-log.md` | **오답노트 (학습 기록) — 매일 쌓는다. 가장 중요** |
| `docs/05-exam-final-check.md` | **시험장 치트시트 — 한 장. 10/24에 보는 건 이 파일이다** |

---

## 10. 진도 체크 (직접 갱신)

- [x] 9/29 — 3문제 자력 해결 (두 개 뽑아서 더하기 / 모의고사 / 최소직사각형)
- [x] 9/30 — 5문제 완주 (덧칠하기 / 키패드 / 공원 산책 + 삼총사 / 기사단원의 무기)
- [x] ~~10/1 ~ 10/4~~ — **공백 4일. 10/5에 일정 재정비 완료**
- [x] 1단계 후반 10/5 (1/2일) — 5문제 완주 (카펫·소수 찾기·할인 행사 + 카드 뭉치·바탕화면 정리)
- [x] ~~10/6 ~ 10/18~~ — **공백 13일. 10/19에 비상 재정비 (5일 플랜)**
- [x] **10/19 밤 ~ 10/20 (한 세션) — BFS/DFS 1일차** · 3문제 (타겟 넘버 / 네트워크 Lv.3 / 무인도 여행)
      → 재귀·그래프·격자 **세 형태**를 봤다. **10/20 슬롯이 여기 쓰였다.** 복습 2문제는 10/21로 이월
- [x] **10/21 (수) — 격자 BFS 최단거리 (큐)** ★★ **최대 관문 돌파** · 신규 3문제
      (게임 맵 최단거리 4R / 미로 탈출 3R / 리코쳇 로봇 2R — 라운드 수가 줄었다)
      → 복습 2문제(소수 만들기·피로도)는 **10/22로 이월** (학습자 중단 요청)
- [x] **10/22 (목) 밤 — DP 1차원** ★ **3문제 완주** (피보나치 2R / 멀리 뛰기 2R / 2×n 타일링 **1R**)
      → 세 문제가 전부 `dp[i]=dp[i-1]+dp[i-2]` 라는 걸 직접 세워 확인. **DP 3단계 확보**
      → 이월 복습(소수 만들기·피로도)은 10/23으로 재이월
- [ ] **10/23 (금) — DP 2차원 → 그리디 → BFS/DFS 유지보수 → 모의 90분 → 치트시트 정리**
- [ ] 10/24 (토) 09:00 시험 🎯 — 아침엔 05번 치트시트만

**중간 점검 기준 (D-5 버전)**

| 시점 | 기준 | 못 넘기면 |
|---|---|---|
| ~~10/20~~ | ~~격자 최단거리~~ | ❌ 미달 — 10/19 분량에 슬롯을 썼다 |
| ~~10/21 밤~~ | ~~최단거리 BFS 1문제~~ | ✅ **3문제 통과 — 초과 달성** |
| ~~10/22 밤~~ | ~~DP 3문제가 같은 점화식~~ | ✅ **달성** — 3번은 점화식 즉시 인지 (1라운드) |
| **10/23 낮** | 빈 화면에서 **BFS 큐 + DFS 템플릿** 타이핑 | 모의 전에 30분 더 |
| **10/23 저녁** | 모의 3문제 중 **2개** | 그래도 시험은 본다 |

**D-2 현실적 목표 (시험 구성 정보 반영)**: **BFS/DFS 2문제를 확실히 + DP 1문제에 부분점수.**

| 출제 범위 | 목표 | 현재 |
|---|---|---|
| **BFS/DFS × 2** | **2문제 다 푼다** | ✅ 6문제 경험. 템플릿 암기만 남음 |
| **구현 / 시뮬레이션** | 나오면 푼다 | ✅ 9문제 경험. 신규 학습 불필요 |
| **그리디** | 1문제 풀 수 있게 | 🟡 1문제 → 10/23 오후 2문제 추가 |
| **DP × 1** | 점화식을 세워 1차원이면 풀고, 2차원이면 **부분점수** | ❌ → 10/22 밤 + 10/23 오전 |

> **BFS/DFS 2문제를 다 풀면 그것만으로 통과권**이다. 그리디·DP는 그 위에 얹는다.
> 단 **빈칸 제출은 하지 않는다** — 점화식을 못 세워도 완전탐색이라도 제출하면 부분점수가 나온다.
