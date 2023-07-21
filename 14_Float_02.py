# float equality
x = 0.125  # it can be expressed in power of 2, so we get exact value as float
print(x)
print(f"{x:.20f}")
x = 0.125 + 0.125 + 0.125
y = 0.375
print(f"{x == y}")

x = 0.1 # it can not be expressed in power of 2, so we dont get exact value as float
print(x)
print(f"{x:.20f}")
x = 0.1 + 0.1 + 0.1
y = 0.3
print(f"x:{x:0.20f}, y:{y:.20f}")
print(f"direct comparison: {x == y}")
print(f"round comparison: {round(x,3):.3f} & {round(y,3):.3f}: {round(x,3) == round(y,3)}")

# instead of round, use isclose()

from math import isclose

# If no errors occur, the result will be: abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol).

x = 0.1 + 0.1 + 0.1
y = 0.3
print(f"{isclose(x,y)}, {x==y}")

x = 123456789.01
y = 123456789.04
print(f"{isclose(x,y)}, {x==y}")

x = 0.01
y = 0.02
print(f"{isclose(x,y)}, {x==y}")

import math
# coerce float to integers : data loss
# truncate(), floor(), ciel(), round()

# truncate(): returns integer portion
print(f"{math.trunc(10.4)}, {math.trunc(0.3)}, {math.trunc(10.9)}")
print(f"{math.trunc(-10.4)}, {math.trunc(-0.3)}, {math.trunc(-10.9)}")

# int() uses trunc() so we can use int() instead also
print(f"{int(10.4)}, {int(0.3)}, {int(10.9)}")
print(f"{int(-10.4)}, {int(-0.3)}, {int(-10.9)}")

# floor() : largest int less than or equal to number
print(f"{math.floor(10.4)}, {math.floor(-10.4)}")

# ceil() : smallest integer greater than or equal to number
print(f"{math.ceil(10.2)}, {math.ceil(-10.2)}")

# trunc
from math import trunc
# trunc(x:Real): truncates x to the nearest integeral towards 0
print(f"trunc: {trunc(10.3)}, {trunc(10.8)}")
print(f"trunc: {trunc(-10.3)}, {trunc(-10.8)}")

from math import floor
print(f"floor: {floor(-10.2)}, {floor(-10.9)}, {floor(10.9)}")

from math import ceil
print(f"ceil: {ceil(10.9)}, {ceil(-10.9)}")

# round(x,n) : will round the number x to nearest multiple of 10^-n
# if no  n is specified, it will round to int
# IEEE754 standard rounds to nearest value, with ties round to nearest value with an even least significant digit
print(f"round: {round(10.9)}, {round(-10.5)}, {round(10.3)}")
print(f"{round(10.23)}, {round(10.23,1)}, {round(10.73,1)}, {round(10.78,1)}")
print(f"{round(10.23)}, {round(10.232,2)}, {round(10.734,2)}, {round(10.785,2)}")
print(f"{round(18.1, -1)}, {round(14.8, -1)}")
print(f"{round(1.25, 1)}, {round(-1.25,1)}")
print(f"{round(1.35, 1)}, {round(-1.35,1)}")

print(f"{round(15, -1)}, {round(-15, -1)}")
print(f"{round(25, -1)}, {round(-25, -1)}")

x = (0.5 + 1.5 + 2.5)/3
print(f"{x}")

y = (round(0.5) + round(1.5) + round(2.5))/3
print(f"{round(0.5)}, {round(1.5)}, {round(2.5)}, {y}")

print(f"{round(10.3)}, {round(10.9)}")

# rounding away from zero
# sign(x) * int(abs(x)+0.5)

import numpy as np
def round2(x):
    return np.sign(x) * int(abs(x) + 0.5)

from math import fabs, copysign

def round_up(x):
    return copysign(1, x) * int(fabs(x) + 0.5)


print(f"round2: {round2(10.5)}, {round2(10.2)}, {round2(10.8)}, {round2(-10.5)}, {round2(-10.8)}, {round2(-10.2)}")
print(f"round_up: {round_up(11.2)}, {round_up(198.45)}, {round_up(-199.54)}")

