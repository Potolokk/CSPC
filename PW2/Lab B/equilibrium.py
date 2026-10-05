"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
def k_imbalance(x):
    return (2 * x)**2 / ((a - x) * (b - x)) - K

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance (start x0=0.5).
x_newton = newton(k_imbalance, x0=0.5)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
def k_imbalance_sq(x):
    x_val = x[0] if isinstance(x, (list, np.ndarray)) else x
    return k_imbalance(x_val)**2

res_slsqp = minimize(k_imbalance_sq, x0=[0.5], method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res_slsqp.x[0]

print(f"Equilibrium x (Newton): {x_newton:.4f}")
print(f"Equilibrium x (SLSQP):  {x_slsqp:.4f}")

# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three amounts change.
nH2_eq = a - x_newton
nI2_eq = b - x_newton
nHI_eq = 2 * x_newton

print(f"\nEquilibrium amounts:")
print(f"H2: {nH2_eq:.4f} mol")
print(f"I2: {nI2_eq:.4f} mol")
print(f"HI: {nHI_eq:.4f} mol")

x_vals = np.linspace(0, 0.99, 200)
nH2_vals = a - x_vals
nI2_vals = b - x_vals
nHI_vals = 2 * x_vals

plt.figure(figsize=(8, 5))
plt.plot(x_vals, nH2_vals, label='H2', color='blue')
plt.plot(x_vals, nI2_vals, label='I2', linestyle='--', color='cyan')
plt.plot(x_vals, nHI_vals, label='HI', color='red')

plt.axvline(x=x_newton, color='green', linestyle=':', label=f'Equilibrium x = {x_newton:.3f}')
plt.scatter([x_newton]*3, [nH2_eq, nI2_eq, nHI_eq], color='green', zorder=5)

plt.xlabel('Extent of reaction (x)')
plt.ylabel('Amount (mol)')
plt.title('Chemical Equilibrium (H2 + I2 <=> 2 HI)')
plt.legend()
plt.grid(True)

plt.savefig('equilibrium.png')
plt.show()