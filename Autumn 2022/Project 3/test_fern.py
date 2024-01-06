from fern import AffineTransform


def test_params_default_to_zero():
    t = AffineTransform()
    assert t(1, 2) == (0, 0)
    assert t(-3.14, 1.2345) == (0, 0)


def test_affine_transform():
    t = AffineTransform(1, 0, 0, 1, 0, 0)
    assert t(1, 2) == (1, 2)
    t = AffineTransform(0, 1, 1, 0, 0, 0)
    assert t(1, 2) == (2, 1)
    t = AffineTransform(1, 1, 1, 0, -3, 9)
    assert t(1, 2) == (0, 10)
