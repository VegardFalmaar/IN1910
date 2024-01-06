import numpy as np
import pytest

import ode
from double_pendulum import DoublePendulum, solve_double_pendulum


def test_derivatives_at_rest_is_zero():
    model = DoublePendulum()
    t = 123.0   # arbitrary
    u = np.zeros(4)
    assert np.all(model(t, u) == 0.0)


@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0),
        (0, 0.5, 3.386187037),
        (0.5, 0, -7.678514423),
        (0.5, 0.5, -4.703164534),
    ],
)
def test_domega1_dt(theta1, theta2, expected):
    model = DoublePendulum()
    t = 0
    y = (theta1, 0.25, theta2, 0.15)
    dtheta1_dt, domega1_dt, _, _ = model(t, y)
    assert np.isclose(dtheta1_dt, 0.25)
    assert np.isclose(domega1_dt, expected)


@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0.0),
        (0, 0.5, -7.704787325),
        (0.5, 0, 6.768494455),
        (0.5, 0.5, 0.0),
    ],
)
def test_domega2_dt(theta1, theta2, expected):
    model = DoublePendulum()
    t = 0
    y = (theta1, 0.25, theta2, 0.15)
    _, _, dtheta2_dt, domega2_dt = model(t, y)
    assert np.isclose(dtheta2_dt, 0.15)
    assert np.isclose(domega2_dt, expected)


def test_solve_pendulum_ode_with_zero_ic():
    model = DoublePendulum()
    u0 = np.zeros(4)
    T = 10.0
    dt = 0.01
    sol = ode.solve_ode(model, u0, T, dt)
    assert np.all(sol.solution == 0.0)


@pytest.mark.parametrize('L1', [1.0, 2.0, 3.0])
@pytest.mark.parametrize('L2', [1.0, 2.0, 3.0])
def test_solve_double_pendulum_function_zero_ic(L1, L2):
    u0 = np.zeros(4)
    T = 10.0
    model = DoublePendulum(L1=L1, L2=L2)
    sol = solve_double_pendulum(u0, T, pendulum=model)
    assert np.all(sol.theta1 == 0.0)
    assert np.all(sol.omega1 == 0.0)
    assert np.all(sol.theta2 == 0.0)
    assert np.all(sol.omega2 == 0.0)
    assert np.all(sol.x1 == 0.0)
    assert np.all(sol.y1 == -L1)
    assert np.all(sol.x2 == 0.0)
    assert np.all(sol.y2 == -L1 - L2)
