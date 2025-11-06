import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import List, Tuple


def plot_coverage(
    targets: List[Tuple[float, float]],
    candidates: List[Tuple[float, float]],
    selected: List[int],
    coverage_radius: float,
    ax,
    title: str
):
    """
    Visualizes IoT sensor placement.
    - targets: list of (x, y) positions of IoT nodes to cover
    - candidates: list of (x, y) potential sensor positions
    - selected: indices of chosen sensors
    - coverage_radius: coverage distance
    - ax: matplotlib axis
    - title: plot title
    """
    ax.set_title(title)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.set_xlabel("X-coordinate")
    ax.set_ylabel("Y-coordinate")

    # Plot targets (red)
    tx, ty = zip(*targets)
    ax.scatter(tx, ty, c='red', marker='x', label='Targets')

    # Plot all candidate sensors (light gray)
    cx, cy = zip(*candidates)
    ax.scatter(cx, cy, c='gray', alpha=0.4, label='Candidate Sensors')

    # Plot selected sensors (green) + coverage area
    for idx in selected:
        x, y = candidates[idx]
        ax.scatter(x, y, c='green', s=80, edgecolors='black', label='Selected Sensor' if idx == selected[0] else "")
        circle = patches.Circle((x, y), coverage_radius, fill=False, color='blue', linestyle='--', alpha=0.5)
        ax.add_patch(circle)

    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, linestyle='--', alpha=0.4)
