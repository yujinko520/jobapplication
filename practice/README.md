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
| `pg_game_map_shortest.py` | [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) Lv.2 | **격자 BFS 최단거리** ★★ 🔒 **10/20에 직접 풀기 전까지 열지 말 것** |
| `pg_gym_clothes.py` | [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578) Lv.2 | 해시 그룹핑 + 경우의 수 |

**복붙하지 말고 보고 다시 치세요.** 손이 기억해야 시험장에서 나옵니다.

---

## 일자별 신규 문제 체크리스트

> 🚨 **2026-10-19 비상 재정비 (D-5).** 10/6~10/18 13일 공백. 이전 체크리스트는 전부 무효.
> 남은 학습일은 **10/19~10/23 의 5일**. 하루 **6~8문제**.
> 각 날의 문제는 **우선순위 순**이다. 시간이 부족하면 **뒤에서부터 버린다.**

### 10/19 (월) — BFS/DFS 1일차 · 재귀 + 덩어리 세기 · **8문제**

- [ ] 1. [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) Lv2★ — DFS 재귀 입문
- [ ] 2. [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) Lv3★ — 탐색 템플릿 첫 적용
- [x] ~~3. 카카오프렌즈 컬러링북(1829)~~ — ❌ **Python 미지원(C/Java만). 10/20 제외**
- [ ] 3. [무인도 여행](https://school.programmers.co.kr/learn/courses/30/lessons/154540) Lv2★ — 격자 flood fill
      ↑ **여기까지가 필수선**
- [ ] 4. [거리두기 확인하기](https://school.programmers.co.kr/learn/courses/30/lessons/81302) Lv2 — 격자 탐색
- [ ] 5. [전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971) Lv2
- [ ] 6. [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163) Lv3★ — 상태 전이
- [ ] 🔁 7. [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) Lv2 — 복습(백트래킹)
- [ ] 🔁 8. [소수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12977) Lv1 — 복습(조합)

### 10/20 (화) — BFS/DFS 2일차 · 격자 최단거리 ★★

- [ ] 1. [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) Lv2★★ ← **최대 관문**
      ⚠️ **Python 지원 여부 먼저 확인!** (ID가 4자리 = 구 카카오 세트)
      미지원이면 → [미로 탈출](https://school.programmers.co.kr/learn/courses/30/lessons/159993) 을 관문으로 삼는다
- [ ] 2. [미로 탈출](https://school.programmers.co.kr/learn/courses/30/lessons/159993) Lv2★
- [ ] 3. [리코쳇 로봇](https://school.programmers.co.kr/learn/courses/30/lessons/169199) Lv2
- [ ] 4. [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163) Lv3★ — 상태 전이 BFS
- [ ] 🔁 5. [옹알이(2)](https://school.programmers.co.kr/learn/courses/30/lessons/133499) Lv1 — 복습(구현)
- [ ] 🔁 6. [실패율](https://school.programmers.co.kr/learn/courses/30/lessons/42889) Lv1 — 복습(완전탐색)

### 10/21 (수) — 해시 + 정렬

- [ ] 1. [완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576) Lv1★
- [ ] 2. [전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577) Lv2★
- [ ] 3. [가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746) Lv2★★ — 정렬 `key`
- [ ] 4. [오픈채팅방](https://school.programmers.co.kr/learn/courses/30/lessons/42888) Lv2
- [ ] 5. [H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747) Lv2
- [ ] 🔁 6~7. **BFS 2문제** (10/19~10/20 중 안 푼 것) ★

### 10/22 (목) — 스택·큐·힙 + 그리디 + BFS 복습

- [ ] 1. [올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909) Lv2★ — 스택
- [ ] 2. [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586) Lv2 — 큐
- [ ] 3. [더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626) Lv2★ — 힙
- [ ] 4. [체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862) Lv1★ — 그리디
- [ ] 5. [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885) Lv2★ — 그리디 + 투포인터
- [ ] 🔁 6. **빈 화면에서 BFS 템플릿 타이핑** ★★ ← 이 날의 통과 기준
- [ ] 🔁 7. BFS/DFS 남은 문제 1개

### 10/23 (금) — 모의고사 1회 (2시간) + 복기

- [ ] 타이머 2시간: 신고 결과 받기(92334) + 문자열 압축(60057) + 튜플(64065)
- [ ] 복기 1시간 — `docs/04-review-log.md`
- [ ] `docs/05-exam-final-check.md` **BFS 템플릿 칸 채우기** + 전체 정독
- [ ] 일찍 자기

### 10/24 (토) — 시험 🎯

`docs/05-exam-final-check.md` 한 장만 들고 간다.

---

## ❌ 10/19에 버린 것 (안 배우고 시험 본다)

- **DP 전부** (피보나치·멀리뛰기·2×n 타일링·땅따먹기·정수 삼각형·등굣길)
- **다익스트라 / 최단경로** (배달·섬 연결하기·아이템 줍기)
- **이분탐색 / 파라메트릭** (입국심사·순위 검색)
- **Lv.3 DFS** (여행경로·순위·가장 먼 노드)
- **모의고사 2~4회차** (주차 요금 계산·캐시·후보키·파일명 정렬·프렌즈4블록·자물쇠와 열쇠·다트 게임·뉴스 클러스터링)

> 시험에 DP나 이분탐색이 나오면 **버린다.** 5일에 다 담을 수 없다.
> 대신 **BFS/DFS + 구현 + 해시/정렬**(출제의 60% 이상)에 전부 쏟는다.
