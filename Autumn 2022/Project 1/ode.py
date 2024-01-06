import abc
from typing import NamedTuple, Optional, List

import numpy as np
import matplotlib.pyplot as plt         # type: ignore
from scipy.integrate import solve_ivp   # type: ignore


class InvalidInitialConditionError(RuntimeError):
    pass


class ODEModel(abc.ABC):
    @abc.abstractmethod
    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def verify_number_of_inputs(self, u: np.ndarray) -> None:
        if not len(u) == self.num_states:
            msg = f'Length of initial value {len(u)} does not match '
            msg += f'num_states {self.num_states}'
            raise InvalidInitialConditionError(msg)

    @property
    def num_states(self) -> int:
        raise NotImplementedError


class ODEResult(NamedTuple):
    time: np.ndarray
    solution: np.ndarray

    @property
    def num_states(self):
        return self.solution.shape[0]

    @property
    def num_timepoints(self):
        return self.solution.shape[1]


def solve_ode(
    model: ODEModel,
    u0: np.ndarray,
    T: float,
    dt: float,
) -> ODEResult:
    t = np.arange(0, T + 0.5*dt, dt)
    sol = solve_ivp(model, (0, T + dt), u0, t_eval=t, method='Radau')
    res = ODEResult(sol.t, sol.y)
    return res


def plot_ode_solution(
    results: ODEResult,
    state_labels: Optional[List[str]] = None,
    filename: Optional[str] = None,
) -> None:
    fig, ax = plt.subplots()
    if state_labels is None:
        state_labels = [f'State {i+1}' for i in range(results.num_states)]
    for label, res in zip(state_labels, results.solution):
        ax.plot(results.time, res, label=label)
    ax.legend()
    ax.grid(True)
    ax.set_xlabel('Time')
    ax.set_ylabel('ODE Solution')
    if filename is None:
        plt.show()
    else:
        fig.savefig(filename)
        plt.close(fig)
