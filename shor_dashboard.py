import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Shor's Algorithm Probability Distribution",
                   layout="wide",
                   page_icon=":atom_symbol:")

# -----------------------------------------------------
# Mathematical functions
# -----------------------------------------------------
def residue_mod_q(x, q):
    x_mod = x % q
    if x_mod > q / 2:
        x_mod -= q
    return x_mod

def P_shor_vectorized(c, r, q):
    """
    Fully vectorized computation of the Shor probability distribution term.
    """
    Rc = residue_mod_q(r * c, q)
    B = (q - 1) // r

    b = np.arange(B + 1)

    expo = np.exp(2j * np.pi * Rc * b / q)
    S = expo.sum()

    return (1 / q) * abs(S)**2


# -----------------------------------------------------
# Sidebar controls
# -----------------------------------------------------
st.sidebar.header("Parameters")
t = st.sidebar.slider("t (qbits 1st register)", min_value=4, max_value=14, value=8)
r = st.sidebar.slider("r (period)", min_value=2, max_value=60, value=10)

style = st.sidebar.selectbox("Plot style", ["Bars", "Line"], index=0)

# -----------------------------------------------------
# Title
# -----------------------------------------------------
st.title("Probability Distribution of Measuring k in QPE (Shor's Algorithm)")


# -----------------------------------------------------
# Computation
# -----------------------------------------------------
q = 2**t
P_raw = np.array([P_shor_vectorized(c, r, q) for c in range(q)])
P = P_raw / np.sum(P_raw)


# -----------------------------------------------------
# Plotly figure
# -----------------------------------------------------
fig = go.Figure()

if style == "Line":
    fig.add_trace(go.Scatter(
        x=list(range(q)),
        y=P,
        mode="lines",
        line=dict(width=1)
    ))
else:
    fig.add_trace(go.Bar(
        x=list(range(q)),
        y=P,
        marker=dict(line=dict(width=0)),
    ))

fig.update_layout(
    width=1200,
    height=500,
    xaxis_title="k",
    yaxis_title="P(k)",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
