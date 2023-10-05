from decimal import Decimal
from fractions import Fraction

# some issues are observed in float values comparison due to float number not being able to be represented in binary
print(10.0 == Decimal('10.0'))
print(0.1 == Decimal('0.1'))  # 0.1 can not be represented in binary equivalent

print(Decimal('0.125') == Fraction('1/8'))

# chained comparisons
# a == b == c means a==b and a==c
low = 1
med = 2
high = 3

print(high > med > low)

print(1 == Decimal('1.0') == Fraction(1, 1))

# a < b  > c # a < b and b > c

print([1, 2] is [1, 2], [1, 2] == [1, 2])

# membership test

print('one' in {'one': 1, 'two': 2})

# short circuit

print(3 < 2 < 4 / 0)

min_age = 18
max_age = 60
age = 24
is_eligible = min_age <= age <= max_age
print(f"is eligible: {is_eligible}")
