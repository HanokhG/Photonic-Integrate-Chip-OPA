README - Integrated Photonics Layout & Simulation Toolkit
=========================================================

This repository includes Python scripts and GDSII files related to photonic integrated circuits (PICs), focused on:
- 1D Optical Phased Array (OPA) based on MMI trees
- Thermo-optic interference analysis
- Waveguide loss characterization
- GDS layout generation for Electron Beam Lithography (EBL)

Repository Structure
---------------------

📁 Branch: Simulation-and-Data-process
--------------------------------------
This branch contains simulation and data fitting scripts, as well as raw and processed measurement data.

🔹 Python Scripts:
- **Bent-Loss-Measurement.py**  
  Fit the propagation loss induced by waveguide bends.

- **Straight-Loss-Measurement.py**  
  Extract straight waveguide loss from measured transmission.

- **Mzi_interference_vs_temperature.py**  
  Simulate how interference fringes shift with temperature in a Mach-Zehnder Interferometer.

- **Fit_resist_thickness_vs_spin_speed.py**  
  Fit spin-coating data to predict resist thickness under different spin speeds.

- **Simulate_1d_opa_farfield.py**  
  Generate the far-field pattern of a 1D OPA array with arbitrary phase and spacing.

- **Thermo-Optic Coefficient (TOC) Comparison.py**  
  Analyze dn/dT of TiO₂/SiN hybrid waveguides and compare TOC for design optimization.

🔹 Data Files:
- **SiN.txt** — Effective index vs temperature for SiN
- **TiO2P.txt**, **TiO2_30.txt**, **TiO2_50.txt**, **TiO2_70.txt** — TOC measurements of TiO₂ claddings (various thicknesses)

🔹 Dependency File:
- **requirements.txt** — Python packages required (e.g., `matplotlib`, `numpy`, `scipy`, `pandas`)

📁 Branch: EBL-pattern
-----------------------
This branch is focused on GDS layout generation using [gdsfactory](https://github.com/gdsfactory/gdsfactory).

🔹 Layout Scripts:
- **Layout for 1D Optical Phased Array.py**  
  GDS generator for a hierarchical 1D OPA structure (MMI tree + delay lines + tapers). Output: `YNmmi10.gds`

- **Layout for MZI.py**  
  Layout generator for a Mach-Zehnder Interferometer with long/short arms. Output: `YNmzi09.gds`

- **Bent and Straight Layout for Loss Measurement.py**  
  Includes bent waveguides with multiple radii and straight reference waveguides. Output: `YNbend07.gds`

🔹 GDS Outputs:
- **YNmmi10.gds** — Final OPA array layout with 64 output ports and variable delays
- **YNmzi09.gds** — MZI layout for thermo-optic tuning test
- **YNbend07.gds** — Contains several bent and straight segments for waveguide loss calibration

🔹 requirements.txt  
Layout scripts require:  
- `gdsfactory` (v7+ recommended)  
- `matplotlib`, `numpy`

Getting Started
----------------

1. **Install Python Requirements**  
   ```bash
   pip install -r requirements.txt
