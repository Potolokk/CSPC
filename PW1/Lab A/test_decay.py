"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    """Проверка, что отрицательный параметр lam вызывает ошибку ValueError."""
    with pytest.raises(ValueError):
        simulate(1000, -0.4)


def test_matches_law():
    """Проверка совпадения симуляции с физическим законом N0 * exp(-lam * t)."""
    N0 = 10000
    lam = 0.2
    steps = 5
    
    # Запускаем симуляцию
    result = simulate(N0, lam, steps)
    
    # Сравниваем полученные значения с экспоненциальным законом
    for t, N in enumerate(result):
        expected = N0 * np.exp(-lam * t)
        # pytest.approx позволяет сравнивать числа с плавающей точкой с погрешностью
        assert N == pytest.approx(expected, rel=0.1)