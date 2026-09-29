# practice — 직접 풀고 기록하는 곳

> **플랫폼: 프로그래머스** (백준은 2026-04-28 서비스 종료)

## 쓰는 법

1. `_template.py` 를 복사해서 `pg_문제이름.py` 로 만듭니다
2. **먼저 주석으로 설계를 씁니다** (코드 금지!)
3. 구현하고 `python3 practice/pg_문제이름.py` 로 예제를 확인합니다
4. 프로그래머스에 제출합니다
5. 틀렸거나 답을 봤으면 `docs/04-review-log.md` 에 기록합니다

파일명 규칙: `pg_<영문이름>.py`

## 이미 들어있는 예제 (풀이 과정을 보여주는 용도)

| 파일 | 문제 | 배울 것 |
|---|---|---|
| `pg_mock_exam.py` | [모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840) Lv.1 | 완전탐색 + 나머지 순환 |
| `pg_game_map_shortest.py` | [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) Lv.2 | **격자 BFS 최단거리** ★★ |
| `pg_gym_clothes.py` | [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578) Lv.2 | 해시 그룹핑 + 경우의 수 |

**복붙하지 말고 보고 다시 치세요.** 손이 기억해야 시험장에서 나옵니다.

---

## 단계별 필수 문제 체크리스트 (25일 플랜)

문제는 대부분 [고득점 Kit](https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit)에 유형별로 묶여 있습니다.

### 1단계 (9/29~10/2) 구현·완전탐색 — 8문제
- [ ] [두 개 뽑아서 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/68644) Lv.1
- [ ] [최소직사각형](https://school.programmers.co.kr/learn/courses/30/lessons/86491) Lv.1
- [ ] [모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840) Lv.1 ★
- [ ] [덧칠하기](https://school.programmers.co.kr/learn/courses/30/lessons/161989) Lv.1
- [ ] [키패드 누르기](https://school.programmers.co.kr/learn/courses/30/lessons/67256) Lv.1 — 구현
- [ ] [카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842) Lv.2 ★
- [ ] [소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839) Lv.2 — 순열 ★
- [ ] [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) Lv.2 — 백트래킹 ★

### 2단계 (10/3~10/6) 정렬·해시·스택/큐/힙 — 10문제
- [ ] [완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576) Lv.1 ★
- [ ] [K번째수](https://school.programmers.co.kr/learn/courses/30/lessons/42748) Lv.1
- [ ] [같은 숫자는 싫어](https://school.programmers.co.kr/learn/courses/30/lessons/12906) Lv.1
- [ ] [전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577) Lv.2
- [ ] [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578) Lv.2 ★
- [ ] [가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746) Lv.2 ★
- [ ] [H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747) Lv.2
- [ ] [올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909) Lv.2 ★
- [ ] [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586) Lv.2
- [ ] [더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626) Lv.2 ★

### 3단계 (10/7~10/14) BFS/DFS ★★ — 12문제 + 도전 2
- [ ] [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) Lv.2 ★
- [ ] [카카오프렌즈 컬러링북](https://school.programmers.co.kr/learn/courses/30/lessons/1829) Lv.2
- [ ] [무인도 여행](https://school.programmers.co.kr/learn/courses/30/lessons/154540) Lv.2 ★
- [ ] [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) Lv.2 ★★★ **최우선**
- [ ] [미로 탈출](https://school.programmers.co.kr/learn/courses/30/lessons/159993) Lv.2 ★
- [ ] [리코쳇 로봇](https://school.programmers.co.kr/learn/courses/30/lessons/169199) Lv.2
- [ ] [전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971) Lv.2
- [ ] [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) Lv.3 ★
- [ ] [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163) Lv.3 ★
- [ ] [여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164) Lv.3
- [ ] [가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189) Lv.3 ★
- [ ] [순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191) Lv.3
- [ ] (도전) [경주로 건설](https://school.programmers.co.kr/learn/courses/30/lessons/67259) Lv.3
- [ ] (도전) [아이템 줍기](https://school.programmers.co.kr/learn/courses/30/lessons/87694) Lv.3

### 4단계 (10/15~10/18) 이분탐색·투포인터·그리디 — 10문제
- [ ] [체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862) Lv.1 ★
- [ ] [큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883) Lv.2 ★
- [ ] [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885) Lv.2 ★
- [ ] [조이스틱](https://school.programmers.co.kr/learn/courses/30/lessons/42860) Lv.2
- [ ] [연속 부분 수열 합의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/131701) Lv.2
- [ ] [순위 검색](https://school.programmers.co.kr/learn/courses/30/lessons/72412) Lv.2
- [ ] [단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884) Lv.3 ★★
- [ ] [보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258) Lv.3 ★
- [ ] [입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238) Lv.3 ★★
- [ ] [징검다리 건너기](https://school.programmers.co.kr/learn/courses/30/lessons/64062) Lv.3 ★

### 5단계 (10/19~10/22) DP — 8문제
- [ ] [피보나치 수](https://school.programmers.co.kr/learn/courses/30/lessons/12945) Lv.2
- [ ] [2 x n 타일링](https://school.programmers.co.kr/learn/courses/30/lessons/12900) Lv.2 ★
- [ ] [멀리 뛰기](https://school.programmers.co.kr/learn/courses/30/lessons/12914) Lv.2
- [ ] [땅따먹기](https://school.programmers.co.kr/learn/courses/30/lessons/12913) Lv.2 ★★
- [ ] [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105) Lv.3 ★★
- [ ] [등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898) Lv.3 ★
- [ ] (도전) [N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895) Lv.3
- [ ] (여유시) [배달](https://school.programmers.co.kr/learn/courses/30/lessons/12978) Lv.2 — 다익스트라

### 6단계 (10/23) 실전 모의고사 — 2시간 타이머
- [ ] 안 풀어본 Lv.1 1문제 + Lv.2 2문제 연속으로
