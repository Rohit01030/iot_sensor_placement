# iot_sensor_placement
A Python + Streamlit project demonstrating Greedy and Energy-Aware algorithms for optimal IoT sensor placement. It applies facility location and approximation techniques to minimize sensors and energy use while ensuring full coverage, visualized interactively in real time.

# 📡 IoT Sensor Placement Optimization – Facility Location + Approximation (Energy-Aware Version)

This project demonstrates **approximation-based optimization algorithms** for efficient IoT sensor placement.  
It compares **Greedy Set Cover** and **Energy-Aware Greedy** methods to minimize sensor count while maintaining full coverage and optimizing energy usage.

---

## 🧠 Project Overview

With the rapid growth of the **Internet of Things (IoT)**, millions of sensors are deployed for applications like smart cities, environmental monitoring, and industrial automation.  
However, deploying too many sensors increases cost and energy consumption.  
This project models the placement problem as a **Facility Location Problem (FLP)** and applies **approximation algorithms** to achieve energy-efficient and cost-effective coverage.

---

## 🚀 Features

- Greedy and Energy-Aware Greedy algorithms implemented in Python  
- Interactive web visualization using **Streamlit**  
- Adjustable parameters (targets, sensors, coverage radius)  
- Real-time visualization of sensor coverage  
- Comparison of performance metrics (coverage, cost, and runtime)

---

## 🧩 Algorithms Used

### 1. Greedy Set Cover Algorithm  
- Selects sensors that cover the maximum number of uncovered targets.  
- Ensures full coverage with the fewest sensors.  

### 2. Energy-Aware Greedy Algorithm  
- Considers both coverage and energy cost.  
- Balances efficiency and energy consumption.  
- Results in slightly higher sensor count but lower total cost.

---

## 🖼️ Visualization Example

Two plots are displayed side-by-side:
- **Left:** Greedy Algorithm coverage  
- **Right:** Energy-Aware Greedy Algorithm coverage  

Each plot shows:  
🔴 *Targets (IoT nodes)*  
🟢 *Selected Sensors*  
🔵 *Coverage Areas (radius)*  

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| Programming Language | Python 3 |
| Web Framework | Streamlit |
| Visualization | Matplotlib |
| Libraries | NumPy, Random, Math |

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/iot_sensor_placement.git
cd iot_sensor_placement

