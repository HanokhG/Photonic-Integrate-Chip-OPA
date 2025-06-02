import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 标题
st.title("Interference Pattern vs. Effective Index")

# 参数定义
delta_L = 9.4e-6  # 9.4 μm
wavelength = np.linspace(850e-9, 950e-9, 1000)

# 用户滑块选择 n_eff
n_eff = st.slider(
    r"Effective Index $n_{\mathrm{eff}}$",
    min_value=1.6989,
    max_value=1.70427,
    value=1.78022,
    step=0.0001
)

# 干涉函数
def compute_intensity(n_eff):
    OPD = n_eff * delta_L
    return 0.5 * (1 + np.cos(2 * np.pi * OPD / wavelength))

# 计算干涉强度
intensity = compute_intensity(n_eff)

# 画图
fig, ax = plt.subplots()
ax.plot(wavelength * 1e9, intensity, label=f"$n_{{eff}}$ = {n_eff:.5f}")
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Normalized Intensity")
ax.set_title("Interference Pattern")
ax.grid(True)
ax.legend()

st.pyplot(fig)
