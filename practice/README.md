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

## 일자별 신규 문제 체크리스트

**하루 5문제 = 신규 3 + 복습 2.** 아래는 **신규 3문제**만.
복습 2문제는 [CLAUDE.md §4 복습 풀](../CLAUDE.md)에서 고릅니다.

### 1단계 (9/29~10/2) 구현·완전탐색
- **9/29 화** ✅ — [두 개 뽑아서 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/68644) / [모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840) / [최소직사각형](https://school.programmers.co.kr/learn/courses/30/lessons/86491)
- [ ] **9/30 수** — [덧칠하기](https://school.programmers.co.kr/learn/courses/30/lessons/161989) / [키패드 누르기](https://school.programmers.co.kr/learn/courses/30/lessons/67256)★ / [공원 산책](https://school.programmers.co.kr/learn/courses/30/lessons/172928)
- [ ] **10/1 목** — [카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842) / [소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839)★ / [할인 행사](https://school.programmers.co.kr/learn/courses/30/lessons/131127)
- [ ] **10/2 금** — [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946)★ / [전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971) / [행렬 테두리 회전하기](https://school.programmers.co.kr/learn/courses/30/lessons/77485)

### 2단계 (10/3~10/6) 정렬·해시·스택큐·힙
- [ ] **10/3 토** — [K번째수](https://school.programmers.co.kr/learn/courses/30/lessons/42748) / [문자열 내 마음대로 정렬하기](https://school.programmers.co.kr/learn/courses/30/lessons/12915) / [가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746)★
- [ ] **10/4 일** — [완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576)★ / [폰켓몬](https://school.programmers.co.kr/learn/courses/30/lessons/1845) / [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578)★
- [ ] **10/5 월** — [같은 숫자는 싫어](https://school.programmers.co.kr/learn/courses/30/lessons/12906) / [올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909)★ / [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586)
- [ ] **10/6 화** 복습일 — [더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626)★ **(신규 1) + 복습 4**

### 3단계 (10/7~10/13) BFS/DFS ★★
- [ ] **10/7 수** — [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)★ / [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165)★ / [카카오프렌즈 컬러링북](https://school.programmers.co.kr/learn/courses/30/lessons/1829)
- [ ] **10/8 목** — [여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164) / [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163)★ / [거리두기 확인하기](https://school.programmers.co.kr/learn/courses/30/lessons/81302)
- [ ] **10/9 금** — [무인도 여행](https://school.programmers.co.kr/learn/courses/30/lessons/154540)★ / [리코쳇 로봇](https://school.programmers.co.kr/learn/courses/30/lessons/169199) / [퍼즐 조각 채우기](https://school.programmers.co.kr/learn/courses/30/lessons/84021)(도전)
- [ ] **10/10 토** ★★ — [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844)★★ / [미로 탈출](https://school.programmers.co.kr/learn/courses/30/lessons/159993)★ / [경주로 건설](https://school.programmers.co.kr/learn/courses/30/lessons/67259)(도전)
- [ ] **10/11 일** — [가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189)★ / [순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191) / [아이템 줍기](https://school.programmers.co.kr/learn/courses/30/lessons/87694)
- [ ] **10/12 월** — [배달](https://school.programmers.co.kr/learn/courses/30/lessons/12978)★ / [섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861) / [합승 택시 요금](https://school.programmers.co.kr/learn/courses/30/lessons/72413)(도전)
- [ ] **10/13 화** 복습일 — **신규 없음 · 복습 5 + BFS 템플릿 암기 확인**

### 4단계 (10/14~10/16) 이분탐색·투포인터·그리디
- [ ] **10/14 수** — [예산](https://school.programmers.co.kr/learn/courses/30/lessons/12982) / [순위 검색](https://school.programmers.co.kr/learn/courses/30/lessons/72412) / [입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238)★★
- [ ] **10/15 목** — [징검다리 건너기](https://school.programmers.co.kr/learn/courses/30/lessons/64062)★ / [연속 부분 수열 합의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/131701) / [보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258)★
- [ ] **10/16 금** — [체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862)★ / [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885)★ / [큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883)★

### 5단계 (10/17~10/19) DP
- [ ] **10/17 토** — [피보나치 수](https://school.programmers.co.kr/learn/courses/30/lessons/12945) / [멀리 뛰기](https://school.programmers.co.kr/learn/courses/30/lessons/12914) / [2 x n 타일링](https://school.programmers.co.kr/learn/courses/30/lessons/12900)★
- [ ] **10/18 일** — [땅따먹기](https://school.programmers.co.kr/learn/courses/30/lessons/12913)★★ / [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105)★★ / [등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898)★
- [ ] **10/19 월** — [조이스틱](https://school.programmers.co.kr/learn/courses/30/lessons/42860) / [단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884)★★ / [N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895)(도전)

### 6단계 (10/20~10/23) 🔴 실전 모의고사 — **타이머 필수, 미리 풀지 말 것**

- [ ] **10/20 화** 1회차 · 2시간 — [신고 결과 받기](https://school.programmers.co.kr/learn/courses/30/lessons/92334) + [문자열 압축](https://school.programmers.co.kr/learn/courses/30/lessons/60057) + [튜플](https://school.programmers.co.kr/learn/courses/30/lessons/64065)
- [ ] **10/21 수** 2회차 · 2시간 — [주차 요금 계산](https://school.programmers.co.kr/learn/courses/30/lessons/92341) + [캐시](https://school.programmers.co.kr/learn/courses/30/lessons/17680) + [후보키](https://school.programmers.co.kr/learn/courses/30/lessons/42890)
- [ ] **10/22 목** 3회차 · 2.5시간 — [파일명 정렬](https://school.programmers.co.kr/learn/courses/30/lessons/17686) + [프렌즈4블록](https://school.programmers.co.kr/learn/courses/30/lessons/17679) + [자물쇠와 열쇠](https://school.programmers.co.kr/learn/courses/30/lessons/60059)
- [ ] **10/23 금** 4회차 · 1시간 — [다트 게임](https://school.programmers.co.kr/learn/courses/30/lessons/17682) + [뉴스 클러스터링](https://school.programmers.co.kr/learn/courses/30/lessons/17677) → 이후 오답노트 정독

**모의고사 규칙**: 타이머 ON · 처음 5분 전체 훑고 순서 정하기 · 검색/힌트 금지 ·
한 문제 45분 넘으면 넘어가기 · 끝난 뒤에만 채점

**끝나고 1시간 복기가 본론**: 못 푼 이유(유형 인식 실패? 구현 실패?) / 시간 배분 실패 여부

---

> ⚠️ 링크가 404면 Claude에게 알려주세요. 문제 ID를 바로 고칩니다.
