import matplotlib
matplotlib.use('TkAgg')  # Ensure plot window pops up

import matplotlib.pyplot as plt
import numpy as np

# -------------------
# Step 1: Load the Element Factor (EF) data
# -------------------
ef_raw = np.loadtxt("1.txt")  # ← Replace with your EF data file

# Map pixel_x nonlinearly to angle (from -1 to 1 → arcsin in degrees)
N_pts = len(ef_raw)
pixel_x = np.linspace(-1, 1, N_pts)
theta_ef = np.rad2deg(np.arcsin(pixel_x))  # Angle from -90° to +90°

# -------------------
# Step 2: Interpolate EF to a high-resolution angle grid
# -------------------
theta_highres = np.linspace(-20, 20, 10000)  # Angle range in degrees
ef_interp = np.interp(theta_highres, theta_ef, ef_raw)
ef_interp /= np.max(ef_interp)  # Normalize EF

# -------------------
# Step 3: Compute the Array Factor (AF) for 1D OPA
# -------------------
N = 64                    # Number of antenna elements
d = 5e-6                  # Element spacing (meters)
wavelength = 905e-9       # Operating wavelength (meters)
n_eff = 1.8375            # Effective index of waveguide
delta_L = 76.436e-6       # Phase delay (meters)

# Total phase shift from path length difference
delta_phi_total = (2 * np.pi / wavelength) * n_eff * delta_L
delta_phi_eff = np.mod(delta_phi_total, 2 * np.pi)  # Wrap phase into 2π

# Compute AF pattern
theta_rad = np.deg2rad(theta_highres)
psi = 2 * np.pi * d / wavelength * np.sin(theta_rad) - delta_phi_eff
AF = np.abs(np.sin(N * psi / 2) / (N * np.sin(psi / 2)))
AF = np.nan_to_num(AF)  # Replace NaNs with 0
AF /= np.max(AF)        # Normalize AF

# -------------------
# Step 4: Combine EF and AF² for total far-field pattern
# -------------------
total = ef_interp * AF**2
total /= np.max(total)  # Normalize total intensity

# -------------------
# Step 5: Plot the far-field result
# -------------------
plt.figure(figsize=(8, 5))
plt.plot(theta_highres, 20 * np.log10(total + 1e-12), label="EF × AF²", linewidth=2)
plt.xlabel('Angle (degrees)')
plt.ylabel('Normalized Intensity (dB)')
plt.title("Simulated Far-Field of 1D Optical Phased Array")
plt.xlim(-20, 20)
plt.ylim(-80, 0)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
