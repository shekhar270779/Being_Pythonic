# Rational: p/q where p,q are integers and q is not 0
# import Fraction class from fractions module
from fractions import Fraction

pi = Fraction(numerator=22, denominator=7)
half = Fraction(1,2)
one_third = Fraction(1,3)
print(f"{pi}, {half}, {one_third}")

x = 12 * half
print(x)
x = 7 * pi
print(x)

quarter = Fraction(0.25)
print(quarter)

three_fifth = Fraction('3/5')
print(three_fifth)

num_of_people = 6
slice = Fraction(1, num_of_people)
print(slice)

print(f"half + half is: {half + half}")
print(f"half * half is: {half * half}")
print(f"half / half is: {half / half}")
v = one_third + quarter
print(f"One-third + Quarter: {v}, numerator: {v.numerator}, denominator: {v.denominator}")

print(f"{0.3:.20f}")

import math

x = Fraction(math.pi)
print(f"{x}")

print(x.limit_denominator(10))
print(x.limit_denominator(100))

y = Fraction(0.3).limit_denominator(10)
print(f"{y}")



