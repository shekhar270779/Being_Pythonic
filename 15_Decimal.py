# decimal module PE327
# avoids the approximation issue
import decimal
from decimal import Decimal

# global context
gctx = decimal.getcontext() # returns the current context
print("Global Context:\n", gctx)

x = Decimal('1.25')
y = Decimal('1.35')
print(f"ROUND_HALF_EVEN: x:{round(x,1)}, y:{round(y,1)}")
# local context
with decimal.localcontext() as lctx:
    lctx.prec = 2
    lctx.rounding = decimal.ROUND_HALF_UP
    print("\nLocal Context:\n", lctx)
    print(f"Current context: {decimal.getcontext()}")
    print(f"ROUND_HALF_UP: x:{round(x,1)}, y:{round(y,1)}")
    lctx.rounding = decimal.ROUND_HALF_DOWN
    print(f"ROUND_HALF_DOWN: x:{round(x, 1)}, y:{round(y, 1)}")

print(type(decimal.getcontext()), type(decimal.localcontext()))

# z = (sign, (digits), exponent)
z = Decimal((1, (3, 1, 4), -2))
print(z)

x = 10.1
s1 = 0
for i in range(100000):
    s1 += x

print(f"s1: {s1:.20f}")

y = Decimal((0, (1,0,1), -1))
s2 = 0
for i in range(100000):
    s2 += y

print(f"s2: {s2:.20f}")

# context precision does not affect storage of object
# context precision affects arithmetic operations

a = Decimal('0.12345')
b = Decimal('0.12345')
c = a + b
print(c)

gctx.prec = 2
a = Decimal('0.12345')
b = Decimal('0.12345')
c = a + b
print(c)

# We know that n = d * (n//d) + (n % d)
# for int, n//d = floor(n/d)
# for decimal, n//d = trunc(n/d)

x = 10 //3
y = Decimal(10) // Decimal(3)
print(f"{x}, {y}")

x = -10//3
y = Decimal(-10) // Decimal(3)
print(f"{x}, {y}")

def equation(n,d):
    print(f"{n//d}, {n%d}")
    return n == d * (n//d) + (n % d)

print(equation(10,3))
print(equation(-10,3))
print(equation(-135,4))

x = 0.01
x_dec = Decimal('0.01')

import math
root = math.sqrt(x)
root_mix = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(f"{root:1.20f}, {root_mix:1.20f}, {root_dec:1.20f}")

def divmod2(n, d):
    return (n//d, n%d, n==d*(n//d) + (n%d))


x = 10
y = 3
print(divmod2(x,y))

x= Decimal(10)
y= Decimal(3)
print(divmod2(x,y))

x = -10
y = 3
print(divmod2(x,y))

x = Decimal(-10)
y = Decimal(3)
print(divmod2(x,y))

a = Decimal('2')
print(f"sqrt: {a.sqrt()}, ln:{a.ln()}, exp:{a.exp()}")

a = Decimal('3')
print(f"{math.sqrt(a):.15f}, {a.sqrt():.15f}")

# performance
import sys
x = 3.1415
y = Decimal('3.1415')
print(f"{sys.getsizeof(x)}, {sys.getsizeof(y)}")

import time

def run_float(n=1):
    for i in range(n):
        a=3.1415

def run_decimal(n=1):
    for i in range(n):
        a = Decimal('3.1415')


n=10000000
start = time.perf_counter()
run_float(n)
stop = time.perf_counter()
print(f"run_float time: {stop - start}")

start = time.perf_counter()
run_decimal(n)
stop = time.perf_counter()
print(f"run_decimal time: {stop - start}")

def operate_float(n=1):
    a=3.1415
    for i in range(n):
        a + a


def operate_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a + a



n=10000000
start = time.perf_counter()
operate_float(n)
stop = time.perf_counter()
print(f"operate_float time: {stop - start}")

start = time.perf_counter()
operate_decimal(n)
stop = time.perf_counter()
print(f"operate_decimal time: {stop - start}")












