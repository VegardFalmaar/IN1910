import nose.tools as nt
from writing_bubble_sort import bubble_sort

def test_empty_list():
    """Test that empty list returns an empty list."""
    a = []
    a_old = a.copy()
    b = []
    nt.assert_equal(bubble_sort(a), b)
    nt.assert_equal(a, a_old)

def test_one_element():
    """Test that list with one element returns a list with just that element."""
    a = [3]
    a_old = a.copy()
    b = [3]
    nt.assert_equal(bubble_sort(a), b)
    nt.assert_equal(a, a_old)

def test_various_lists():
    a = [5, 4, 3, 2, 1]
    a_old = a.copy()
    b = [1, 2, 3, 4, 5]
    nt.assert_equal(bubble_sort(a), b)
    nt.assert_equal(a, a_old)

    a = (3, 5, 2, 4, 7, 6, 1)
    a_old = (3, 5, 2, 4, 7, 6, 1)
    b = [1, 2, 3, 4, 5, 6, 7]
    nt.assert_equal(bubble_sort(a), b)
    nt.assert_equal(a, a_old)

    a = [-3, -5, 2, 0, 4]
    a_old = a.copy()
    b = [-5, -3, 0, 2, 4]
    nt.assert_equal(bubble_sort(a), b)
    nt.assert_equal(a, a_old)