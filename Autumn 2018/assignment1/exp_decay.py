# from scipy.integrate import solve_ivp
import numpy as np
from ODESolver import RungeKutta4

class ExponentialDecay:
    def __init__(self, a):
        self.a = a

    def __call__(self, t, u):
        """Define the RHS of the ODE."""
        return -self.a*u

    def solve(self, u0, T, dt):
        n = np.ceil(T/dt)
        timepoints = np.linspace(0, T, n)
        # return si.solve_ivp(self, (0, T), (u0,), t_eval=timepoints)
        solver = RungeKutta4(self)
        solver.set_initial_condition(u0)
        return solver.solve(timepoints)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    a = 0.4
    T = 2
    dt = 0.01
    u0 = 3.2
    decay_model = ExponentialDecay(a)
    t, u = decay_model.solve(u0, T, dt)

    plt.plot(t, u)
    plt.show()