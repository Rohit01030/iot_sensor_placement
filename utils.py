import random
import math
from typing import List, Tuple, Dict, Set

# ------------------------------------------------------
# Generate random target points (e.g., IoT devices to cover)
# ------------------------------------------------------
def generate_targets(num_targets: int, seed: int = 42) -> List[Tuple[float, float]]:
    random.seed(seed)
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_targets)]


# ------------------------------------------------------
# Generate random candidate sensor positions
# ------------------------------------------------------
def generate_candidates(num_candidates: int, seed: int = 42) -> List[Tuple[float, float]]:
    random.seed(seed + 1)
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_candidates)]


# ------------------------------------------------------
# Compute coverage map — which targets each candidate covers
# ------------------------------------------------------
def compute_coverage(
    targets: List[Tuple[float, float]],
    candidates: List[Tuple[float, float]],
    coverage_radius: float
) -> Dict[int, Set[int]]:
    coverage_map = {}
    for i, candidate in enumerate(candidates):
        coverage_map[i] = set()
        for j, target in enumerate(targets):
            dist = math.sqrt((candidate[0] - target[0])**2 + (candidate[1] - target[1])**2)
            if dist <= coverage_radius:
                coverage_map[i].add(j)
    return coverage_map
