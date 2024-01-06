# from scipy.integrate import solve_ivp
import numpy as np
from ODESolver import RungeKutta4, ForwardEuler

class Pendulum:
    def __init__(self, g=9.81, L=1, M=1):
        self.g = g
        self.L = L
        self.M = M

    def __call__(self, u, t): # Må byttes rekkefølge for å bruke solve_ivp
        """Compute the derivatives of theta and omega."""
        theta, omega = u
        new_omega = -self.g*np.sin(theta)/self.L
        new_theta = omega
        return (new_theta, new_omega)

    def solve(self, u0, T, dt, angles='rad'):
        self.dt = dt
        if angles == 'deg':
            u0 = [e*np.pi/180 for e in u0]
        elif angles != 'rad':
            raise KeyError('Keyword angles must be either "rad" og "deg".')
        n = np.ceil(T/dt)
        timepoints = np.linspace(0, T, n+1)
        # self.t, self.u = solve_ivp(self, (0, T), (u0,), t_eval=timepoints)

        # solver = RungeKutta4(self)
        solver = ForwardEuler(self)
        solver.set_initial_condition(u0)
        self._u, self._t = solver.solve(timepoints)

    @property
    def t(self):
        try:
            return self._t
        except AttributeError:
            raise AttributeError('No attribute t, the problem has not been solved yet.')

    @property
    def theta(self):
        try:
            return self._u[:, 0]
        except AttributeError:
            raise AttributeError('No attribute theta, the problem has not been solved yet.')

    @property
    def omega(self):
        try:
            return self._u[:, 1]
        except AttributeError:
            raise AttributeError('No attribute omega, the problem has not been solved yet.')

    @property
    def potential(self):
        try:
            return self.M*self.g*(self.y + self.L)
        except AttributeError:
            raise AttributeError('The problem has not been solved yet.')

    @property
    def kinetic(self):
        try:
            return 0.5*self.M*(self.vx**2 + self.vy**2)
        except AttributeError:
            raise AttributeError('The problem has not been solved yet.')

    @property
    def x(self):
        try:
            return self.L*np.sin(self.theta)
        except AttributeError:
            raise AttributeError('No attribute x, the problem has not been solved yet.')

    @property
    def y(self):
        try:
            return -self.L*np.cos(self.theta)
        except AttributeError:
            raise AttributeError('No attribute y, the problem has not been solved yet.')

    @property
    def vx(self):
        try:
            return np.gradient(self.x, self._t)
        except AttributeError:
            raise AttributeError('No attribute vx, the problem has not been solved yet.')

    @property
    def vy(self):
        try:
            return np.gradient(self.y, self._t)
        except AttributeError:
            raise AttributeError('No attribute vy, the problem has not been solved yet.')


class DampenedPendulum(Pendulum):
    def __init__(self, g=9.81, L=1, M=1, B=0.2):
        Pendulum.__init__(self, g=g, L=L, M=M)
        self.B = B

    def __call__(self, u, t):
        theta, omega = u
        new_omega = -self.g*np.sin(theta)/self.L - self.B*omega/self.M
        new_theta = omega
        return (new_theta, new_omega)

if __name__ == '__main__':
    model = Pendulum(M=2, L=0.5)
    model.solve(u0=(60, 0), T=4, dt=0.01, angles='deg')
    import matplotlib.pyplot as plt
    plt.subplot(2, 1, 1)
    plt.title('Theta')
    plt.plot(model.t, model.theta)
    plt.subplot(2, 1, 2)
    plt.title('Energy')
    plt.plot(model.t, model.kinetic, model.t, model.potential, model.t, model.kinetic+model.potential)
    plt.legend(['kinetic', 'potential', 'total'])
    plt.show()

    model = DampenedPendulum(M=2, L=0.5)
    model.solve(u0=(60, 0), T=4, dt=0.01, angles='deg')
    plt.plot(model.t, model.kinetic, model.t, model.potential, model.t, model.kinetic+model.potential)
    plt.title('Energy')
    plt.legend(['kinetic', 'potential', 'total'])
    plt.show()