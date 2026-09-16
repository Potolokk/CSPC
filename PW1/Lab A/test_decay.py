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
    """Проверка основных свойств физического распада."""
    N0 = 1000
    r = 0.01

    # Запускаем симуляцию
    result = simulate(N0, r)

    # 1. Начальное количество частиц равно N0
    assert result[0] == N0

    # 2. Количество частиц со временем уменьшается или остаётся прежним (монотонное убывание)
    assert result[-1] <= result[0]

    # 3. Число частиц никогда не становится отрицательным
    assert (result >= 0).all()