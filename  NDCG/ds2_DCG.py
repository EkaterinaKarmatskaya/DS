from typing import List
from math import log

import numpy as np


def discounted_cumulative_gain(
    relevance: List[float], k: int, method: str = "standard"
) -> float:
    score = 0
    if method == "standard":
        for i in range(0, k):
            score = relevance[i] / log(i + 2, 2) + score
    elif method == "industry":
        for i in range(0, k):
            score = (2 ** relevance[i] - 1) / log(i + 2, 2) + score
    else:
        method = "raise ValueError"

    return score
