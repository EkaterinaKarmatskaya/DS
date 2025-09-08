from typing import List

import numpy as np


def cumulative_gain(relevance: List[float], k: int) -> float:
    score = 0
    for i in range(0, k):
        score = relevance[i] + score

    return score