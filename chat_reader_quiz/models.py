from dataclasses import dataclass
from typing import List

@dataclass
class Question:
    text: str
    options: List[str]  # [A, B, C, D]
    answer_index: int   # 0..3
