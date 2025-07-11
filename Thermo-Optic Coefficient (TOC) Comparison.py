import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend to ensure plots display as popups

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Labels and corresponding data files
labels = ["SiN", "30nm", "50nm", "70nm", "Patterned"]
files = {
    "SiN": "SiN.txt",
    "30nm": "TiO2_30.txt",
    "50nm": "TiO2_50.txt",
    "70nm": "TiO2_70.txt",
    "Patterned": "TiO2P.txt"
}

# Custom colors for each structure
colors = ["red", "blue", "green", "orange", "black"]

# Store fitted TOC (dn_eff/dT) values
slopes = []

# Compute TOC for each structure
for label in labels:
    df = pd.read_csv(files[label])
    df.columns = ["Temperature", "n_eff"]
    slope = np.polyfit(df["Temperature"], df["n_eff"], 1)[0]
    slopes.append(slope)

# Print TOC values
print("Thermo-optic coefficients (TOC):")
for lbl, s in zip(labels, slopes):
    print(f"{lbl}: dn_eff/dT = {s:.2e} 1/K")

# Plot TOC values as a bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(labels, slopes, color=colors)

# Annotate bars with slope values
for bar, s in zip(bars, slopes):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
             f"{s:.1e}", ha='center', va='bottom', fontsize=10)

plt.xlabel("Structure")
plt.ylabel("dn_eff / dT (1/K)")
plt.title("Thermo-Optic Coefficient (TOC) Comparison")
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
