import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Shor's Algorithm Probability Distribution", layout="wide", page_icon=":atom_symbol:")

# -------------------------
# Mathematical functions
# -------------------------
def residue_mod_q(x, q):
    x_mod = x % q
    if x_mod > q / 2:
        x_mod -= q
    return x_mod

def P_shor_vectorized(c, r, q):
    """
    Fully vectorized computation of the Shor probability distribution term.
    Much faster than looping or using generators.
    """
    Rc = residue_mod_q(r * c, q)
    B = (q - 1) // r

    # Vector b = [0, 1, ..., B]
    b = np.arange(B + 1)

    # Compute sum(exp(2πi * Rc * b / q))
    expo = np.exp(2j * np.pi * Rc * b / q)
    S = expo.sum()

    return (1 / q) * abs(S)**2

# -------------------------
# Sidebar (Controls)
# -------------------------
st.sidebar.header("Parameters")
t = st.sidebar.slider("t (qbits 1st register)", min_value=4, max_value=14, value=8)
r = st.sidebar.slider("r (period)", min_value=2, max_value=60, value=10)

# Default = Bars
style = st.sidebar.selectbox("Plot style", ["Bars", "Line"], index=0)

# -------------------------
# Title
# -------------------------
st.title("Probability Distribution of Measuring k in QPE Shor's Algorithm")

# -------------------------
# Computation
# -------------------------
q = 2**t
P_raw = np.array([P_shor_vectorized(c, r, q) for c in range(q)])
P = P_raw / np.sum(P_raw)

# -------------------------
# Plot
# -------------------------
fig, ax = plt.subplots(figsize=(12, 5))

if style == "Line":
    ax.plot(range(q), P, linewidth=1)
else:
    ax.bar(range(q), P, width=1.0)

ax.set_xlabel("k")
ax.set_ylabel("P(k)")
ax.grid(alpha=0.3)

st.pyplot(fig)
