import nose.tools as nt
import numpy as np
from double_pendulum import DoublePendulum

def test_double_pendulum_call():
    """Test the call method of the DoublePendulum class.

    The output of the method is compared to valued calculated by hand.
    """
    model = DoublePendulum(M_1=2, L_1=0.5, M_2=1.5, L_2=1)
    np.testing.assert_allclose(model(u=(np.pi/3, -np.pi/9, np.pi/9, -np.pi/18), t=1), (-np.pi/9, -19.81398625, -np.pi/18, 4.273140287))

def test_double_pendulum_cartesian():
    """Test that the distance between the masses are what they should be."""
    model = DoublePendulum(M_1=2, L_1=0.5, M_2=1.5, L_2=1)
    model.solve(u0=(60, -10, 0, -20), T=10, dt=0.001, angles='deg')
    np.testing.assert_allclose(model.x1**2+model.y1**2, model.L_1**2)
    np.testing.assert_allclose((model.x2-model.x1)**2+(model.y2-model.y1)**2, model.L_2**2)

def test_double_pendulum_equilibrium():
    """Test that the system behaves as expected from an equilibrium starting position."""
    model = DoublePendulum(M_1=2, L_1=0.5, M_2=1.5, L_2=1)
    model.solve(u0=(0, 0, 0, 0), T=10, dt=0.001, angles='deg')
    n = np.ceil(10/0.001)
    zero_array = np.zeros(int(n+1))
    np.testing.assert_allclose(model.theta1, zero_array, atol=1E-10)
    np.testing.assert_allclose(model.theta2, zero_array, atol=1E-10)
    np.testing.assert_allclose(model.vx1, zero_array, atol=1E-10)
    np.testing.assert_allclose(model.vy1, zero_array, atol=1E-10)
    np.testing.assert_allclose(model.vx2, zero_array, atol=1E-10)
    np.testing.assert_allclose(model.vy2, zero_array, atol=1E-10)

# def test_double_pendulum_kinetic():
#     """Test that the distance between the masses are what they should be."""
#     model = DoublePendulum(M_1=2, L_1=0.5, M_2=1.5, L_2=1)
#     model.solve(u0=(60, -10, 0, -20), T=10, dt=0.001, angles='deg')