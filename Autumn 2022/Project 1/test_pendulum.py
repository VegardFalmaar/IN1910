import pytest
import numpy as np

import ode
import pendulum


@pytest.mark.parametrize(
    'theta, omega, correct',
    [(np.pi/6, 0.35, (0.35, -9.81/1.42*0.5)), (.0, .0, (.0, .0))]
)
def test_pendulum_EOMs(theta, omega, correct):
    eps = 1E-14
    L = 1.42
    t = 123.0   # arbitrary
    de = pendulum.Pendulum(L)
    res = de(t, np.array([theta, omega]))
    assert abs(res[0] - correct[0]) < eps
    assert abs(res[1] - correct[1]) < eps


def test_solve_pendulum_ode_with_zero_ic():
    model = pendulum.Pendulum()
    u0 = np.zeros(2)
    T = 10.0
    dt = 0.01
    sol = ode.solve_ode(model, u0, T, dt)
    assert np.all(sol.solution == 0.0)


@pytest.mark.parametrize('L', [1.0, 2.0, 3.0])
def test_solve_pendulum_function_zero_ic(L):
    u0 = np.zeros(2)
    T = 10.0
    model = pendulum.Pendulum(L=L)
    sol = pendulum.solve_pendulum(u0, T, pendulum=model)
    assert np.all(sol.theta == 0.0)
    assert np.all(sol.omega == 0.0)
    assert np.all(sol.x == 0.0)
    assert np.all(sol.y == -L)
