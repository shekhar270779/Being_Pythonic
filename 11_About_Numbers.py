# Numbers
# Integers : int
# Rational numbers: p/q , p & q are integers and q is not zero : fractions.Fraction
# Real numbers : can be represented as float or decimal.Decimal
# Complex Numbers: complex
# Boolean truth values : bool : False -> 0, True -> 1

# Integers : int datatype
# int object in python uses variable number of bits

import sys
import time
import math

print(f"memory (bytes) by 0 integer: {sys.getsizeof(0)}")
print(f"memory (bytes) by 1 integer: {sys.getsizeof(1)}")
print(
    f"memory (bytes) by 2^1000 integer: {sys.getsizeof(2 ** 1000)}, no. of bits: {(sys.getsizeof(2 ** 1000) - 24) * 8}")


def calc(x: int):
    for i in range(10000000):
        x * 2


start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(f"{end - start} secs")

start = time.perf_counter()
calc(2 ** 100)
end = time.perf_counter()
print(f"{end - start} secs")

# mathemetical operations
# int + int => int
# int - int => int
# int * int => int
# int / int => float
# int ** int => int
# int // int => floor division
# int % int =>  modulos

# a = b * (a//b) + (a % b)

floor_value = 135 // 4
mod_value = 135 % 4
print(f"135/4: floor:{floor_value}, mod:{mod_value}")

# floor : floor of a real number is the largest integer <=a
print(f"3.1: {math.floor(3.1)}, 3.99:{math.floor(3.99)}, -3.16:{math.floor(-3.16)}")

floor_value = -135 // 4
mod_value = -135 % 4
print(f"-135/4: floor:{floor_value}, mod:{mod_value}")


def equation_value(a, b):
    return b * (a // b) + (a % b)


print(f"13/4: floor: {13 // 4}, mod: {13 % 4}, eq_val: {equation_value(13, 4)}")
print(f"-13/4: floor: {-13 // 4}, mod: {-13 % 4}, eq_val: {equation_value(-13, 4)}")
print(f"13/-4: floor: {13 // -4}, mod: {13 % -4}, eq_val: {equation_value(13, -4)}")
print(f"-13/-4: floor: {-13 // -4}, mod: {-13 % -4}, eq_val: {equation_value(-13, -4)}")

print(f"13/4: {13 / 4}, floor:{math.floor(13 / 4)}, div:{13 // 4}, mod:{13 % 4}, trunc: {math.trunc(13 / 4)}")
print(f"-13/4: {-13 / 4}, floor:{math.floor(-13 / 4)}, div:{-13 // 4}, mod:{-13 % 4}, trunc: {math.trunc(-13 / 4)}")

# integer constructor and bases
# int class has 2 constructors
# int(), int(string, base) : string that can be parsed to a number

a = "1110101"
int_a = int(a, base=2)
bin_a = bin(int_a)
print(f"int: {int_a}, bin: {bin_a}")

a = "567"
int_a = int(a, base=8)
oct_a = oct(int_a)
print(f"int: {int_a}, oct: {oct_a}")

a = "abcde"
int_a = int(a, base=16)
hex_a = hex(int_a)
print(f"int: {int_a}, hex: {hex_a}")


def f(n, b):
    '''custom convertor function to any base
    '''
    if b < 2 or b > 36:
        raise ValueError("base must be between 2 to 36")
    sign = -1 if n < 0 else 1
    n = n * sign
    if n == 0:
        return '0'
    lst = ['-'] if sign == -1 else []
    map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x = n
    while (x > 0):
        x, m = divmod(x, b)
        lst.insert(1, map[m])

    return ''.join(lst)


print(f(232, 5), int(f(232, 5), base=5))
num = 1096
base = 15
print(f"base {base}: {f(num, base)}, int: {int(f(num, base), base=base)}")

num = -1096
print(f"Representing {num} in different base as below:")
for b in range(1, 17):
    try:
        print(f"base:{b:2}: {f(num, b)}")
    except ValueError:
        print(f"base:{b:2}: base should be >= 2")
        continue
