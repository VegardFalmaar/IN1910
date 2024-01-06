import os

import numpy as np
import matplotlib.pyplot as plt


class ChaosGame:
    def __init__(self, n: int, r: float = 0.5):
        if not isinstance(n, int):
            raise TypeError(f'n must be integer, not {type(n)}')
        if not isinstance(r, float):
            raise TypeError(f'f must be float, not {type(r)}')
        if n < 3:
            raise ValueError(f'n must >= 3, not {n = }')
        if not 0 < r < 1:
            raise ValueError(f'Must have 0 < r < 1, not {r = }')
        self._n = n
        self._r = r
        self._vertices = self._generate_ngon()
        self.sequence = None
        self.vertex_indices = None

    def _generate_ngon(self):
        vertices = np.empty((self._n, 2))
        angles = distributed_angles(self._n)
        vertices[:, 0] = np.sin(angles)
        vertices[:, 1] = np.cos(angles)
        return vertices

    def plot_ngon(self):
        """Plot the positions of the vertices in the ngon."""
        fig, ax = plt.subplots()
        ax.scatter(self._vertices[:, 0], self._vertices[:, 1])
        ax.grid()
        ax.axis('equal')
        fig.savefig(f'output/vertices_{self._n}-gon')
        plt.close(fig)

    def _starting_point(self):
        w = np.random.random(size=self._n)
        w /= np.sum(w)
        v = w.dot(self._vertices)
        return v

    def iterate(self, steps: int, discard: int = 5) -> np.ndarray:
        assert isinstance(steps, int)
        assert isinstance(discard, int)
        seq = np.empty((steps, 2))
        indices = np.empty(steps, dtype=int)
        seq[0] = self._starting_point()
        for _ in range(discard):
            seq[0], indices[0] = self._sequence_step(seq[0])
        for i in range(steps - 1):
            seq[i+1], indices[i+1] = self._sequence_step(seq[i])
        self.sequence = seq
        self.vertex_indices = indices

    def _sequence_step(self, x):
        i = np.random.randint(0, self._n)
        c = self._r*x + (1 - self._r)*self._vertices[i]
        return c, i

    def plot(self, color: bool = False, cmap: str = 'rainbow'):
        if color:
            colors = self.gradient_color
        else:
            colors = 'black'
        fig, ax = plt.subplots()
        ax.scatter(
            self.sequence[:, 0],
            self.sequence[:, 1],
            c=colors,
            cmap=cmap,
            s=0.1,
            marker='.'
        )
        ax.axis('equal')
        ax.axis('off')
        return fig, ax

    def show(self, color: bool = False, cmap: str = 'rainbow'):
        self.plot(color, cmap)
        plt.show()

    @property
    def gradient_color(self):
        colors = [self.vertex_indices[0]]
        for idx in self.vertex_indices[1:]:
            colors.append(0.5*(colors[-1] + idx))
        return colors

    def savepng(self, outfile, color=False, cmap='rainbow'):
        fig, _ = self.plot(color, cmap)
        file_ext = os.path.splitext(outfile)[1]
        if file_ext not in ['', '.png']:
            s = f'output filename should have extension .png, not {file_ext}'
            raise ValueError(s)
        fig.savefig(outfile)
        plt.close(fig)


def distributed_angles(n: int):
    return np.linspace(0, 2*np.pi, n + 1)[:-1]


def plot_ngon_vertices():
    for i in range(3, 9):
        g = ChaosGame(i)
        g.plot_ngon()


def plot_points_in_pentagon():
    g = ChaosGame(5)
    N = 1000
    v = np.empty((N, 2))
    for i in range(N):
        v[i] = g._starting_point()

    fig, ax = plt.subplots()
    ax.scatter(v[:, 0], v[:, 1])
    ax.axis('equal')
    ax.axis('off')
    fig.savefig('output/pentagon_1000_points')
    plt.close(fig)


def plot_sequence():
    g = ChaosGame(3, 0.5)
    g.iterate(steps=10_000)
    g.show(color=False)
    g.show(color=True)
    g.savepng('output/triangle_no_ext', color=True)
    g.savepng('output/triangle_ext.png', color=True)


def generate_some_figures():
    n_values = [3, 4, 5, 5, 6]
    r_values = [1/2, 1/3, 1/3, 3/8, 1/3]
    for m, (n, r) in enumerate(zip(n_values, r_values)):
        g = ChaosGame(n, r)
        g.iterate(10_000)
        fname = f'figures/chaos{m+1}.png'
        g.savepng(fname, color=True)


if __name__ == '__main__':
    plot_ngon_vertices()
    plot_points_in_pentagon()
    plot_sequence()
    generate_some_figures()
