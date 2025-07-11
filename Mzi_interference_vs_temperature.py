import matplotlib
matplotlib.use('TkAgg')  # Enable interactive plot window

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# -------------------
# Parameters
# -------------------
delta_L = 9.4e-6  # Optical path difference (in meters), 9.4 μm
wavelength = np.linspace(850e-9, 950e-9, 1000)  # Wavelength range in meters

# Initial effective index (corresponding to a reference temperature, e.g., 280 K)
initial_n = 1.78022

# -------------------
# Interference function for MZI
# -------------------
def compute_intensity(n_eff):
    OPD = n_eff * delta_L  # Optical Path Difference
    return 0.5 * (1 + np.cos(2 * np.pi * OPD / wavelength))  # Normalized intensity

# -------------------
# Plot initialization
# -------------------
fig, ax = plt.subplots(figsize=(8, 5))
plt.subplots_adjust(bottom=0.25)  # Leave space for the slider

intensity = compute_intensity(initial_n)
[line] = ax.plot(wavelength * 1e9, intensity, linewidth=2, label='SiN')  # x-axis in nm

ax.set_xlabel('Wavelength (nm)', fontsize=12)
ax.set_ylabel('Normalized Intensity', fontsize=12)
ax.legend()
ax.grid(True)

# -------------------
# Slider for varying n_eff
# -------------------
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
n_slider = Slider(
    ax=ax_slider,
    label=r'$n_{\mathrm{eff}}$',
    valmin=1.6989,
    valmax=1.70427,
    valinit=initial_n,
    valstep=0.0001
)

# -------------------
# Update function for interactive slider
# -------------------
def update(val):
    n = n_slider.val
    new_intensity = compute_intensity(n)
    line.set_ydata(new_intensity)
    fig.canvas.draw_idle()

n_slider.on_changed(update)

# -------------------
# Show interactive plot
# -------------------

plt.show()
