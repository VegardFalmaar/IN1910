import numpy as np
import matplotlib.pyplot as plt

class AddableDict(dict):
    def __add__(self, other):
        new = self.copy()
        for e in other:
            if e not in new:
                new[e] = other[e]
            else:
                new[e] += other[e]
        return new


class Polynomial:
    def __init__(self, dict):
        # a)
        # self.coeffs = dict

        # c)
        self.coeffs = AddableDict(dict)


    def __call__(self, x):
        val = 0
        for e in self.coeffs:
            val += self.coeffs[e]*x**e
        return val


    def __str__(self):
        str = ''
        for e in self.coeffs:
            str += ' + {} * x^{}'.format(self.coeffs[e], e)
        return str


    def __add__(self, other):
        # b)
        # new_coeffs = self.coeffs.copy()
        # for e in other.coeffs:
        #     if e not in new_coeffs:
        #         new_coeffs[e] = other.coeffs[e]
        #     else:
        #         new_coeffs[e] += other.coeffs[e]
        # return Polynomial(new_coeffs)

        # c)
        return Polynomial(self.coeffs + other.coeffs)


    def derivative(self):
        new_coeffs = {}
        for e in self.coeffs:
            if e != 0:
                new_coeffs[e-1] = self.coeffs[e]*e
        return Polynomial(new_coeffs)


    def __mul__(self, other):
        new_coeffs = {}
        for i in self.coeffs:
            for j in other.coeffs:
                if i+j not in new_coeffs:
                    new_coeffs[i+j] = self.coeffs[i]*other.coeffs[j]
                else:
                    new_coeffs[i+j] += self.coeffs[i]*other.coeffs[j]
        return Polynomial(new_coeffs)


# if __name__ == '__main__':
#     coeffs = {0: 1, 5:-1, 10:1}
#     f = Polynomial(coeffs)
#
#     print(f)
#
#     x = np.linspace(-1, 1, 101)
#     plt.plot(x, f(x))
#     plt.show()

# f = Polynomial({0:1, 5:-7, 10:1})
# g = Polynomial({5:7, 10:1, 15:-3})
#
# print(f+g)

# f = Polynomial({10:1, 6:-3, 2:2})
# print (f.derivative())

f = Polynomial({2: 4, 1: 1})
g = Polynomial({3: 3, 0: 1})
print(f*g)