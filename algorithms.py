
import itertools
import math
from typing import List, Set, Dict, Tuple

def greedy_set_cover(universe: Set[int], subsets: Dict[int, Set[int]]) -> List[int]:
    uncovered = set(universe)
    selected = []
    while uncovered:
        best = None
        best_cover = set()
        for s, cover in subsets.items():
            cov = cover & uncovered
            if len(cov) > len(best_cover):
                best = s
                best_cover = cov
        if best is None or len(best_cover) == 0:
            break
        selected.append(best)
        uncovered -= best_cover
    return selected

def greedy_energy_aware(universe: Set[int], subsets: Dict[int, Set[int]], costs: Dict[int, float]) -> List[int]:
    uncovered = set(universe)
    selected = []
    while uncovered:
        best = None
        best_score = -1
        best_cover = set()
        for s, cover in subsets.items():
            cov = cover & uncovered
            if len(cov) == 0:
                continue
            score = len(cov) / (costs.get(s, 1) + 1e-9)
            if score > best_score:
                best = s
                best_score = score
                best_cover = cov
        if best is None:
            break
        selected.append(best)
        uncovered -= best_cover
    return selected
