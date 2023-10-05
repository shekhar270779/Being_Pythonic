# Function parameters and arguments
# Argument Vs Parameter

def f(a, b):  # in this context, a,b are called parameters of function f. a,b are local variables to the function f
    a = a * 2
    b = b * 2
    print(f"f(): {a},{b}")


x, y = 10, 15
f(x, y)  # when we call function f, x & y are called the arguments to function f
# in python, x & y are passed by reference i.e. memory addresses are passed
print(x, y)


# arguments by position
def hello(fname, lname):
    return (f"Hello {fname} {lname}!!")  # calling function hello() and passing arguments by function


print(hello("Kapil", "Dev"))


# we can also specify default value
# Rule: if  parameter is defined with a default value, every parameter after it must have a default value
def hello1(fname="", lname=""):  # default values are assigned as empty string
    return (f"Hello {fname} {lname}")


print(hello1())
print(hello1("Ram"))  # positional argument
print(hello1(lname="Kishan"))  # keyword argument or named argument


def select_choice(choice1=None, choice2=None, choice3=None):
    return choice1 or choice2 or choice3


print(select_choice("Red"))
print(select_choice(choice2="Orange", choice3="Green"))
print(select_choice(choice1="Red", choice3="Blue"))

# once we use named arguments, all arguments after it must be named too
print(select_choice("Purple", choice2="Red", choice3="Yellow"))

# tuple
# what defines tuple in python is not () but comma
# () is used to make tuple clear
t = 1, 2, 3
print(t)

# to create a tuple with single element
s = 9,
print(s)

# to create an empty tuple we have to use ()
e = ()
print(e)

# packed values are values that are bundled together in some way
t = (1, 2, 3)
lst = ['green', 'yellow', 'red']
lang = 'python'
odd_set = {1, 3, 5}
a_dict = {1: 'one', 2: 'two', 3: 'three'}

# infact, any iterable is considered as a packed value

# Unpacking: the act of splitting packed values contained in list or tuple into individual variables

# list unpack
x, y, z = [11, 12, 13]
print(x, y, z)

# tuple unpack
x, y, z = 10, 11, 12
print(x, y, z)

# string unpack
x, y, z = 'BYE'
print(x, y, z)


def swap(a, b):
    a, b = b, a
    return a, b


print(swap(10, 20))

codes = {'code-1': 'Abra ka dabra',
         'code-2': 'khul ja sim sim'}

for code in codes:  # it iterates through keys # unordered collection
    print(code, codes[code])

for k, v in codes.items():
    print(k, v)

set1 = {'p', 'y', 't', 'h', 'o', 'n'}  # unordered collection'
for item in set1:
    print(item, end=',')
print()

# Python >= 3.5
# we may not necessarily want to unpack all elements
# we may want to unpack say just first value

colors = ['green', 'blue', 'red', 'orange']
x, y = colors[0], colors[1:]
print(f"x:{x}, y:{y}")

# we can use * operator

a, *b = colors
print(f"a:{a}, b:{b}")

pi, *constants = (3.14, 1.414, 1.732)
print(pi, constants)

a, *s = 'hello'
print(a, s)

alert, success, *others = ['red', 'green', 'blue', 'orange']
print(alert, success, others)

first, second, *others, last = [1, 2, 3, 4, 5]
print(first, second, last, others)

a, *b = 'python'
b.insert(0, a)
print(a, b)

# merge two lists into one
evens = [2, 4, 6, 8]
odds = [1, 3, 5, 7]
nums = [*evens, *odds]
print(nums)

s = {10, -99, 3, 'd'}
print(s)

# merge dictionaries

d1 = {'p': 1, 'y': 13}
d2 = {'k': 2}
d3 = {'k': 3, 'o': 10}
d = {**d1, **d2, **d3}
print(d)

colors = {'red': 1, 'green': 2, 'yellow': 3}
rgb = {'red': 'r', 'green': 'g', 'blue': 'b'}
my_colors = {'black': 'k', **rgb}
print(my_colors)

# nested list
a, b, (c, d) = [1, 2, [3, 4]]
print(a, b, c, d)
a, *b, c, d, e = 'Hello man'
print(a, b, c, d, e)

a, *b, (c, *d) = [1, 2, 3, 'python']
print(a, b, c, d)

# * always unpacks to a list
x, *y, z = (1, 2, 3, 4, 5)
print(x, y, z)

# convert string into a list
s = 'hello python'
*s, = s
print(s)

# merge lists and eliminate duplicates
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
*z, = {*x, *y}
print(x, y, z)

s1 = {1, 2, 3}
s2 = {3, 4, 5}

s = {*s1, *s2}
print(s)

base_env = {'alpha': 1, 'beta': 2, 'gamma': 3}
user_env = {'beta': 2.2, 'theta': 4}

final_env = {**base_env, **user_env}
print(final_env)


def f(a, b, c):
    print(a, b, c)


f(10, 20, 30)


def f1(*args):
    s = 0
    for x in args:
        s += x
    return s


print(f1(10, 20))
print(f1(10, 20, 30))


# note : *args exhausts positional arguments, we can not add more positional arguments after *args

def afunc(a, b, *c):
    print(f"a:{a}")
    print(f"b:{b}")
    print(f"c:{c}")


afunc(1, 2)
afunc(1, 2, 3)
afunc(1, 2, 3, 4)
afunc(1, 2, [3, 4, 5])


def my_avg(*args):
    s = 0
    for x in args:
        s += x
    n = len(args)
    return n and s / n


print(my_avg())
print(my_avg(1))
print(my_avg(1, 2))
print(my_avg(1, 2, 3))


def my_avg2(a, *args):
    # force avg function to pass atleast one arg
    try:
        s = a
    except e:
        return e

    for x in args:
        s += x
    n = len(args) + 1
    return s / n


print(my_avg2(5))
print(my_avg2(5, 6))
# print(my_avg2())

l2, l3 = [4], [4, 5]
print(my_avg2(*l2), my_avg2(*l3))


# keyword arguments
# to make keyword arguments mandatory, we create parameters after positional parameters have been exhausted

def f(a, b, *args, c):
    print(a, b, args, c)


f(1, 2, 3, 4, c=5)
f(1, 2, c=4)


def f(*args, d):
    print(args, d)


f(1, 2, 3, d='hello')
f(d='Welcome')


# we can force no positional arguments
def f(*, d):
    print(d)


f(d=1)


def f(a, b=1, *args, d, e=True):
    '''
    a: mandatory position arg
    b: optional position arg, default value specified
    args: other positional arguments
    d: mandatory keyword argument
    e: optional keyword argument  
    '''
    print(a, b, args, d, e)


f(11, 13, 14, 15, 16, d=10, e=False)


def f(a, b=1, *, d, e=True):
    '''
    a: mandatory position arg
    b: optional position arg, default value specified
    *: no other positional arguments
    d: mandatory keyword argument
    e: optional keyword argument
    '''
    print(a, b, d, e)


f(11, d=10)


# **kwargs
# no parameter can come after kwargs
def f(*, r, **kwargs):
    print(r, kwargs)


f(r=2)
f(r=1, color='red', metal='steel')


def f(**kwargs):
    print(kwargs)


f(a=1, b=2)


def f(*args, **kwargs):
    print(args, kwargs)


f(1, 2, 3, r='6', c='red', m='gold')


def calc_hi_low_avg(*args):
    l = args and min(args)
    m = args and max(args)
    a = (l + m) / 2
    return a


print(calc_hi_low_avg(2, 3, 4))
print(calc_hi_low_avg(10, 11, 12))

# timer function
import time


def time_it(fn, *args, repeat=1, **kwargs):
    start = time.perf_counter()
    for i in range(repeat):
        fn(*args, **kwargs)
    stop = time.perf_counter()
    return (stop - start) / repeat


print(time_it(print, 1, 2, 3, sep='-'))
print(time_it(print, 1, 2, 3, sep='=', repeat=2))


def compute_power_1(n, *, start=1, end):
    results = []
    for i in range(start, end + 1):
        results.append(n ** i)
    return results


print(compute_power_1(2, end=5))


def compute_power_2(n, *, start=1, end):
    return [n ** i for i in range(start, end + 1)]


print(compute_power_2(2, end=5))


# using generators
def compute_power_3(n, *, start=1, end):
    return (n ** i for i in range(start, end + 1))


print(list(compute_power_3(2, end=5)))

print(time_it(compute_power_1, 2, end=5000, repeat=5))
print(time_it(compute_power_2, 2, end=5000, repeat=5))
print(time_it(compute_power_3, 2, end=5000, repeat=5))
