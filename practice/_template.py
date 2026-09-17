"""[문제 번호] 문제 이름

링크: https://www.acmicpc.net/problem/____
유형: ____
제한: N <= ____  →  허용 복잡도 O(____)

--- 설계 (코드 치기 전에 여기부터 채우세요) ---
1.
2.
3.

--- 엣지 케이스 ---
- n = 1 일 때?
- 답이 없을 때 출력값은?
"""

import sys


def solve(data: str) -> str:
    """입력 문자열을 받아 출력 문자열을 반환 (테스트하기 쉽게 분리)."""
    lines = data.strip().split('\n')
    # n = int(lines[0])
    # arr = list(map(int, lines[1].split()))
    return ""


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    # 제출 전 예제로 확인
    EXAMPLE_IN = """
"""
    EXAMPLE_OUT = """
"""
    got = solve(EXAMPLE_IN)
    print("결과:", got)
    print("기대:", EXAMPLE_OUT.strip())
