import nose.tools as nt
from exp_decay import ExponentialDecay

def test_ExponentialDecay():
    """Test that the output of the ExponentialDecay.__call__ method is correct."""
    a = 0.4
    t = 1   # Random value for t as it does not matter
    u = 3.2
    f = ExponentialDecay(a)
    nt.assert_almost_equal(f(t, u), -1.28)