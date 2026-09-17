"""algo/ 템플릿 검증.

`pytest -q` 가 전부 통과해야 템플릿을 믿고 외울 수 있습니다.
각 모듈의 doctest(문서 안 예제)도 같이 돌립니다.
"""

import doctest
import importlib

import pytest

from algo import (
    backtracking,
    bfs_dfs,
    binary_search,
    dp,
    graph,
    sorting_hash,
    stack_queue,
    two_pointers,
)

MODULE_NAMES = [
    "algo.backtracking",
    "algo.bfs_dfs",
    "algo.binary_search",
    "algo.dp",
    "algo.graph",
    "algo.sorting_hash",
    "algo.stack_queue",
    "algo.two_pointers",
]


@pytest.mark.parametrize("name", MODULE_NAMES)
def test_doctests(name):
    """각 모듈 docstring의 >>> 예제가 전부 맞는지."""
    module = importlib.import_module(name)
    result = doctest.testmod(module, verbose=False)
    assert result.failed == 0, f"{name}: doctest {result.failed}개 실패"


# --- 완전탐색 / 백트래킹 -------------------------------------------------
def test_n_and_m_count():
    # 3P2 = 6가지
    assert len(backtracking.n_and_m(3, 2)) == 6
    assert len(backtracking.n_and_m(4, 4)) == 24


def test_subsets_count():
    assert len(backtracking.subsets([1, 2, 3, 4])) == 16   # 2^4


def test_n_queens_known_values():
    assert backtracking.n_queens(8) == 92                  # 널리 알려진 값
    assert backtracking.n_queens(4) == 2


# --- BFS / DFS -----------------------------------------------------------
def test_bfs_and_dfs_visit_all_reachable():
    g = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3], 5: []}
    assert sorted(bfs_dfs.bfs_order(g, 1)) == [1, 2, 3, 4]      # 5는 고립
    assert sorted(bfs_dfs.dfs_order_recursive(g, 1)) == [1, 2, 3, 4]
    assert bfs_dfs.dfs_order_stack(g, 1) == bfs_dfs.dfs_order_recursive(g, 1)


def test_grid_shortest_path_unreachable():
    maze = [[1, 0], [0, 1]]
    assert bfs_dfs.grid_shortest_path(maze) == -1


def test_count_islands_edge_cases():
    assert bfs_dfs.count_islands([[0, 0], [0, 0]]) == 0
    assert bfs_dfs.count_islands([[1, 1], [1, 1]]) == 1
    assert bfs_dfs.count_islands([[1, 0], [0, 1]]) == 2         # 대각선은 연결 아님


def test_multi_source_bfs_all_ripe_already():
    assert bfs_dfs.multi_source_bfs([[1, 1], [1, 1]]) == 0


def test_bfs_on_numbers_backward_only():
    assert bfs_dfs.bfs_on_numbers(10, 3) == 7                   # 뒤로는 한 칸씩만


# --- 이분탐색 -------------------------------------------------------------
def test_binary_search_edges():
    arr = [1, 3, 5, 7, 9]
    assert binary_search.binary_search(arr, 1) == 0
    assert binary_search.binary_search(arr, 9) == 4
    assert binary_search.binary_search([], 1) == -1


def test_parametric_matches_bruteforce():
    """파라메트릭 결과가 완전탐색 결과와 같은지 (신뢰도 확인)."""
    trees = [20, 15, 10, 17]
    need = 7
    expected = max(h for h in range(0, max(trees) + 1)
                   if sum(max(0, t - h) for t in trees) >= need)
    assert binary_search.max_tree_cut_height(trees, need) == expected


def test_lis_both_implementations_agree():
    for arr in ([10, 20, 10, 30, 20, 50], [1], [5, 4, 3, 2, 1], [1, 1, 1]):
        assert binary_search.lis_length(arr) == dp.lis_length_dp(arr)


# --- 투포인터 / 누적합 -----------------------------------------------------
def test_prefix_sum_matches_naive():
    arr = [3, -1, 4, 1, 5, 9, 2, 6]
    prefix = two_pointers.build_prefix(arr)
    for left in range(len(arr)):
        for right in range(left, len(arr)):
            assert two_pointers.range_sum(prefix, left, right) == sum(arr[left:right + 1])


def test_prefix_sum_2d_matches_naive():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    S = two_pointers.build_prefix_2d(board)
    assert two_pointers.range_sum_2d(S, 0, 0, 2, 2) == 45
    assert two_pointers.range_sum_2d(S, 0, 0, 0, 0) == 1


def test_shortest_subarray_not_found():
    assert two_pointers.shortest_subarray_at_least([1, 1, 1], 10) == 0


def test_subarray_count_with_negatives():
    # 투 포인터로는 못 푸는 케이스를 누적합+해시 버전이 처리하는지
    assert two_pointers.count_subarrays_with_sum_any([1, -1, 1, -1], 0) == 4


# --- 스택 / 큐 / 힙 --------------------------------------------------------
def test_next_greater_all_decreasing():
    assert stack_queue.next_greater([5, 4, 3]) == [-1, -1, -1]


def test_sliding_window_max_matches_naive():
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    naive = [max(arr[i:i + k]) for i in range(len(arr) - k + 1)]
    assert stack_queue.sliding_window_max(arr, k) == naive


def test_merge_cards_order_matters():
    # 10+20=30, 30+40=70 -> 100 (큰 것부터 합치면 더 비쌈)
    assert stack_queue.merge_cards_min_cost([10, 20, 40]) == 100
    assert stack_queue.merge_cards_min_cost([]) == 0


# --- DP -------------------------------------------------------------------
def test_dp_edge_cases():
    assert dp.min_steps_to_one(1) == 0
    assert dp.stairs_max_score([10]) == 10
    assert dp.max_subarray_sum([-1]) == -1
    assert dp.lis_length_dp([]) == 0


def test_knapsack_01_vs_bruteforce():
    from itertools import combinations
    items = [(6, 13), (4, 8), (3, 6), (5, 12)]
    limit = 7
    best = 0
    for r in range(len(items) + 1):
        for pick in combinations(items, r):
            if sum(w for w, _ in pick) <= limit:
                best = max(best, sum(v for _, v in pick))
    assert dp.knapsack_01(items, limit) == best


def test_coin_change_impossible():
    assert dp.coin_change_min([5, 10], 3) == -1
    assert dp.coin_change_min([5, 10], 0) == 0


# --- 그래프 ---------------------------------------------------------------
def test_dijkstra_unreachable_is_inf():
    g = {1: [(2, 1)], 2: [], 3: []}
    dist = graph.dijkstra(g, 1, 3)
    assert dist[2] == 1
    assert dist[3] == float('inf')


def test_dijkstra_matches_bfs_when_all_weights_one():
    weighted = {1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1)], 4: []}
    plain = {1: [2, 3], 2: [4], 3: [4], 4: []}
    d1 = graph.dijkstra(weighted, 1, 4)
    d2 = graph.bfs_shortest_unweighted(plain, 1, 4)
    assert [d1[i] for i in range(1, 5)] == [d2[i] for i in range(1, 5)]


def test_union_find_cycle_detection():
    uf = graph.UnionFind(4)
    assert uf.union(1, 2) is True
    assert uf.union(2, 3) is True
    assert uf.union(1, 3) is False        # 사이클
    assert uf.same(1, 3) is True
    assert uf.same(1, 4) is False


def test_topological_sort_respects_order():
    edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
    order = graph.topological_sort(4, edges)
    pos = {v: i for i, v in enumerate(order)}
    for a, b in edges:
        assert pos[a] < pos[b]


def test_topological_sort_detects_cycle():
    assert graph.topological_sort(3, [(1, 2), (2, 3), (3, 1)]) == []


def test_floyd_warshall_matches_dijkstra():
    edges = [(1, 2, 4), (2, 3, 2), (1, 3, 9), (3, 4, 1)]
    fw = graph.floyd_warshall(4, edges)
    g: dict[int, list[tuple[int, int]]] = {i: [] for i in range(1, 5)}
    for a, b, w in edges:
        g[a].append((b, w))
    dk = graph.dijkstra(g, 1, 4)
    for node in range(1, 5):
        assert fw[1][node] == dk[node]


# --- 정렬 / 해시 -----------------------------------------------------------
def test_sort_two_ways_agree():
    people = [("bob", 90), ("amy", 90), ("cho", 95), ("dan", 80)]
    assert sorting_hash.sort_multi_key(people) == sorting_hash.sort_stable_two_pass(people)


def test_counting_sort_matches_sorted():
    nums = [5, 2, 3, 1, 4, 2, 3, 5, 1, 7, 0]
    assert sorting_hash.counting_sort(nums, 10) == sorted(nums)


def test_exists_and_count_agree():
    cards = [6, 3, 2, 10, 10, -10]
    queries = [10, 9, 2, -10]
    exists = sorting_hash.exists_in_sorted(cards, queries)
    counts = sorting_hash.count_occurrences(cards, queries)
    assert exists == [1 if c > 0 else 0 for c in counts]
