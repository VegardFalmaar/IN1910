import numpy as np

from ode import ODEModel, solve_ode, plot_ode_solution


class ExponentialDecay(ODEModel):
    def __init__(self, a: float):
        self.decay = a

    @property
    def decay(self):
        return self._decay

    @decay.setter
    def decay(self, a: float):
        if a < 0:
            raise ValueError(f'Decay constant a must be negative, not {a}')
        self._decay = a

    @property
    def num_states(self) -> int:
        return 1

    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        self.verify_number_of_inputs(u)
        return -self.decay*u


def solve_exponential_decay():
    ode = ExponentialDecay(0.4)
    u_0 = np.array([13.2])  # arbitrary initial value
    sol = solve_ode(ode, u_0, 10, 0.01)
    assert sol.time[1] - sol.time[0] == 0.01


if __name__ == '__main__':
    model = ExponentialDecay(0.4)
    result = solve_ode(model, u0=np.array([4.0]), T=10.0, dt=0.01)
    plot_ode_solution(
        results=result,
        state_labels=["u"],
        filename="output/exponential_decay.png"
    )
