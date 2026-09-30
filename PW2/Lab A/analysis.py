import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

data = np.genfromtxt('freefall.csv', delimiter=',', skip_header=1)
t = data[:, 0]
y = data[:, 1]

v = np.gradient(y, t)  
a = np.gradient(v, t)

mean_a = np.mean(a)
std_a = np.std(a)

print(f"Mean Acceleration: {mean_a:.2f} m/s^2")
print(f"Standard Deviation of Acceleration: {std_a:.2f} m/s^2")

v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

max_diff = np.max(np.abs(y_rec - y))
print(f"Max difference between original and recovered position: {max_diff:.4f} m")


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

ax1.plot(t, y, label='Original Position (y)', color='blue')
ax1.set_ylabel('Position (m)')
ax1.set_title('Motion Analysis: Free Fall')
ax1.grid(True)
ax1.legend()

ax2.plot(t, v, label='Velocity (v)', color='orange')
ax2.set_ylabel('Velocity (m/s)')
ax2.grid(True)
ax2.legend()

ax3.plot(t, a, label='Measured Acceleration (a)', color='red', alpha=0.7)
ax3.axhline(-9.81, color='black', linestyle='--', label='Theoretical g (-9.81 m/s²)')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Acceleration (m/s²)')
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.savefig('motion.png')
plt.show()


try:
    traj_data = np.genfromtxt('trajectory.csv', delimiter=',', skip_header=1)
    t_2d = traj_data[:, 0]
    x_2d = traj_data[:, 1]
    y_2d = traj_data[:, 2]

    vx = np.gradient(x_2d, t_2d)
    vy = np.gradient(y_2d, t_2d)
    speed = np.sqrt(vx**2 + vy**2)

    fig_bonus, (ax_path, ax_speed) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax_path.plot(x_2d, y_2d, color='purple')
    ax_path.set_xlabel('X (m)')
    ax_path.set_ylabel('Y (m)')
    ax_path.set_title('2D Path (x vs y)')
    ax_path.grid(True)

    ax_speed.plot(t_2d, speed, color='green')
    ax_speed.set_xlabel('Time (s)')
    ax_speed.set_ylabel('Speed (m/s)')
    ax_speed.set_title('Speed over Time')
    ax_speed.grid(True)

    plt.tight_layout()
    plt.savefig('trajectory_2d.png')
except OSError:
    pass