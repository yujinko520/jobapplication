"""practice/ 예제 풀이가 프로그래머스 공식 예제와 일치하는지 검증."""

import importlib.util
from pathlib import Path

PRACTICE = Path(__file__).resolve().parent.parent / "practice"


def load(filename: str):
    """practice/ 안의 파일을 모듈로 불러옵니다 (패키지가 아니라서 경로로 로드)."""
    path = PRACTICE / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_pg_mock_exam():
    """모의고사 (Lv.1) — https://school.programmers.co.kr/learn/courses/30/lessons/42840"""
    m = load("pg_mock_exam.py")
    assert m.solution([1, 2, 3, 4, 5]) == [1]          # 공식 예제1
    assert m.solution([1, 3, 2, 4, 2]) == [1, 2, 3]    # 공식 예제2 (동점자 전원)
    assert m.solution([2]) == [2]                      # 엣지: 1문제
    # 패턴이 실제로 순환하는지 (1번 수포자는 1,2,3,4,5,1,2,... )
    assert m.solution([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [1]


def test_pg_game_map_shortest():
    """게임 맵 최단거리 (Lv.2) — https://school.programmers.co.kr/learn/courses/30/lessons/1844"""
    m = load("pg_game_map_shortest.py")
    ex1 = [[1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1],
           [1, 0, 1, 1, 1],
           [1, 1, 1, 0, 1],
           [0, 0, 0, 0, 1]]
    ex2 = [[1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1],
           [1, 0, 1, 1, 1],
           [1, 1, 1, 0, 0],
           [0, 0, 0, 0, 1]]
    assert m.solution(ex1) == 11        # 공식 예제1
    assert m.solution(ex2) == -1        # 공식 예제2 (도달 불가)
    assert m.solution([[1]]) == 1       # 엣지: 시작 = 도착
    assert m.solution([[1, 1], [0, 1]]) == 3


def test_pg_gym_clothes():
    """의상 (Lv.2) — https://school.programmers.co.kr/learn/courses/30/lessons/42578"""
    m = load("pg_gym_clothes.py")
    assert m.solution([["yellowhat", "headgear"],
                       ["bluesunglasses", "eyewear"],
                       ["green_turban", "headgear"]]) == 5
    assert m.solution([["crowmask", "face"],
                       ["bluesunglasses", "face"],
                       ["smoky_makeup", "face"]]) == 3
    assert m.solution([["a", "face"]]) == 1   # 엣지: 한 벌뿐
