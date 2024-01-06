import nose.tools as nt
from pendulum import Pendulum
import numpy as np

def test_Pendulum_call():
    """Test the call method of the Pendulum class.

    This is done by comparing the method's output to values computed by hand.
    """
    L = 2.2
    omega = 0.1
    theta = np.pi/4
    t = 1           # Random value for t as it does not matter in the calculation
    test_case = Pendulum(L=L)
    # nt.assert_almost_equal(test_case(t, (theta, omega)), (0.1, 3.1530534))
    nt.assert_almost_equal(test_case((theta, omega), t)[0], 0.1)
    nt.assert_almost_equal(test_case((theta, omega), t)[1], -3.1530534197)#, places=5)

    # nt.assert_equal(test_case(t, (0, 0)), (0, 0))
    nt.assert_equal(test_case((0, 0), t)[0], 0)
    nt.assert_equal(test_case((0, 0), t)[1], 0)

@nt.raises(AttributeError)
def test_t():
    """Test the property t."""
    model = Pendulum()
    model.t

@nt.raises(AttributeError)
def test_theta():
    """Test the property theta."""
    model = Pendulum()
    model.theta

@nt.raises(AttributeError)
def test_omega():
    """Test the property omega."""
    model = Pendulum()
    model.omega

def test_equilibrium():
    """Test that the system behaves as expected when theta_0 = omega_0 = 0."""
    model = Pendulum()
    model.solve(u0=(0, 0), T=4, dt=0.01)
    n = np.ceil(4/0.01)
    np.testing.assert_allclose(model.t, np.linspace(0, 4, n+1))
    np.testing.assert_allclose(model.theta, np.zeros(int(n+1)))
    np.testing.assert_allclose(model.omega, np.zeros(int(n+1)))

def test_Cartesian():
    """Test the Cartesian coordinates to describe the motion."""
    model = Pendulum(L=2)
    model.solve(u0=(50, 0), T=4, dt=0.01, angles='deg')
    np.testing.assert_allclose(model.x**2+model.y**2, model.L**2)