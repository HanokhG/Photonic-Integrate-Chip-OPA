
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Convert to radians for x-axis
angle_radians = np.array([0, np.pi, 2*np.pi])

# Averaged losses
avg_losses = np.array([
    np.mean([-24.23, -23.57]),
    np.mean([-24.89, -24.21]),
    np.mean([-24.28, -24.97])
])

# Original data for plotting range bars
loss_data = {
    0: [-24.23, -23.57],
    np.pi: [-24.89, -24.21],
    2*np.pi: [-24.28, -24.97]
}

# Linear regression (fit)
slope, intercept, r_value, p_value, std_err = linregress(angle_radians, avg_losses)
fit_line = slope * angle_radians + intercept

# Plotting
plt.figure(figsize=(6, 4))
for angle, losses in loss_data.items():
    plt.plot([angle, angle], losses, '.--', color='steelblue', linewidth=1.2)

plt.plot(angle_radians, avg_losses, '.', color='black')
plt.plot(angle_radians, fit_line, '-', color='orange', label=f'Fit: {-slope:.2f} dB/rad')

# Set custom ticks as 0, π, 2π
plt.xticks(angle_radians, [r'$1\pi$', r'$2\pi$', r'$3\pi$'])
plt.xlabel('Bend Angle (rad)')
plt.ylabel('Measured power (dBm)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.ylim(-26, -22)

plt.tight_layout()
plt.show()
