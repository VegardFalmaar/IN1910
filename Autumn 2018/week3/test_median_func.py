import nose.tools as nt
from median_func import median

def test_one_element():
    """Test list with one element."""
    a = [3]
    nt.assert_equal(median(a), 3)

def test_two_elements():
    """Test list with two elements."""
    a = [5, 3]
    nt.assert_equal(median(a), 4)

def test_data_unchanged():
    """Test input data is unchanged."""
    a = [3, 5, 4, 2]
    a_old = a.copy()
    median(a)
    nt.assert_equal(a, a_old)

@nt.raises(Exception)
def test_empty_list_input():
    """Test that empty list input raises an error."""
    a = []
    median(a)