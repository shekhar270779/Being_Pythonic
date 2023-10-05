# Float class is default representation of a real number in Python
# In CPython, float is implemented using C double type
# float uses a fixed number of bytes (8 bytes / 64 bits)
# sign: 1 bit, exponent: 11 bits, significant digits: 52

# significant digits: simply all digits except leading and trailing zeroes
# for ex 67423000000 => 67423E6 => exponent is 6 and no. of significant digits: 5
# 0.001234567 => 1234567E-9 => exponent -9, no. of significant digits: 7

# some numbers can not be represented using finite number of terms
# eg. pi = 3.14159...
# Some numbers which have a finite decimal representation do not have a finite binary representation

print(f"{.1:.5f}")
print(f"{.1:.10f}")
print(f"{.1:.15f}")
print(f"{.1:.20f}")

print(f"{float(10)}, {float(12.5)}, {float('15')}")

from fractions import Fraction

pi = Fraction('22/7')
print(f"pi in float: {float(pi)}")

x = 0.1 + 0.1 + 0.1
y = 0.3
print(f"Comparing x & y: {x == y}, x: {x:0.20f}, y: {y:0.20f}")

# round may not necessarily solve this float comparison problem
x = round(0.1, 5) + round(0.1, 5) + round(0.1, 5)
y = round(0.3, 5)
print(f"rounding each element: equality test: {x == y}")

# rounding whole equation may solve this problem
x = round(0.1 + 0.1 + 0.1, 5)
y = round(0.3, 5)
print(f"rounding whole expression: equality test: {x == y}")

# we can write a custom function to compare the numbers and deem them equal if difference is less
# than some range (epsilon)

import math


def is_equal(x, y, tolerance):
    return math.fabs(x - y) < tolerance


x = 0.1 + 0.1 + 0.1
y = 0.3
print(f"x:{x:.20f}, y:{y:.20f}, x-y: {x - y:.20f}")
print(f"absolute tolerance: {is_equal(x, y, 1E-15)}")

x = 10000.1 + 10000.1 + 10000.1
y = 30000.3
print(f"x:{x:.20f}, y:{y:.20f}, x-y: {x - y:.20f}")
print(f"absolute tolerance: {is_equal(x, y, 1E-15)}")

# use relative tolerance
absolute_tolerance = 1E-15
relative_tolerance = absolute_tolerance * max(abs(x), abs(y))
x = 0.1 + 0.1 + 0.1
y = 0.3
print(f"x:{x:.20f}, y:{y:.20f}, x-y: {x - y:.20f}")
print(f"relative tolerance: {is_equal(x, y, relative_tolerance)}")

relative_tolerance = absolute_tolerance * max(abs(x), abs(y))
x = 10000.1 + 10000.1 + 10000.1
y = 30000.3
print(f"x:{x:.20f}, y:{y:.20f}, x-y: {x - y:.20f}")
print(f"relative tolerance: {is_equal(x, y, relative_tolerance)}")

# combine absolute and relative tolerance

abs_tolerance = 1E-15
relative_tolerance = abs_tolerance * max(abs(x), abs(y))
tolerance = max(abs_tolerance, relative_tolerance)
x = 0.1 + 0.1 + 0.1
y = 0.3
print(f"x:{x:.20f}, y:{y:.20f}, x-y: {x - y:.20f}")
print(f"combined tolerance: {is_equal(x, y, tolerance)}")

abs_tolerance = 1E-15
relative_tolerance = abs_tolerance * max(abs(x), abs(y))
tolerance = max(abs_tolerance, relative_tolerance)
x = 10000.1 + 10000.1 + 10000.1
y = 30000.3
print(f"x:{x:.20f}, y:{y:.20f}, x-y: {x - y:.20f}")
print(f"combined tolerance: {is_equal(x, y, tolerance)}")

# use math module
# PEP 485

x = 0.1 + 0.1 + 0.1
y = 0.3
print(f"{math.isclose(x, y, abs_tol=1e-15)}")
x = 10000.1 + 10000.1 + 10000.1
y = 30000.3
print(f"{math.isclose(x, y, abs_tol=1e-15)}")
