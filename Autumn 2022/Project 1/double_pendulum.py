from typing import Optional
from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt     # type: ignore
from matplotlib import animation    # type: ignore

import ode
from pendulum import plot_energy


class DoublePendulum(ode.ODEModel):
    def __init__(
        self,
        L1: Optional[float] = 1.0,
        L2: Optional[float] = 1.0,
        g: Optional[float] = 9.81
    ):
        self.L1 = L1
        self.L2 = L2
        self.g = g

    @property
    def num_states(self) -> int:
        return 4

    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        self.verify_number_of_inputs(u)
        _, omega1, _, omega2 = u
        dtheta1_dt = omega1
        domega1_dt = self.domega1_dt(u)
        dtheta2_dt = omega2
        domega2_dt = self.domega2_dt(u)
        return np.array([dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt])

    def domega1_dt(self, u: np.ndarray) -> float:
        theta1, omega1, theta2, omega2 = u
        del_th = theta2 - theta1
        L1, L2, g = self.L1, self.L2, self.g
        t1 = L1 * omega1**2 * np.sin(del_th) * np.cos(del_th)
        t2 = g * np.sin(theta2) * np.cos(del_th)
        t3 = L2 * omega2**2 * np.sin(del_th)
        t4 = - 2 * g * np.sin(theta1)
        num = t1 + t2 + t3 + t4
        denom = 2*L1 - L1*np.cos(del_th)**2
        return num/denom

    def domega2_dt(self, u: np.ndarray) -> float:
        theta1, omega1, theta2, omega2 = u
        del_th = theta2 - theta1
        L1, L2, g = self.L1, self.L2, self.g
        t1 = - L2 * omega2**2 * np.sin(del_th) * np.cos(del_th)
        t2 = 2 * g * np.sin(theta1) * np.cos(del_th)
        t3 = - 2 * L1 * omega1**2 * np.sin(del_th)
        t4 = - 2 * g * np.sin(theta2)
        num = t1 + t2 + t3 + t4
        denom = 2*L2 - L2*np.cos(del_th)**2
        return num/denom


@dataclass
class DoublePendulumResults:
    results: ode.ODEResult
    double_pendulum: DoublePendulum

    @property
    def theta1(self):
        return self.results.solution[0]

    @property
    def omega1(self):
        return self.results.solution[1]

    @property
    def theta2(self):
        return self.results.solution[2]

    @property
    def omega2(self):
        return self.results.solution[3]

    @property
    def x1(self):
        return self.double_pendulum.L1 * np.sin(self.theta1)

    @property
    def y1(self):
        return - self.double_pendulum.L1 * np.cos(self.theta1)

    @property
    def x2(self):
        return self.x1 + self.double_pendulum.L2*np.sin(self.theta2)

    @property
    def y2(self):
        return self.y1 - self.double_pendulum.L2*np.cos(self.theta2)

    @property
    def potential_energy(self):
        L1, L2 = self.double_pendulum.L1, self.double_pendulum.L2
        U1 = self.double_pendulum.g*(self.y1 + L1)
        U2 = self.double_pendulum.g*(self.y2 + L1 + L2)
        return U1 + U2

    @property
    def vx1(self) -> np.ndarray:
        return np.gradient(self.x1, self.results.time)

    @property
    def vy1(self) -> np.ndarray:
        return np.gradient(self.y1, self.results.time)

    @property
    def vx2(self) -> np.ndarray:
        return np.gradient(self.x2, self.results.time)

    @property
    def vy2(self) -> np.ndarray:
        return np.gradient(self.y2, self.results.time)

    @property
    def kinetic_energy(self):
        return 0.5*(self.vx1**2 + self.vy1**2 + self.vx2**2 + self.vy2**2)

    @property
    def total_energy(self):
        return self.kinetic_energy + self.potential_energy


def solve_double_pendulum(
    u0: np.ndarray,
    T: float,
    dt: float = 0.01,
    pendulum: Optional[DoublePendulum] = None,
) -> DoublePendulumResults:
    if pendulum is None:
        pendulum = DoublePendulum()
    sol = DoublePendulumResults(ode.solve_ode(pendulum, u0, T, dt), pendulum)
    return sol


def exercise_3d():
    u0 = np.array([np.pi/6, 0.35, 0, 0])
    T = 10.0
    dt = 0.01
    model = DoublePendulum()
    res = solve_double_pendulum(u0, T, dt, model)
    plot_energy(res, filename="output/energy_double.png")


def animate_pendulum(results: DoublePendulumResults) -> None:
    """Adopted from
    https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
    license: BSD
    """
    fig = plt.figure()
    ax = fig.add_subplot(
        111, aspect="equal", autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2)
    )
    ax.grid()

    (line,) = ax.plot([], [], "o-", lw=2)
    time_text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    kinetic_energy_text = ax.text(0.02, 0.90, "", transform=ax.transAxes)
    potential_energy_text = ax.text(0.02, 0.85, "", transform=ax.transAxes)

    def init():
        """initialize animation"""
        line.set_data([], [])
        time_text.set_text("")
        kinetic_energy_text.set_text("")
        potential_energy_text.set_text("")
        return line, time_text, kinetic_energy_text, potential_energy_text

    def animate(i):
        """perform animation step"""
        line.set_data(
            (0, results.x1[i], results.x2[i]), (0, results.y1[i], results.y2[i])
        )
        time_text.set_text(f"time = {results.results.time[i]:.1f}")
        kinetic_energy_text.set_text(
            f"kinetic energy = {results.kinetic_energy[i]:.3f} J"
        )
        potential_energy_text.set_text(
            f"potential energy = {results.potential_energy[i]:.3f} J"
        )
        return line, time_text, kinetic_energy_text, potential_energy_text

    ani = animation.FuncAnimation(
        fig, animate, frames=len(results.results.time), interval=10, blit=True,
        init_func=init
    )
    plt.show()


def exercise_4():
    results = solve_double_pendulum(
        u0=np.array([np.pi, 0.35, 0, 0]), T=40.0, dt=0.01
    )
    animate_pendulum(results)


if __name__ == "__main__":
    exercise_3d()
    exercise_4()
