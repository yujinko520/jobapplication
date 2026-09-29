"""[프로그래머스] 의상 — 함수형 출제 + 해시

링크: https://school.programmers.co.kr/learn/courses/30/lessons/42578
유형: 해시 + 경우의 수
제한: clothes <= 30  →  완전탐색은 2^30이라 불가능. 수학으로 접근

--- 프로그래머스 형식 ---
- 입력을 직접 읽지 않음 (함수 인자로 들어옴)
- print가 아니라 **return**
- 반환 타입을 문제가 요구한 대로 (여기서는 정수)

--- 설계 ---
1. 종류별 개수를 센다  {'headgear': 2, 'eyewear': 1}
2. 각 종류마다 "안 입는 경우"를 포함해 (개수 + 1) 가지 선택지
3. 전부 곱한 뒤, "전부 안 입는 경우" 1가지를 뺀다
   → (2+1) * (1+1) - 1 = 5

--- 왜 이 공식인가 ---
종류가 독립이므로 곱의 법칙. 단, 알몸(전부 미착용)은 제외해야 하므로 -1.
"""

from collections import Counter


def solution(clothes: list[list[str]]) -> int:
    counter = Counter(kind for name, kind in clothes)

    answer = 1
    for cnt in counter.values():
        answer *= (cnt + 1)                # +1 = 그 종류를 안 입는 경우
    return answer - 1                      # -1 = 전부 안 입는 경우 제외


if __name__ == "__main__":
    t1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    t2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    print("예제1:", solution(t1), "/ 기대: 5")
    print("예제2:", solution(t2), "/ 기대: 3")
