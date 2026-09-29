"""[프로그래머스] 모의고사 (Lv.1) — 완전탐색 + 구현

링크: https://school.programmers.co.kr/learn/courses/30/lessons/42840
유형: 완전탐색 / 구현
제한: answers 길이 <= 10,000, 수포자는 3명  ->  O(3N) = 3만. 여유로움

--- 설계 (코드 치기 전에 먼저 쓴 것) ---
1. 세 사람의 찍는 패턴을 리스트로 정의한다 (각각 길이가 다름)
2. 각 사람마다 answers를 훑으며, 패턴을 %(나머지)로 순환시켜 비교
3. 최고 점수를 구하고, 그 점수를 받은 사람 번호를 오름차순으로 모은다

--- 핵심 아이디어 ---
패턴이 반복되므로 i번째 문제에서 그 사람이 찍는 답은
    pattern[i % len(pattern)]
"나머지 연산으로 순환"은 코테에서 계속 나오는 패턴입니다.

--- 엣지 케이스 ---
- 여러 명이 동점이면 전부 반환 (오름차순)
- 반환 타입은 **리스트** (정수 아님)
"""

PATTERNS = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
]


def solution(answers: list[int]) -> list[int]:
    scores = [0, 0, 0]

    for i, correct in enumerate(answers):
        for person, pattern in enumerate(PATTERNS):
            if pattern[i % len(pattern)] == correct:    # ★ 나머지로 순환
                scores[person] += 1

    best = max(scores)
    return [i + 1 for i, sc in enumerate(scores) if sc == best]   # 번호는 1부터


if __name__ == "__main__":
    print("예제1:", solution([1, 2, 3, 4, 5]), "/ 기대: [1]")
    print("예제2:", solution([1, 3, 2, 4, 2]), "/ 기대: [1, 2, 3]")
