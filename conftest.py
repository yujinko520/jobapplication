"""레포 루트를 import 경로에 추가 (pytest 버전과 무관하게 algo/practice import 가능)."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
