# lambda expressions
# we create functions using def statement
# lambda expressions are another way to create functions
# lambda expressions are also called as anonymous functions
# lambda [parameter list]: expression
# it creates a function and returns a function object
# we assign lambda to a variable name

square = lambda x : x ** 2
cube = lambda x : x ** 3
n = 9
print(f"Square of {n} is {square(n)}")
print(f"cube of {n} is {cube(n)}")

def apply_fun(x, f):
    return f(x)

print(f"sq: {apply_fun(n, square)}")
print(f"cube: {apply_fun(n, cube)}")

print(f"double of {n} is {apply_fun(n, lambda x: 2 * n)}")

# limitations
# body of lambda is limited to a single expression
# no assignments lambd x : x += 5 [not allowed]
# no annotations allowed
# single logical line of code

add = lambda x=0, y=0: x + y
print(add(), add(10), add(10,5))

min_max_avg = lambda *args: (min(args) + max(args)) / 2
print(f"min|_max_avg : {min_max_avg(10, 11, 12, 13, 14, 15)}")

day_colors = {'mon': 'white',
              'tue':'orange' ,
              'wed': 'blue',
              'thu': 'yellow',
              'fri': 'green',
              'sat': 'black',
              'sun':'red'
              }

pick_shirt_color = lambda day, **kwargs: kwargs.get(day, None)
print(pick_shirt_color('tue', **day_colors ))

sq = lambda x: x ** 2
cube = lambda x : x ** 3
fun_list = [sq, cube]
apply_fun = lambda x, f: f(x)
n = 5
result = [apply_fun(n, f) for f in fun_list]
print(f"num: {n}, result: {result}")

apply_func = lambda func, *args, **kwargs: func(*args, **kwargs)
print(apply_func(lambda x, y: x + y, 10, 11))
print(apply_func(lambda *args: max(args), 10,9,12,13))


# sorted()
letters = ['k', 'A', 'b', 'E', 'f', 'G']
print(sorted(letters))

# sort in case-insensitive way
print(sorted(letters, key=lambda x : x.upper()))

signals = {'alpha': 7.1, 'beta': 5.6, 'gamma': 8.9, 'theta': 7.8}
print(sorted(signals))
print(sorted(signals, key=lambda x : signals[x]))

import math

dist_from_origin = lambda x : math.sqrt(x.real**2 + x.imag**2)
print(sorted([1+3j, 2+5j, 3-4j, 5-4j, 1+2j], key=dist_from_origin))

words = ['please', 'sorry', 'help', 'thankyou']
print(sorted(words, key=lambda x : len(x)))


# Shuffle a list of numbers
from random import random

deck = ['A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(10):
    print(f"Sorting {i+1}: {sorted(deck, key=lambda x: random())}")






