"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 
x_gd = 0.0
alpha = 0.1 
for _ in range(100):
    x_gd = x_gd - alpha * df(x_gd)
print(f"GD result: x = {x_gd:.4f}")

res_slsqp = minimize(f, x0=0.0, method="SLSQP")
print(f"SLSQP result: x = {res_slsqp.x[0]:.4f}")
# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

def run_2b(x0):
    print(f"\n--- Part 2B (x0 = {x0}) ---")
    
    # 1. GD
    x_gd = x0
    alpha = 0.01

    for _ in range(500):
        x_gd = x_gd - alpha * dg(x_gd)
    print(f"GD result: x = {x_gd:.4f}")

    
    x_newton = newton(dg, x0=x0, fprime=d2g)
    g2_val = d2g(x_newton)
    point_type = "Minimum" if g2_val > 0 else "Maximum"
    print(f"Newton result: x = {x_newton:.4f} (g'' = {g2_val:.2f} -> {point_type})")

    res = minimize(g, x0=x0, method="SLSQP")
    print(f"SLSQP result: x = {res.x[0]:.4f}")

run_2b(x0=0.0)
run_2b(x0=2.0)