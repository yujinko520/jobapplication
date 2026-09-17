"""practice/ 예제 풀이가 백준/프로그래머스 공식 예제와 일치하는지 검증."""

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


def test_boj_2798_blackjack():
    m = load("boj_2798_blackjack.py")
    # 공식 예제
    assert m.solve("5 21\n5 6 7 8 9") == 21
    assert m.solve("10 500\n93 181 245 214 315 36 185 138 216 295") == 497
    # 두 구현이 같은 답을 내는지
    assert m.solve("5 21\n5 6 7 8 9") == m.solve_loops("5 21\n5 6 7 8 9")


def test_boj_2178_maze():
    m = load("boj_2178_maze.py")
    assert m.solve("4 6\n101111\n101010\n101011\n111011") == 15
    assert m.solve("2 25\n1011101110111011101110111\n1110111011101110111011101") == 38
    assert m.solve("7 7\n1011111\n1110001\n1000001\n1000001\n1000001\n1000001\n1111111") == 13
    assert m.solve("1 1\n1") == 1          # 엣지: 시작 = 도착


def test_pg_gym_clothes():
    m = load("pg_gym_clothes.py")
    assert m.solution([["yellowhat", "headgear"],
                       ["bluesunglasses", "eyewear"],
                       ["green_turban", "headgear"]]) == 5
    assert m.solution([["crowmask", "face"],
                       ["bluesunglasses", "face"],
                       ["smoky_makeup", "face"]]) == 3
    assert m.solution([["a", "face"]]) == 1   # 엣지: 한 벌뿐
