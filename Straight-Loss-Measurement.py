import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for interactive plots

# ----------------------------
# Waveguide length (in micrometers)
# ----------------------------
lengths_um = np.array([0, 6000, 12000, 18000])

# Total bend angle per structure (in radians)
bend_angles_rad = np.array([0*np.pi, 2*np.pi, 3*np.pi, 4*np.pi])

# Loss per bend radian (in dB/rad)
bend_loss_per_rad = 0.12

# Raw measurement data (in dB) for each structure
raw_measurements = {
    0: [-24.23, -23.57],
    6000: [-26.31, -26.86],
    12000: [-29.54],
    18000: [-28.81, -29.13]
}

# Compute average measured loss per group
measured_losses_db = np.array([np.mean(raw_measurements[length]) for length in lengths_um])

# Calculate bend loss for each structure
bend_losses_db = bend_angles_rad * bend_loss_per_rad

# Subtract bend losses to isolate straight waveguide loss
straight_only_losses_db = measured_losses_db - bend_losses_db

# Linear fit to extract propagation loss (dB/µm → dB/cm)
slope, intercept = np.polyfit(lengths_um, straight_only_losses_db, 1)
fit_line = slope * lengths_um + intercept
propagation_loss_dB_per_cm = slope * 1e4

# ----------------------------
# Plotting
# ----------------------------
plt.figure(figsize=(6, 4))

# Plot raw data points with vertical dotted lines for error bars
for i, length in enumerate(lengths_um):
    bend_loss = bend_angles_rad[i] * bend_loss_per_rad
    losses = raw_measurements[length]
    corrected_losses = np.array(losses) - bend_loss
    if len(corrected_losses) == 2:
        plt.plot([length, length], corrected_losses, '.--', color='steelblue', linewidth=1.2)
    else:
        plt.plot(length, corrected_losses[0], '.', color='steelblue')

# Plot average corrected values and fitted line
plt.plot(lengths_um, straight_only_losses_db, 'k.', label='Average (bend-corrected)')
plt.plot(lengths_um, fit_line, 'r-', label=f'Fit: {abs(propagation_loss_dB_per_cm):.2f} dB/cm')

# Beautify plot
plt.xlabel('Straight Waveguide Length (µm)', fontsize=12)
plt.ylabel('Measured Power (dBm, bend-corrected)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.title('Waveguide Propagation Loss Fit', fontsize=13)
plt.show()
