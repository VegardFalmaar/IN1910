import numpy as np
from ODESolver import RungeKutta4
from pendulum import Pendulum
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class DoublePendulum(Pendulum):
    def __init__(self, M_1=1, L_1=1, M_2=1, L_2=1, g=9.81):
        self.M_1, self.L_1, self.M_2, self.L_2, self.g = M_1, L_1, M_2, L_2, g

    def __call__(self, u, t):
        M_1, L_1, M_2, L_2, g = self.M_1, self.L_1, self.M_2, self.L_2, self.g

        theta_1, omega_1, theta_2, omega_2 = u
        dtheta = theta_2 - theta_1

        new_theta_1 = omega_1
        new_theta_2 = omega_2

        new_omega_1 = ((M_2*L_1*omega_1**2*np.sin(dtheta)*np.cos(dtheta)
                        + M_2*g*np.sin(theta_2)*np.cos(dtheta)
                        + M_2*L_2*omega_2**2*np.sin(dtheta)
                        - (M_1 + M_2)*g*np.sin(theta_1))
                        /((M_1 + M_2)*L_1 - M_2*L_1*np.cos(dtheta)**2))

        new_omega_2 = ((-M_2*L_2*omega_2**2*np.sin(dtheta)*np.cos(dtheta)
                        + (M_1 + M_2)*g*np.sin(theta_1)*np.cos(dtheta)
                        - (M_1 + M_2)*L_1*omega_1**2*np.sin(dtheta)
                        - (M_1 + M_2)*g*np.sin(theta_2))
                        /((M_1 + M_2)*L_2 - M_2*L_2*np.cos(dtheta)**2))

        # print('theta_1: {} \n omega_1: {} \n theta_2: {} \n omega_2: {} \n'.format(theta_1, omega_1, theta_2, omega_2))
        # print('new_theta_1: {} \n new_omega_1: {} \n new_theta_2: {} \n new_omega_2: {} \n'.format(new_theta_1, new_omega_1, new_theta_2, new_omega_2))


        return (new_theta_1, new_omega_1, new_theta_2, new_omega_2)


    @property
    def t(self):
        try:
            return self._t
        except AttributeError:
            raise AttributeError('No attribute t, the problem has not been solved yet.')

    @property
    def theta1(self):
        try:
            return self._u[:, 0]
        except AttributeError:
            raise AttributeError('No attribute theta1, the problem has not been solved yet.')

    @property
    def theta2(self):
        try:
            return self._u[:, 2]
        except AttributeError:
            raise AttributeError('No attribute theta2, the problem has not been solved yet.')

    @property
    def x1(self):
        try:
            return self.L_1*np.sin(self.theta1)
        except AttributeError:
            raise AttributeError('No attribute x1, the problem has not been solved yet.')

    @property
    def y1(self):
        try:
            return -self.L_1*np.cos(self.theta1)
        except AttributeError:
            raise AttributeError('No attribute y1, the problem has not been solved yet.')

    @property
    def x2(self):
        try:
            return self.x1 + self.L_2*np.sin(self.theta2)
        except AttributeError:
            raise AttributeError('No attribute x2, the problem has not been solved yet.')

    @property
    def y2(self):
        try:
            return self.y1 - self.L_2*np.cos(self.theta2)
        except AttributeError:
            raise AttributeError('No attribute y2, the problem has not been solved yet.')

    @property
    def vx1(self):
        try:
            return np.gradient(self.x1, self._t)
        except AttributeError:
            raise AttributeError('No attribute vx1, the problem has not been solved yet.')

    @property
    def vy1(self):
        try:
            return np.gradient(self.y1, self._t)
        except AttributeError:
            raise AttributeError('No attribute vy1, the problem has not been solved yet.')

    @property
    def vx2(self):
        try:
            return np.gradient(self.x2, self._t)
        except AttributeError:
            raise AttributeError('No attribute vx2, the problem has not been solved yet.')

    @property
    def vy2(self):
        try:
            return np.gradient(self.y2, self._t)
        except AttributeError:
            raise AttributeError('No attribute vy2, the problem has not been solved yet.')

    @property
    def potential(self):
        try:
            P_1 = self.M_1*self.g*(self.y1 + self.L_1)
            P_2 = self.M_2*self.g*(self.y2 + self.L_1 + self.L_2)
            return P_1 + P_2
        except AttributeError:
            raise AttributeError('The problem has not been solved yet.')

    @property
    def kinetic(self):
        try:
            K_1 = 0.5*self.M_1*(self.vx1**2 + self.vy1**2)
            K_2 = 0.5*self.M_2*(self.vx2**2 + self.vy2**2)
            return K_1 + K_2
        except AttributeError:
            raise AttributeError('The problem has not been solved yet.')

    def create_animation(self):
        # Create empty figure
        fig = plt.figure()

        # Configure figure
        plt.axis('equal')
        plt.axis('off')
        plt.axis((-3, 3, -3, 3))

        # Make an "empty" plot object to be updated throughout the animation
        self.pendulums, = plt.plot([], [], 'o-', lw=2)

        # ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
        # ax.grid()
        #
        # self.pendulums, = ax.plot([], [], 'o-', lw=2)

        # Call FuncAnimation
        self.animation = FuncAnimation(fig,
                                        self._next_frame,
                                        frames=range(0, len(self.x1), int(np.ceil(0.01/self.dt))),
                                        repeat=None,
                                        interval=self.dt,
                                        blit=True)

    def _next_frame(self, i):
        self.pendulums.set_data((0, self.x1[i], self.x2[i]),
                                (0, self.y1[i], self.y2[i]))
        return self.pendulums,

    def show_animation(self):
        plt.show()

if __name__ == '__main__':
    model = DoublePendulum(M_1=2, L_1=1, M_2=3, L_2=1)
    model.solve(u0=(140, -10, 90, -40), T=20, dt=0.001, angles='deg')
    # print(model.x1[:50])
    model.create_animation()
    model.show_animation()

    # model.solve(u0=(0, 0, 0, 0), T=4, dt=0.001, angles='deg')
    # plt.plot(model.x1, model.y1, model.x2, model.y2)
    # print(model.t[:10])
    # print(model.vx1[:10])
    # print(model.vy1[:10])
    # print(model.vx2[:10])
    # print(model.vy2[:10])

    # plt.plot(model.t, model.kinetic, model.t, model.potential, model.t, model.kinetic+model.potential)
    # plt.title('Energy')
    # plt.legend(['kinetic', 'potential', 'total'])
    # plt.show()