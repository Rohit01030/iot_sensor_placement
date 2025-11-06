import streamlit as st
import matplotlib.pyplot as plt
from algorithms import greedy_set_cover, greedy_energy_aware
from utils import generate_targets, generate_candidates, compute_coverage
from visualize import plot_coverage


st.set_page_config(page_title="IoT Sensor Placement Optimization", layout="wide")

st.title("📡 IoT Sensor Placement Optimization – Facility Location + Approximation (Energy-Aware Version)")
st.markdown("This interactive web app demonstrates Greedy and Energy-Aware Greedy algorithms for optimal IoT sensor placement.")


# --- Input parameters ---
col1, col2, col3 = st.columns(3)
num_targets = col1.slider("Number of Targets", 5, 40, 15)
num_candidates = col2.slider("Number of Candidate Sensors", 5, 60, 25)
coverage_radius = col3.slider("Coverage Radius", 10.0, 100.0, 30.0)
seed = st.number_input("Random Seed", value=42, step=1)

# --- Run button ---
if st.button("🚀 Run Optimization"):
    # Generate synthetic data
    targets = generate_targets(num_targets, seed)
    candidates = generate_candidates(num_candidates, seed)
    coverage_map = compute_coverage(targets, candidates, coverage_radius)

    # Assign random energy costs for energy-aware version
    import numpy as np
    energy_costs = {i: np.random.uniform(1, 10) for i in range(len(candidates))}

    # Run Greedy Algorithm
    st.subheader("Greedy Algorithm")
    greedy_result = greedy_set_cover(set(range(len(targets))), coverage_map)
    st.write(f"✅ Sensors Selected: {len(greedy_result)}")
    st.write(f"🕒 Total Runtime: Very fast (O(n²))")

    # Run Energy-Aware Greedy Algorithm
    st.subheader("Energy-Aware Greedy Algorithm")
    energy_result = greedy_energy_aware(set(range(len(targets))), coverage_map, energy_costs)
    total_cost = sum(energy_costs[i] for i in energy_result)
    st.write(f"✅ Sensors Selected: {len(energy_result)}")
    st.write(f"⚡ Total Energy Cost: {total_cost:.2f}")

    # --- Visualization ---
    st.subheader("📊 Visualization Comparison")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    plot_coverage(targets, candidates, greedy_result, coverage_radius, axes[0], "Greedy Algorithm")
    plot_coverage(targets, candidates, energy_result, coverage_radius, axes[1], "Energy-Aware Greedy Algorithm")
    st.pyplot(fig)

    # --- Summary ---
    st.success("✅ Optimization complete! Check visual comparison and summary above.")
    st.markdown("""
    **Interpretation:**
    - The **Greedy algorithm** ensures full coverage with the fewest sensors.
    - The **Energy-Aware Greedy algorithm** may use slightly more sensors but optimizes for cost/energy efficiency.
    """)

else:
    st.info("👆 Adjust parameters and click 'Run Optimization' to begin.")
