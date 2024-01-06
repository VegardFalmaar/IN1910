import math, pytest

import calculator


eps = 1E-10


@pytest.mark.parametrize('a, b, out', [(1, 2, 3), (4, -2, 2), (6, 8, 14)])
def test_add_int(a, b, out):
    assert calculator.add(a, b) == out


@pytest.mark.parametrize('a, b, out', [(0.1, 0.2, 0.3), (0.4, -0.2, 0.2), (0.6, 0.8, 1.4)])
def test_add_float(a, b, out):
    assert abs(calculator.add(a, b) - out) < eps


@pytest.mark.parametrize('a, b, out', [(21, 7, 3), (8, 2, 4), (86, -43, -2)])
def test_divide_int(a, b, out):
    assert calculator.divide(a, b) == out


@pytest.mark.parametrize('a, b, out', [(1, 2, 0.5), (0, 2, 0.0), (-1, 2.5, -0.4)])
def test_divide_float(a, b, out):
    assert abs(calculator.divide(a, b) - out) < eps


@pytest.mark.parametrize('a, out', [(0, 1), (1, 1), (2, 2), (3, 6), (6, 720)])
def test_factorial(a, out):
    assert calculator.factorial(a) == out


@pytest.mark.parametrize(
    'a, out',
    [(0, 0), (math.pi/4, 1/math.sqrt(2)), (math.pi/2, 1), (3*math.pi/2, -1)]
)
def test_sin(a, out):
    assert abs(calculator.sin(a) - out) < eps


@pytest.mark.parametrize('a, out', [(4, 2), (81, 9), (73, math.sqrt(73)), (431, math.sqrt(431))])
def test_sqrt(a, out):
    assert abs(calculator.sqrt(a) - out) < eps


@pytest.mark.parametrize('a', [-1, -2, -724])
def test_factorial_raises_ValueError_for_negatives(a):
    with pytest.raises(ValueError):
        calculator.factorial(a)


@pytest.mark.parametrize('a', [1/3, 1.0, 41/7])
def test_factorial_raises_TypeError_for_floats(a):
    with pytest.raises(TypeError):
        calculator.factorial(a)


@pytest.mark.parametrize('a', [1, 3, 0])
def test_divide_raises_ZeroDivisionError(a):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(a, 0)
