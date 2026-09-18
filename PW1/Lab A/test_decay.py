import numpy as np
import pytest
from decay import simulate


def test_starts_at_N0():
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)


def test_matches_law():
    N0 = 50000
    lam = 0.1
    dt = 0.05
    steps = 100

    simulated = simulate(N0, lam, dt=dt, steps=steps)

    t = np.arange(steps + 1) * dt
    analytical = N0 * np.exp(-lam * t)

    np.testing.assert_allclose(simulated, analytical, rtol=0.05)