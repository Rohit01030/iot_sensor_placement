
from utils import generate_random_points, candidate_grid, compute_coverage_sets
from algorithms import greedy_set_cover, greedy_energy_aware
from visualize import plot_solution
import os, time, json, random

OUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')
os.makedirs(OUT_DIR, exist_ok=True)

def run_sample(seed=42):
    random.seed(seed)
    points = generate_random_points(15, 100, 100, seed)
    candidates = candidate_grid(100, 100, 25)
    radius = 30.0

    energies = {i: random.uniform(50, 100) for i in range(len(candidates))}
    costs = {i: 100.0 / energies[i] for i in range(len(candidates))}

    universe, subsets = compute_coverage_sets(points, candidates, radius)

    t0 = time.time()
    greedy_sel = greedy_set_cover(universe, subsets)
    t1 = time.time()
    greedy_time = (t1-t0)*1000

    t0 = time.time()
    energy_sel = greedy_energy_aware(universe, subsets, costs)
    t1 = time.time()
    energy_time = (t1-t0)*1000

    results = {
        "n_points": len(points),
        "n_candidates": len(candidates),
        "radius": radius,
        "greedy": {"selected": greedy_sel, "count": len(greedy_sel), "time_ms": greedy_time},
        "energy_aware": {"selected": energy_sel, "count": len(energy_sel), "time_ms": energy_time}
    }

    with open(os.path.join(OUT_DIR, 'results_energy.json'), 'w') as f:
        json.dump(results, f, indent=2)

    plot_solution(points, candidates, greedy_sel, radius, os.path.join(OUT_DIR, 'greedy_basic.png'))
    plot_solution(points, candidates, energy_sel, radius, os.path.join(OUT_DIR, 'energy_aware.png'))

    print("Energy-aware results saved.")
    return results

if __name__ == '__main__':
    res = run_sample()
    print(json.dumps(res, indent=2))
