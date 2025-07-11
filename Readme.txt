# Photonic-Integrate-Chip-OPA

This repository contains all design and data processing code related to a photonic integrated chip for Optical Phased Array (OPA) research.

## 📁 Branch Overview

### 1. `fabrication` Branch (Chip Design and Pattern Generation)

This branch focuses on photonic chip fabrication workflows. It includes:
- **EBL (Electron Beam Lithography)** pattern generation.
- Python scripts for **custom photonic structure design**.
- Tools for generating GDSII-compatible layouts for nanofabrication.

📌 Tools used:
- KLayout / GDSWriter for layout generation
- NumPy, matplotlib for structure shaping
- EBL pattern optimization for minimum feature size

### 2. `measurement` Branch (Data Processing and Analysis)

This branch contains code used after chip fabrication:
- Processing raw measurement data (e.g. optical spectra, interference patterns)
- Plotting and fitting of experimental results
- Streamlit / Jupyter-based visualization tools

📌 Functions include:
- Effective index sweep and intensity plotting
- Spectral peak analysis
- Phase shift / interference analysis
