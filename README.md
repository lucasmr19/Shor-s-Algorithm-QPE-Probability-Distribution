# Shor's Algorithm QPE Probability Distribution

This Streamlit app visualizes the probability distribution of measuring a value **k** in the first register of Shor’s algorithm **after the Quantum Fourier Transform (QFT)**, i.e., the output of the quantum phase estimation (QPE) step.

The plot shows

$$
P(k) = \frac{1}{q} \left| \sum_{b=0}^{\lfloor (q-1)/r \rfloor} 
e^{2\pi i \, rkc / q} \right|^2,
$$

where  
- $t$ = number of qubits in the first register,  
- $q = 2^t$,  
- $r$ = period of the modular multiplication function.

The app allows interactive adjustment of parameters $ t $ and $ r $, and displays the resulting probability distribution either as a bar plot or line plot.

---

## 🚀 Online App (Streamlit Cloud)

The app is live and accessible at:

[https://shor-qpe-distribution.streamlit.app/](https://shor-qpe-distribution.streamlit.app/)

---

## 📦 Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/lucasmr19/Shor-s-Algorithm-QPE-Probability-Distribution
cd Shor-s-Algorithm-QPE-Probability-Distribution
pip install -r requirements.txt
````

---

## ▶️ Running locally

Run the app with:

```bash
streamlit run shor_dashboard.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 📁 Project Structure

```
.
├── shor_dashboard.py
├── requirements.txt
└── README.md
```

---

## ✨ Features

✔ Interactive sliders for **t** (first register qubits) and **r** (period)
✔ Bar or line plot
✔ Fully vectorized and optimized computation
✔ Suitable for teaching Shor’s algorithm
✔ Ready for Streamlit Cloud deployment

---

## 📄 License

[MIT License]
