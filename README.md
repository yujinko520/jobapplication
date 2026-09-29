# Python3 코딩테스트 준비 (노베이스 → 합격권)

> **시험일: 2026년 10월 24일 (토)** — 학습 시작 2026-09-29, 남은 기간 **25일**
> **플랫폼: 프로그래머스** (백준은 2026-04-28 서비스 종료)
> 학습 방향과 주차별 커리큘럼은 **[CLAUDE.md](CLAUDE.md)** 를 먼저 읽으세요.

알고리즘은 처음이지만 Python 문법은 다뤄본 사람을 위한 학습 레포입니다.
읽기만 하는 문서가 아니라 **실행하고 테스트할 수 있는 코드**가 같이 있습니다.

```
.
├── docs/           # 학습 가이드 (읽는 순서대로 번호가 붙어 있음)
├── algo/           # 유형별 알고리즘 템플릿 (bfs_dfs, dp, graph, binary_search ...)
├── practice/       # 대표 문제 패턴 풀이 예제
└── tests/          # 위 코드들이 실제로 맞는지 검증하는 테스트
```

## 0. 시작하기 전에 알아야 할 것

코딩테스트는 **"머리 좋은 사람 찾기"가 아니라 "훈련한 사람 찾기"** 시험입니다.
출제되는 유형은 사실상 정해져 있고(15개 내외), 각 유형마다 정해진 풀이 골격이 있습니다.
노베이스가 3개월 안에 합격권에 드는 건 아주 흔한 일이에요.

**핵심 원칙 3가지**

1. **30분 룰** — 모르는 문제를 3시간 붙잡는 건 공부가 아니라 낭비입니다.
   30분 고민 → 안 풀리면 답을 보고 → **이해하고 → 닫고 다시 직접 구현**. 이게 1사이클.
2. **양보다 복습** — 새 문제 10개보다, 푼 문제 3개를 3일 뒤 다시 푸는 게 훨씬 강합니다.
3. **손으로 먼저** — 코드부터 치지 말고 종이/주석에 "입력 → 어떻게 → 출력"을 먼저 쓰세요.
   구현이 막히는 이유의 80%는 문제를 덜 이해해서입니다.

## 1. 25일 로드맵 (9/29 시작 → 10/24 시험)

하루 2시간 기준, 총 50시간. 날짜별 상세 계획과 필수 문제는 **[CLAUDE.md](CLAUDE.md)** 에 있습니다.

| 단계 | 기간 | 일수 | 주제 | 문서 |
|---|---|---|---|---|
| 1 | 9/29~10/2 | 4일 | 입출력 + 시간복잡도 + 완전탐색 | [00](docs/00-getting-started.md) [01](docs/01-python-cheatsheet.md) [02](docs/02-complexity.md) [구현](docs/topics/01-implementation.md) |
| 2 | 10/3~10/6 | 4일 | 정렬 + 해시 + 스택/큐/힙 | [정렬](docs/topics/02-sorting.md) [해시](docs/topics/03-hash.md) [스택·큐](docs/topics/04-stack-queue.md) |
| **3** | **10/7~10/14** | **8일** | **BFS / DFS ★ 최우선** | [BFS·DFS](docs/topics/05-bfs-dfs.md) |
| 4 | 10/15~10/18 | 4일 | 이분탐색 + 투포인터 + 그리디 | [이분탐색](docs/topics/06-binary-search.md) [투포인터](docs/topics/07-two-pointers.md) [그리디](docs/topics/08-greedy.md) |
| 5 | 10/19~10/22 | 4일 | DP (유형 3개) + 다익스트라 | [DP](docs/topics/09-dp.md) [그래프](docs/topics/10-graph-advanced.md) |
| 6 | 10/23 | 1일 | 모의고사 + 오답 복습 | [실전 전략](docs/03-exam-day.md) |

> 25일 중 **8일을 BFS/DFS에 씁니다.** 출제 비중이 압도적이라 투자 대비 회수가 가장 큽니다.
> 일정이 밀리면 DP·그리디를 먼저 자르고, **BFS/DFS는 끝까지 지킵니다.**

## 2. 어디서 문제를 푸나

2026년 4월 백준(BOJ) 종료 이후, 국내 취업용 코테 준비는 **프로그래머스로 수렴**했습니다.
네이버·카카오·라인이 실제 시험에 쓰는 플랫폼이라 **연습 환경 = 실전 환경**입니다.

| 메뉴 | 용도 |
|---|---|
| [고득점 Kit](https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | **유형별 문제집. 이 커리큘럼의 척추** |
| [코딩테스트 연습](https://school.programmers.co.kr/learn/challenges) | 레벨·태그 필터 |

**난이도 기준**: Lv.1을 막힘없이 → **Lv.2가 합격선** → Lv.3은 BFS/DFS·DP만 선별.
Lv.4~5는 버립니다.

> 참고: 삼성(SW Expert Academy) 등 일부는 여전히 표준입력형입니다.
> 필요하면 [docs/00 부록](docs/00-getting-started.md)만 훑으면 됩니다.

## 3. 이 레포 쓰는 법

```bash
# 템플릿 코드가 정말 맞는지 확인 (전부 통과해야 정상)
pytest -q

# 특정 알고리즘만 실행해 보기
python3 -m algo.graph
python3 -m algo.binary_search
```

문제를 풀 때는 `practice/` 안의 예제를 참고하되, **복붙하지 말고 보고 다시 치세요.**
손이 기억해야 시험장에서 나옵니다.

## 4. 오늘 당장 할 일

1. [프로그래머스](https://school.programmers.co.kr/) 회원가입
2. [docs/00-getting-started.md](docs/00-getting-started.md) 읽고 `solution()` 형식 익히기
3. [두 개 뽑아서 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/68644) 제출해서 통과 한 번 보기
4. [모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840), [최소직사각형](https://school.programmers.co.kr/learn/courses/30/lessons/86491) 풀기
5. [docs/04-review-log.md](docs/04-review-log.md) 에 오답노트 첫 줄 쓰기

여기까지 하면 1일차 완료입니다. 나머지는 [CLAUDE.md](CLAUDE.md)의 커리큘럼을 따라가세요.
