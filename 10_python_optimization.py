# every thing is an object
import platform

print(platform.python_implementation())
print(platform.python_version())


def f():
    print("hello")


# f: is name of the function
# f(): invokes the function
print(type(f))
print(hex(id(f)))

f = lambda x: x * 2

print(type(f))
print(hex(id(f)))

# any object can be assigned to a variable
# so function can also be assigned to a variable
# function can also be passed as an argument
# function can also be returned
x = f
print(x(2))


def fun(f):
    return f(5)


print(f"{fun(f)}")

b = int(5)
print(b)

c = int()
print(c)

d = int('101', base=2)
print(d)

# help(int)

print(bin(13))

square = lambda x: x ** 2
cube = lambda x: x ** 3


def select_fun(f_id):
    if f_id == 1:
        return square
    elif f_id == 2:
        return cube
    else:
        return None


fun_choice = int(input("Enter 1 for square and 2 for cube:"))
math_fun = select_fun(fun_choice)
print(math_fun(5))

result = select_fun(fun_choice)(5)
print(result)


def execute_fun(f, n):
    return f(n)


print(execute_fun(select_fun(fun_choice), 5))

# pre cached (interned) range of integers [-5, 256]
a = 10
b = int(10)
c = int('1010', base=2)
d = 5 + 5
print(hex(id(a)), hex(id(b)), hex(id(c)), hex(id(d)))

# some strings are also interned by python
# not all strings are interned by Python
# we can force a string to be interned using sys.intern()

a = "hello world"
b = "hello world"
print(f"is a and b referring to same address? {a is b}")

import sys

a = sys.intern("@#187 Rahatani")
b = sys.intern("@#187 Rahatani")
c = "@#187 Rahatani"
print(f"{hex(id(a))}, {hex(id(b))}, {hex(id(c))}")

import time


def compare_intern(n):
    a = sys.intern("this_is_a_long_string_for_comparison")
    b = sys.intern("this_is_a_long_string_for_comparison")
    for i in range(n):
        if a is b:
            pass


start = time.perf_counter()
compare_intern(50000)
end = time.perf_counter()
print(f"{end - start}")


def compare_string(n):
    a = "this is a long string for_comparison"
    b = "this is a long string for comparison"
    for i in range(n):
        if a == b:
            pass


start = time.perf_counter()
compare_string(50000)
end = time.perf_counter()
print(f"{end - start}")


# Set membership is faster than list or tuple membership
# instead of x in [1,2,3] or x in (1,2,3), write x in {1,2,3}

def my_func():
    mins = 24 * 60  # gets pre calculated and stored
    t = (1, 2) * 5  # gets pre calculated and stored
    x = 'abc' * 3  # gets pre calculated and stored
    y = 'abcdefghij' * 3  # does not get pre calculated and stored
    z = ['a', 'b'] * 3


print(my_func.__code__.co_consts)

import string

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)


def membership_test(n, container, e):
    for i in range(n):
        if e in container:
            pass


start = time.perf_counter()
membership_test(10000, char_list, 'z')
end = time.perf_counter()
print(f"list membership test: {end - start}")

start = time.perf_counter()
membership_test(10000, char_tuple, 'z')
end = time.perf_counter()
print(f"tuple membership test: {end - start}")

start = time.perf_counter()
membership_test(10000, char_set, 'z')
end = time.perf_counter()
print(f"set membership test: {end - start}")
