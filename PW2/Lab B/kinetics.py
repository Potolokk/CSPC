"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1) 
t_data = data[:, 0]
C_data = data[:, 1]

C0 = C_data[0]

def error(k):
    C_model = C0 * np.exp(-k * t_data)
    return np.sum((C_data - C_model)**2)

res = minimize(error, x0=0.5, method="SLSQP", bounds=[(0, 5)])
k_fitted = res.x[0]

print(f"Fitted k :{k_fitted:.4f}")

plt.figure(figsize=(8, 5))
plt.scatter(t_data, C_data, color='red', label='Measured Data')
t_dense = np.linspace(min(t_data), max(t_data), 100)
plt.plot(t_dense, C0 * np.exp(-k_fitted * t_dense), label=f'Fit (k = {k_fitted:.3f})', color='blue')
plt.xlabel('Time (t)')
plt.ylabel('Concentration (C)')
plt.title('Reaction Kinetics Fitting')
plt.legend()
plt.grid(True)
plt.savefig('kinetics.png')
plt.show()