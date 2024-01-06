def add(x: float, y: float) -> float:
    return x + y

def divide(x: float, y: float) -> float:
    return x/y

def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError

    if n == 0:
        return 1
    elif n < 0:
        raise ValueError
    return n*factorial(n - 1)

def sin(x: float, N: int=20) -> float:
    s = 0.0
    for n in range(N+1):
        s += (-1)**n*x**(2*n + 1)/factorial(2*n + 1)
    return s

def sqrt(y: float, x0: float = 1, tol: float = 1e-12) -> float:
    f = lambda x: 0.5*(y/x + x)
    x_prev = x0
    x_new = f(x_prev)
    while abs(x_new - x_prev) > tol:
        x_prev = x_new
        x_new = f(x_prev)
    return x_new
