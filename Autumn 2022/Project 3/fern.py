import numpy as np
import matplotlib.pyplot as plt


class AffineTransform:
    def __init__(
        self,
        a: float = 0.0,
        b: float = 0.0,
        c: float = 0.0,
        d: float = 0.0,
        e: float = 0.0,
        f: float = 0.0
    ):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f

    def __call__(self, x, y):
        x_new = self._a*x + self._b*y + self._e
        y_new = self._c*x + self._d*y + self._f
        return x_new, y_new


functions = [
    AffineTransform(0, 0, 0, 0.16, 0, 0),
    AffineTransform(0.85, 0.04, -0.04, 0.85, 0, 1.60),
    AffineTransform(0.20, -0.26, 0.23, 0.22, 0, 1.60),
    AffineTransform(-0.15, 0.28, 0.26, 0.24, 0, 0.44)
]


def draw_random_function():
    probabilities = [0.01, 0.85, 0.07, 0.07]
    assert abs(sum(probabilities) - 1.0) < 1E-8
    p_cumulative = [probabilities[0]]
    for p in probabilities[1:]:
        p_cumulative.append(p_cumulative[-1] + p)
    r = np.random.random()
    for j, p in enumerate(p_cumulative):
        if r < p:
            return functions[j]


def iterate():
    N = 50_000
    x = np.zeros((N, 2))
    for i in range(N - 1):
        x[i+1] = draw_random_function()(x[i, 0], x[i, 1])
    return x


def plot(x):
    fig, ax = plt.subplots()
    ax.scatter(
        x[:, 0],
        x[:, 1],
        cmap='forestgreen',
        s=0.1,
        marker='.'
    )
    ax.axis('equal')
    ax.axis('off')
    fig.savefig('figures/barnsley_fern.png')
    plt.close(fig)


if __name__ == '__main__':
    points = iterate()
    plot(points)
