import numpy as np
import matplotlib.pyplot as plt

class Quadratic:
    def __init__(self, a_2, a_1, a_0):
        self.coeffs = {0:a_0, 1:a_1, 2:a_2}


    def __call__(self, x):
        val = 0
        for e in self.coeffs:
            val += self.coeffs[e]*x**e
        return val


    def __str__(self):
        a_2, a_1, a_0 = self.coeffs[2], self.coeffs[1], self.coeffs[0]
        line = '{:g}*x^2'.format(a_2)

        if a_1 > 0:
            line += ' + {:g}*x'.format(a_1)
        elif a_1 < 0:
            line += ' - {:g}*x'.format(abs(a_1))

        if a_0 > 0:
            line += ' + {:g}'.format(a_0)
        elif a_0 < 0:
            line += ' - {:g}'.format(abs(a_0))

        return line


    def __add__(self, other):
        new_coeffs = {}
        for e in self.coeffs:
            new_coeffs[e] = self.coeffs[e] + other.coeffs[e]
        return Quadratic(new_coeffs[2], new_coeffs[1], new_coeffs[0])


    def __subtract__(self, other):
        new_coeffs = {}
        for e in self.coeffs:
            new_coeffs[e] = self.coeffs[e] - other.coeffs[e]
        return Quadratic(new_coeffs[2], new_coeffs[1], new_coeffs[0])


    def roots(self):
        a, b, c = self.coeffs[2], self.coeffs[1], self.coeffs[0]
        sqrt = b**2 - 4*a*c
        tol = 1E-10

        if abs(sqrt) < tol:
            res = (-b/(2*a),)
        elif sqrt < -tol:
            res = ()
        else:
            res = ((-b + np.sqrt(sqrt))/(2*a), (-b - np.sqrt(sqrt))/(2*a))

        return res


    def intersect(self, other):
        diff = self.__subtract__(other)
        return diff.roots()



# f = Quadratic(2, -2, 2)
# g = Quadratic(1, -2, 1)
# h = Quadratic(1, -3, 2)
#
# x = np.linspace(-2, 4, 101)
# plt.plot(x, f(x), x, g(x), x, h(x))
# plt.legend(['f', 'g', 'h'])
# plt.grid()
# plt.show()
#
# print (f.roots())
# print (g.roots())
# print (h.roots())
#
# print (h.intersect(f))

f = Quadratic(1, -2, 1)
g = Quadratic(2, 3, -2)

x = np.linspace(-7, 5, 101)
plt.plot(x, f(x), x, g(x))

points = f.intersect(g)
for point in points:
    print (point)
    plt.plot(point, f(point), 'ro')

plt.grid()
plt.show()