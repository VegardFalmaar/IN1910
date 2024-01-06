from pathlib import Path

import pytest
import numpy as np

import exp_decay
import ode
from ode import InvalidInitialConditionError

eps = 1E-8


@pytest.mark.parametrize('a', [-0.01, -1.0, -15.3])
def test_negative_decay_raises_ValueError(a):
    with pytest.raises(ValueError):
        de = exp_decay.ExponentialDecay(a)
    with pytest.raises(ValueError):
        de = exp_decay.ExponentialDecay(0.4)
        de.decay = a


def test_ODE_RHS():
    de = exp_decay.ExponentialDecay(0.4)
    t = 0.0     # arbitrary
    u = np.array([3.2])
    assert abs(de(t, u)[0] - (-1.28)) < eps


def test_num_states_ExponentialDecay_is_one():
    model = exp_decay.ExponentialDecay(0.4)
    assert model.num_states == 1


def test_solve_with_different_number_of_initial_states():
    with pytest.raises(InvalidInitialConditionError):
        model = exp_decay.ExponentialDecay(0.4)
        t = 0.035
        u_0 = np.array([13.2, 4.1])
        model(t, u_0)


@pytest.mark.parametrize('a', [0.1, 0.3, 0.6, 1.1])
@pytest.mark.parametrize('init_val', [5.0, 3.0, 7.1, 11.2])
@pytest.mark.parametrize('T', [4, 7, 3, 5])
@pytest.mark.parametrize('dt', [0.01, 0.02, 0.04, 0.05])
def test_solve_time(a, init_val, T, dt):
    model = exp_decay.ExponentialDecay(a)
    u0 = np.array([init_val])
    res = ode.solve_ode(model, u0, T, dt)
    assert res.time[0] == 0.0
    assert res.time[-1] == T
    assert res.time[1] - res.time[0] == dt


@pytest.mark.parametrize('a', [0.1, 0.3, 0.6, 1.1])
@pytest.mark.parametrize('init_val', [5.0, 3.0, 7.1, 11.2])
@pytest.mark.parametrize('T', [4, 7, 3, 5])
@pytest.mark.parametrize('dt', [0.01, 0.02, 0.04, 0.05])
def test_solve_solution(a, init_val, T, dt):
    model = exp_decay.ExponentialDecay(a)
    u0 = np.array([init_val])
    res = ode.solve_ode(model, u0, T, dt)
    exact = init_val*np.exp(-a*np.arange(0, T + 0.5*dt, dt))
    max_rel_error = np.max(abs(res.solution[0] - exact)/exact)
    assert max_rel_error < 1E-2


def test_ODEResults():
    time = np.array([1, 2, 3])
    sol = np.array([[7, 2, 3], [9, 2, 2]])
    res = ode.ODEResult(time, sol)
    assert res.num_states == 2
    assert res.num_timepoints == 3


def test_plot_ode_solution_saves_file():
    # check if the file already exists and delete if necessary
    filename = Path('output/test_plot.png')
    if filename.is_file():
        filename.unlink()

    # call the function we are testing
    model = exp_decay.ExponentialDecay(0.4)
    result = ode.solve_ode(model, u0=np.array([4.0]), T=10.0, dt=0.01)
    ode.plot_ode_solution(
        results=result,
        state_labels=["u"],
        filename=filename
    )

    # check that the file has now been created, then delete it
    assert filename.is_file()
    filename.unlink()
