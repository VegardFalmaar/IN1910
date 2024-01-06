import nose.tools as nt
from checking_primes import is_prime


def test_is_prime():
    """Test positive integers"""
    for i in range(1, 4):
        nt.assert_true(is_prime(i))
    nt.assert_false(is_prime(4))
    nt.assert_false(is_prime(12))
    nt.assert_true(is_prime(13))

@nt.raises(Exception)
def test_str_input():
    """Test string input"""
    is_prime('String')

@nt.raises(Exception)
def test_negative_number():
    """Test negative integer"""
    is_prime(-1)