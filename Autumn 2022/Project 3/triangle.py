import os
import numpy as np
import matplotlib.pyplot as plt     # type: ignore


def plot_points(points, fname, fractal=False, colors=None):
    """Plot the positions of points in a triangle."""
    fig, ax = plt.subplots()
    if fractal:
        if colors is None:
            ax.scatter(points[0], points[1], s=0.1, marker='.')
        else:
            red = points[:, colors == 0]
            green = points[:, colors == 1]
            blue = points[:, colors == 2]
            ax.scatter(red[0], red[1], color='red', s=0.1, marker='.')
            ax.scatter(green[0], green[1], color='green', s=0.1, marker='.')
            ax.scatter(blue[0], blue[1], color='blue', s=0.1, marker='.')
        ax.axis('off')
    else:
        ax.scatter(points[0], points[1])
        ax.grid()
    ax.axis('equal')
    fig.savefig(os.path.join('output', fname))
    plt.close(fig)


def triangle_vertices():
    """Return the positions of the vertices of a triangle.

    Args:
        None

    Returns:
        vertices (np.2darray): [[x-positions], [y-positions]]
    """
    return np.array([[0, 1, 1/2], [0, 0, np.sqrt(3)/2]])


def random_point():
    """Generate a random point as a linear combination of the vertices.

    Returns:
        v (np.1darray of length 2): the coordinates of the point
    """
    w = np.random.random(size=3)
    w /= np.sum(w)
    v = triangle_vertices().dot(w)
    return v


def plot_1000_random_points():
    """Generate and plot N random points."""
    N = 1000
    points = np.empty((2, N))
    for i in range(N):
        points[:, i] = random_point()
    plot_points(points, 'triangle_1000_points')


def sequence_of_points():
    """Generate a sequence of points using the iterative formula.

    Returns:
        sequence (np.2darray of shape (2, N):
            array with the positions of N points
    """
    N = 10_000
    sequence = np.empty((2, N))
    colors = np.empty(N)
    sequence[:, 0] = random_point()
    for _ in range(5):
        sequence[:, 0], colors[0] = sequence_step(sequence[:, 0])
    for i in range(N - 1):
        sequence[:, i+1], colors[i+1] = sequence_step(sequence[:, i])
    return sequence, colors


def sequence_step(x):
    """Calculate the next point in the sequence using the iterative formula."""
    i = np.random.randint(0, 3)
    c = triangle_vertices()[:, i]
    return 0.5*(x + c), i


if __name__ == '__main__':
    plot_points(triangle_vertices(), 'triangle_vertices')
    plot_1000_random_points()
    seq, col = sequence_of_points()
    plot_points(seq, 'triangle_sequence', fractal=True, colors=None)
    plot_points(seq, 'triangle_sequence_color', fractal=True, colors=col)
