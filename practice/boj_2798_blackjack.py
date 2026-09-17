"""[BOJ 2798] 블랙잭 — 완전탐색 입문

링크: https://www.acmicpc.net/problem/2798
유형: 완전탐색 (조합)
제한: N <= 100  →  3중 루프 O(N^3) = 100만. 충분히 가능 ★ N이 작다 = 다 해보라는 뜻

--- 설계 ---
1. 카드 N장 중 3장을 고르는 모든 조합을 본다
2. 합이 M 이하인 것 중 최댓값을 기록
3. 출력

--- 엣지 케이스 ---
- 정확히 M이 되는 경우가 있으면 그게 답
- N = 3 이면 조합이 하나뿐
"""

import sys
from itertools import combinations


def solve(data: str) -> int:
    lines = data.strip().split('\n')
    n, m = map(int, lines[0].split())
    cards = list(map(int, lines[1].split()))

    best = 0
    for trio in combinations(cards, 3):    # 3장 고르는 모든 조합
        total = sum(trio)
        if total <= m:
            best = max(best, total)
    return best


def solve_loops(data: str) -> int:
    """itertools 없이 3중 루프로 짠 버전 (같은 답). 둘 다 칠 줄 알아야 합니다."""
    lines = data.strip().split('\n')
    n, m = map(int, lines[0].split())
    cards = list(map(int, lines[1].split()))

    best = 0
    for i in range(n):
        for j in range(i + 1, n):          # ★ i+1부터: 같은 카드 중복 선택 방지
            for k in range(j + 1, n):
                total = cards[i] + cards[j] + cards[k]
                if total <= m:
                    best = max(best, total)
    return best


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    EXAMPLE = "5 21\n5 6 7 8 9"
    print("결과:", solve(EXAMPLE), "/ 기대: 21")
    print("루프 버전:", solve_loops(EXAMPLE))
