from functools import partial


def my_func(a, b, c):
    return a + b + c


def f(x, y):
    return my_func(10, x, y)


print(f(2, 3))

jump_by_20 = lambda x, y: my_func(20, x, y)
print(jump_by_20(1, 2))

mul_func = lambda x, y: x * y
double = lambda x: mul_func(x=x, y=2)
triple = lambda x: mul_func(x=x, y=3)

print(double(10), triple(10))

pow = lambda base, exponent: base ** exponent
square = partial(pow, exponent=2)
cube = partial(pow, exponent=3)

print(square(5), cube(5))


def some_fun(a, b):
    return b in a


lst = [1, 2]
f = partial(some_fun, lst)
print(f(2))
print(f(3))
lst.append(3)
print(f(3))

import math

origin = (0, 0)
distance_sq = lambda a, b: (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
distance_origin_sq = partial(distance_sq, origin)
print(distance_origin_sq((2, 3)))

points = [(2, 3), (3, 5), (-2, 4), (1, 4), (2, 1)]
print(sorted(points, key=distance_origin_sq))
