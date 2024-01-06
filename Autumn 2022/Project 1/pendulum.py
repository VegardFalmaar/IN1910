from typing import Optional
from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt     # type: ignore

import ode


class Pendulum(ode.ODEModel):
    def __init__(self, L: Optional[float] = 1.0, g: Optional[float] = 9.81):
        self.L = L
        self.g = g

    @property
    def num_states(self) -> int:
        return 2

    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        self.verify_number_of_inputs(u)
        theta, omega = u
        der_theta = omega
        der_omega = -self.g / self.L * np.sin(theta)
        return np.array([der_theta, der_omega])


class DampenedPendulum(Pendulum):
    def __init__(
        self,
        L: Optional[float] = 1.0,
        g: Optional[float] = 9.81,
        B: Optional[float] = 1.0,
    ):
        super().__init__(L, g)
        self.B = B

    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        der = super().__call__(t, u)
        der[1] -= self.B*u[1]
        return der


def exercise_2b():
    model = Pendulum()
    u0 = np.array([np.pi / 6, 0.35])
    T = 10.0
    dt = 0.01
    sol = ode.solve_ode(model, u0, T, dt)
    ode.plot_ode_solution(
        sol,
        state_labels=[r"$\theta$", r"$\omega$"],
        filename="output/exercise_2b.png"
    )


@dataclass
class PendulumResults:
    results: ode.ODEResult
    pendulum: Pendulum

    @property
    def theta(self) -> np.ndarray:
        return self.results.solution[0]

    @property
    def omega(self) -> np.ndarray:
        return self.results.solution[1]

    @property
    def x(self) -> np.ndarray:
        return self.pendulum.L * np.sin(self.theta)

    @property
    def y(self) -> np.ndarray:
        return -self.pendulum.L * np.cos(self.theta)

    @property
    def potential_energy(self) -> np.ndarray:
        return self.pendulum.g * (self.y + self.pendulum.L)

    @property
    def vx(self) -> np.ndarray:
        return np.gradient(self.x, self.results.time)

    @property
    def vy(self) -> np.ndarray:
        return np.gradient(self.y, self.results.time)

    @property
    def kinetic_energy(self) -> np.ndarray:
        return 0.5 * (self.vx ** 2 + self.vy ** 2)

    @property
    def total_energy(self):
        return self.potential_energy + self.kinetic_energy


def solve_pendulum(
    u0: np.ndarray,
    T: float,
    dt: float = 0.01,
    pendulum: Optional[Pendulum] = None
) -> PendulumResults:
    if pendulum is None:
        pendulum = Pendulum()
    sol = PendulumResults(ode.solve_ode(pendulum, u0, T, dt), pendulum)
    return sol


def plot_energy(
    results: PendulumResults,
    filename: Optional[str] = None
) -> None:
    fig, ax = plt.subplots()
    time = results.results.time
    ax.plot(time, results.potential_energy, label="Potential energy")
    ax.plot(time, results.kinetic_energy, label="Kinetic energy")
    ax.plot(time, results.total_energy, label="Total energy")
    ax.legend()
    ax.grid(True)
    ax.set_xlabel("Time")
    ax.set_ylabel("Energy")
    if filename is None:
        plt.show()
    else:
        fig.savefig(filename)
        plt.close(fig)


def exercise_2g():
    u0 = np.array([np.pi / 6, 0.35])
    T = 10.0
    dt = 0.01
    res = solve_pendulum(u0, T, dt)
    plot_energy(res, filename="output/energy_single.png")


def exercise_2h():
    u0 = np.array([np.pi / 6, 0.35])
    T = 10.0
    dt = 0.01
    model = DampenedPendulum()
    res = solve_pendulum(u0, T, dt, model)
    plot_energy(res, filename="output/energy_damped.png")


if __name__ == "__main__":
    exercise_2b()
    exercise_2g()
    exercise_2h()
