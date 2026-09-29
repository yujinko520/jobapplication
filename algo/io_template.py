"""표준입력형(삼성 SWEA 등) 문제용 입출력 템플릿 — 부록.

주력 플랫폼인 프로그래머스는 `solution()` 함수형이라 이 파일이 필요 없습니다.
삼성 SW Expert Academy나 자체 플랫폼 코테를 보게 될 때만 참고하세요.
알고리즘 자체는 동일하고, 입출력 껍데기만 다릅니다.
"""

TEMPLATE = '''
import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from itertools import permutations, combinations, product
import bisect, math

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(arr))


solve()
'''

# 입력 패턴 치트시트 --------------------------------------------------------
#   n = int(input())                          정수 하나
#   a, b = map(int, input().split())          한 줄에 정수 둘
#   arr = list(map(int, input().split()))     한 줄에 정수 여러 개
#   s = input().rstrip()                      문자열 (개행 제거 필수!)
#   board = [list(map(int, input().split())) for _ in range(n)]   2차원 배열
#   grid = [input().rstrip() for _ in range(n)]                   문자열 격자
#
# 출력 패턴 ----------------------------------------------------------------
#   print(*arr)                           "1 2 3"
#   print('\n'.join(map(str, arr)))       반복 print보다 훨씬 빠름
#
# 프로그래머스형 -------------------------------------------------------------
#   def solution(arr, k):
#       return answer        # print가 아니라 return!

if __name__ == "__main__":
    print(TEMPLATE)
