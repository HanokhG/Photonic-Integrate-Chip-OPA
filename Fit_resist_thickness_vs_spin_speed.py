import matplotlib
matplotlib.use('TkAgg')  # Enable interactive plotting backend

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# -------------------
# Experimental data: spin speed vs. resist thickness (CSAR)
# -------------------
spin_speed = np.array([1150, 1200, 1250, 1300, 1350, 1400, 1450])  # in rpm
thickness = np.array([401.12, 390.94, 384.78, 383.24, 375.71, 365.57, 367.05])  # in nm

# -------------------
# Define power-law model: thickness = a * speed^b
# -------------------
def power_law(x, a, b):
    return a * np.power(x, b)

# -------------------
# Fit the power-law model to the data
# -------------------
params, covariance = curve_fit(power_law, spin_speed, thickness)
a_fit, b_fit = params

# -------------------
# Generate a smooth curve for visualization
# -------------------
spin_speed_smooth = np.linspace(spin_speed.min(), spin_speed.max(), 300)
thickness_smooth = power_law(spin_speed_smooth, a_fit, b_fit)

# -------------------
# Plot raw data and fitted curve
# -------------------
plt.figure(figsize=(8, 6))
plt.plot(spin_speed, thickness, '.', label='Measured Data')
plt.plot(spin_speed_smooth, thickness_smooth, '-',
         label=fr'$y = {a_fit:.2f} \cdot x^{{{b_fit:.2f}}}$')  # LaTeX-style equation

plt.xlabel('Spin Speed (rpm)', fontsize=12)
plt.ylabel('Resist Thickness (nm)', fontsize=12)
plt.title('CSAR Resist Thickness vs. Spin Speed', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
