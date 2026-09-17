"""완전탐색 / 백트래킹 템플릿.

핵심 골격은 항상 같습니다:  넣고 -> 재귀 -> 빼기
"""

from itertools import combinations, permutations, product


def n_and_m(n: int, m: int) -> list[list[int]]:
    """1~n 중 서로 다른 m개를 골라 만든 모든 수열 (BOJ 15649 N과 M(1)).

    백트래킹의 가장 기본형. 사전 순으로 나옵니다.

    >>> n_and_m(3, 2)
    [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
    """
    result: list[list[int]] = []
    current: list[int] = []
    used = [False] * (n + 1)

    def backtrack() -> None:
        if len(current) == m:
            result.append(current[:])      # ★ 복사해서 저장 (안 하면 전부 같은 객체)
            return
        for num in range(1, n + 1):
            if used[num]:
                continue
            used[num] = True
            current.append(num)            # 넣고
            backtrack()                    # 재귀
            current.pop()                  # 빼기 ★ 되돌리기가 백트래킹의 핵심
            used[num] = False

    backtrack()
    return result


def subsets(arr: list[int]) -> list[list[int]]:
    """모든 부분집합을 비트마스크로 생성 (원소 20개 이하일 때).

    mask의 i번째 비트가 1이면 arr[i]를 선택했다는 뜻입니다.

    >>> subsets([1, 2])
    [[], [1], [2], [1, 2]]
    """
    n = len(arr)
    result = []
    for mask in range(1 << n):                       # 0 ~ 2^n - 1
        result.append([arr[i] for i in range(n) if mask & (1 << i)])
    return result


def n_queens(n: int) -> int:
    """N-Queen: 서로 공격하지 못하게 퀸 n개를 놓는 경우의 수 (BOJ 9663).

    가지치기(promising)가 들어간 백트래킹의 대표 예제입니다.

    >>> [n_queens(k) for k in range(1, 7)]
    [1, 0, 0, 2, 10, 4]
    """
    cols = [0] * n          # cols[row] = 그 행에서 퀸을 놓은 열
    count = 0

    def promising(row: int, col: int) -> bool:
        for r in range(row):
            if cols[r] == col:                          # 같은 열
                return False
            if abs(cols[r] - col) == abs(r - row):      # 같은 대각선
                return False
        return True

    def backtrack(row: int) -> None:
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if not promising(row, col):                 # 가지치기
                continue
            cols[row] = col
            backtrack(row + 1)

    backtrack(0)
    return count


def max_operator_result(nums: list[int], ops: list[int]) -> tuple[int, int]:
    """연산자 끼워넣기 (BOJ 14888): ops = [+, -, *, //] 각 개수.

    나눗셈은 음수일 때 '몫을 취하고 절댓값' 규칙(문제 조건)을 따릅니다.

    >>> max_operator_result([1, 2, 3, 4, 5, 6], [2, 1, 1, 1])
    (54, -24)
    """
    n = len(nums)
    best, worst = -10 ** 9, 10 ** 9
    remain = ops[:]

    def backtrack(idx: int, acc: int) -> None:
        nonlocal best, worst
        if idx == n:
            best, worst = max(best, acc), min(worst, acc)
            return
        for op in range(4):
            if remain[op] == 0:
                continue
            remain[op] -= 1
            if op == 0:
                backtrack(idx + 1, acc + nums[idx])
            elif op == 1:
                backtrack(idx + 1, acc - nums[idx])
            elif op == 2:
                backtrack(idx + 1, acc * nums[idx])
            else:
                # 음수 나눗셈은 절댓값으로 나눈 뒤 부호 복원
                backtrack(idx + 1, -(-acc // nums[idx]) if acc < 0 else acc // nums[idx])
            remain[op] += 1

    backtrack(1, nums[0])
    return best, worst


if __name__ == "__main__":
    print("N과 M(1), n=3 m=2:", n_and_m(3, 2))
    print("부분집합 [1,2,3]:", subsets([1, 2, 3]))
    print("N-Queen 8x8:", n_queens(8))
    print("연산자 끼워넣기:", max_operator_result([1, 2, 3, 4, 5, 6], [2, 1, 1, 1]))
    print("itertools 비교:")
    print("  permutations([1,2,3], 2) =", list(permutations([1, 2, 3], 2)))
    print("  combinations([1,2,3], 2) =", list(combinations([1, 2, 3], 2)))
    print("  product([0,1], repeat=2)  =", list(product([0, 1], repeat=2)))
