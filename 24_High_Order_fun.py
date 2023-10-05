# a high order function is a function takes a function as a parameter
# and/or returns a function as its return value

# sorted a high order fun
print(sorted(['ajay', 'ram', 'karan', 'vishwajeet'], key=lambda x: len(x)))

# map:
result = list(map(lambda x: x ** 2, [2, 3, 4, 5]))
print(result)

result = list(map(lambda x, y: x + y, [1, 2, 3, 4], [10, 20, 30, 40]))
print(result)

result = list(map(lambda x, y: x if x > y else y, [11, 13, 15], [9, 17, 10]))
print(result)

result = list(map(lambda x, y: x - y, [10, 11, 12, 13], [5, 6, 7]))
print(result)

result = list(filter(lambda x: x > 0, [-10, 1, 0, -12, 13]))
print(result)

result = list(filter(None, [None, 0, '', 'hello', -1, False, True]))
print(result)

# Zip : it is not a high order function, but it is used in conjunction with high order functions

result = list(zip([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e', 'f'], 'python'))
print(result)

import string

result = [t[0] + str(t[1]) for t in zip(string.ascii_lowercase, range(1, 11))]
print(result)

# list comprehension , an alternative to map
result = [x ** 2 for x in range(2, 7)]
print(result)

result = [x + y for x, y in zip(range(2, 9), range(1, 8))]
print(result)

even = [x for x in range(1, 11) if x % 2 == 0]
print(even)

# [<expression> for <varname> in <iterable> if <condition>]

result = [x for x in range(1, 30) if x >= 15 and x <= 25]
print(result)

result = [x ** 2 for x in range(10) if x ** 2 < 25]
print(result)


def fact(n):
    return 1 if n < 2 else n * fact(n - 1)


factorials = list(map(fact, range(6)))
print("factorials of 1 to 5:", factorials)

Qsales_22 = [100, 120, 150, 170]
Qsales_23 = [190, 180, 220, 250]

print("Quarlerly sales growth:", list(map(lambda x, y: y - x, Qsales_22, Qsales_23)))

l1 = [10, 12, 15, 16]
l2 = [9, 12, 15, 10]
l3 = [8, 15, 12, 17]
print("best of 3:", list(map(lambda x, y, z: max(x, y, z), l1, l2, l3)))

from random import randint

n = [randint(-10, 10) for i in range(10)]
positive = list(filter(lambda x: x > 0, n))
negative = list(filter(lambda x: x < 0, n))
print("nums", n)
print("positive:", positive)
print("negative:", negative)

fname = ["Virat", "Sachin", "Rohit"]
lname = ["Kohli", "Tendulkar", "Sharma"]
for f, l in zip(fname, lname):
    print(f"{f} {l}")

# factorials using generator
factorials = (fact(i) for i in range(10))
print(factorials)
for n, i in zip(factorials, range(6)):
    print(f"factorial of {i} is {n}")

n1 = [randint(1, 10) for i in range(10)]
n2 = [randint(1, 10) for i in range(10)]
print(n1, n2)
result = [x + y for x, y in zip(n1, n2) if (x + y) % 2 == 0]
print(result)
