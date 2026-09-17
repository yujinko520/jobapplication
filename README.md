# Python3 코딩테스트 준비 (노베이스 → 합격권)

> **시험일: 2026년 10월 24일 (토)**
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

## 1. 5주 압축 로드맵 (시험일 2026-10-24)

하루 2시간 기준. 상세 커리큘럼과 주차별 필수 문제는 **[CLAUDE.md](CLAUDE.md)** 에 있습니다.

| 주차 | 기간 | 주제 | 문서 |
|---|---|---|---|
| 1주 | 9/17~9/23 | 입출력 + Python 문법 + 시간복잡도 + 완전탐색 | [00](docs/00-getting-started.md) [01](docs/01-python-cheatsheet.md) [02](docs/02-complexity.md) [구현](docs/topics/01-implementation.md) |
| 2주 | 9/24~9/30 | 정렬 + 해시 + 스택/큐/힙 | [정렬](docs/topics/02-sorting.md) [해시](docs/topics/03-hash.md) [스택·큐](docs/topics/04-stack-queue.md) |
| 3주 | 10/1~10/7 | **BFS / DFS** ★ 최대 고비 | [BFS·DFS](docs/topics/05-bfs-dfs.md) |
| 4주 | 10/8~10/14 | 이분탐색 + 투포인터 + 그리디 | [이분탐색](docs/topics/06-binary-search.md) [투포인터](docs/topics/07-two-pointers.md) [그리디](docs/topics/08-greedy.md) |
| 5주 | 10/15~10/21 | DP + 다익스트라 | [DP](docs/topics/09-dp.md) [그래프](docs/topics/10-graph-advanced.md) |
| 마무리 | 10/22~10/23 | 모의고사 + 오답 복습 | [실전 전략](docs/03-exam-day.md) |

> 3주차(BFS/DFS)와 5주차(DP)에서 대부분 무너집니다.
> 진도가 밀려도 **BFS/DFS는 절대 건너뛰지 마세요.** 출제 빈도 1위입니다.

## 2. 어디서 문제를 푸나

| 플랫폼 | 특징 | 언제 쓰나 |
|---|---|---|
| [백준 (BOJ)](https://www.acmicpc.net/) | 문제 수 압도적, `input()`으로 표준입력 | 유형별 훈련 주력 |
| [프로그래머스](https://programmers.co.kr/) | 함수 `solution()` 채우기, 국내 기업 실제 출제 형식 | 실전 대비 |
| [solved.ac](https://solved.ac/) | 백준 문제 난이도(브론즈~루비) 표시 | 내 수준 문제 찾기 |
| [LeetCode](https://leetcode.com/) | 영어, 외국계/네카라 일부 | 여유 있으면 |

**시작 난이도**: solved.ac 기준 **브론즈 2 → 실버 3**이 노베이스 출발선입니다.
실버 1~골드 5를 별 도움 없이 풀면 대부분 기업 코테 통과권입니다.

추천 커리큘럼: [백준 단계별 풀어보기](https://www.acmicpc.net/step) 를 위에서부터 순서대로.
이미 로드맵이 잘 짜여 있어서 노베이스에겐 이게 제일 빠릅니다.

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

1. [백준](https://www.acmicpc.net/) 회원가입
2. [docs/00-getting-started.md](docs/00-getting-started.md) 읽고 입출력 템플릿 외우기
3. 백준 [1000번 (A+B)](https://www.acmicpc.net/problem/1000) 제출해서 "맞았습니다!" 한 번 보기
4. [BOJ 2798 블랙잭](https://www.acmicpc.net/problem/2798), [BOJ 2231 분해합](https://www.acmicpc.net/problem/2231) 풀기
5. [docs/04-review-log.md](docs/04-review-log.md) 에 오답노트 첫 줄 쓰기

여기까지 하면 1일차 완료입니다. 나머지는 [CLAUDE.md](CLAUDE.md)의 커리큘럼을 따라가세요.
