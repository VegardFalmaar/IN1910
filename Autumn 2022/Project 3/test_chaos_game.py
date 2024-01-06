import pytest
import numpy as np

from chaos_game import ChaosGame, distributed_angles


def test_init_chaos_game_with_wrong_types_raises_TypeError():
    with pytest.raises(TypeError):
        ChaosGame('n', 0.5)
    with pytest.raises(TypeError):
        ChaosGame(4, 1)


def test_init_chaos_game_with_wrong_values_raises_ValueError():
    with pytest.raises(ValueError):
        ChaosGame(2, 0.5)
    with pytest.raises(ValueError):
        ChaosGame(4, 1.5)
    with pytest.raises(ValueError):
        ChaosGame(4, 0.0)
    with pytest.raises(ValueError):
        ChaosGame(4, 1.0)


def test_savepng_with_wrong_file_ext_raises_error():
    g = ChaosGame(4)
    g.iterate(10)
    with pytest.raises(ValueError):
        g.savepng('no_good.txt')


def test_distributed_angles():
    np.testing.assert_allclose(
        distributed_angles(3),
        [0, 2*np.pi/3, 4*np.pi/3]
    )
    np.testing.assert_allclose(
        distributed_angles(4),
        [0, np.pi/2, np.pi, 3*np.pi/2]
    )


def test_gradient_colors():
    g = ChaosGame(3)
    g.vertex_indices = [1, 2, 3, 4]
    correct_colors = [1, 3/2, 9/4, 25/8]
    colors = g.gradient_color
    assert len(colors) == 4
    tol = 1E-8
    for col, cor in zip(colors, correct_colors):
        assert abs(col - cor) < tol


def test_all_vertices_are_used_in_iteration():
    g = ChaosGame(10)
    g.iterate(10_000)
    for i in range(10):
        assert i in g.vertex_indices
