import numpy as np
import matplotlib.pyplot as plt

# 1. Read decay_observed.csv (delimiter ',', skip header)
data = np.loadtxt('decay_observed.csv', delimiter=',', skiprows=1)
t = data[:, 0]
observed = data[:, 1]

# 2. Set N0 to the first observed value and build analytical law
LAMBDA = 0.3
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# 3. Make a 1x2 subplot with shared x and y axes
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))

# Left plot: Scatter of observed data
ax1.scatter(t, observed, color='blue', alpha=0.6, label='Observed')
ax1.set_title('Observed Data')
ax1.set_xlabel('Time (t)')
ax1.set_ylabel('Count (N)')
ax1.grid(True)

# Right plot: Line of analytical law
ax2.plot(t, analytical, color='red', label='Analytical')
ax2.set_title('Analytical Law')
ax2.set_xlabel('Time (t)')
ax2.grid(True)

plt.tight_layout()

# 4. Save the figure as figure.png
plt.savefig('figure.png')
print("Figure saved as figure.png")