def outer():
    x = 'Python'

    def inner():
        print(f"{x} rocks !!")  # x refers to the one in its outer scope and this nonlocal var is also called
        # as free variable. So free variable x within inner is defined somewhere else
        # so inner and var x which is defined in outer scope are bound together
        # that is called as closure, we basically say inner encloses variable x

    inner()


outer()


# x is a free variable in inner, it is bound to variable x in outer scope when outer runs

# what if we return inner from outer
def outer():
    x = 'Python'

    def inner():
        return (f"{x} rocks again")

    return inner


fn = outer()
print("Calling fn:", fn())


# python first creates a memory address (say mem1) and store string object 'Pyhton' there
# then it creates a "cell" object, which references mem1 memory address.
# later when x variable are referenced from outer and inner functions,
# outer's x and inner's x both point to "cell" object, and cell in turn points to actual string object
# thats how variable are shared in different scope

# We can think of Closures as a function + an extended scope in which free variables are defined
# free variable's value is the object that the cell points to
# so every time function in closure is called and free variable is referenced :
#  Python looks up cell objects, and whatever the cell points to

def outer():
    a = 100
    x = "Python"
    mem_x_outer = hex(id(x))
    print("outer: memory address of x ", mem_x_outer)

    def inner():
        a = 1  # this is local to inner so it will not be a part of closure
        mem_x_inner = hex(id(x))
        print("inner memory address of x:", mem_x_inner)
        print(f"{x} Rocks")  # x is nonlocal

    return inner


fn = outer()  # fn points to inner + extended scope x
fn()
print(fn.__code__.co_freevars)
print(fn.__closure__)

import ctypes

print("...Counter...")


# modify free variables
def counter(delta):
    count = 0
    memadd_count = id(count)
    memadd_delta = id(delta)
    print(f"memory address of count is {hex(memadd_count)}")
    print(f"value from memadd_count is {ctypes.cast(memadd_count, ctypes.py_object).value}")
    print(f"memory address of delta is {hex(memadd_delta)}")
    print(f"value from memadd_delta is {ctypes.cast(memadd_delta, ctypes.py_object).value}")

    def increase_count():
        nonlocal count, delta
        count += delta
        return count

    return increase_count


plus5 = counter(5)

# lets call plus5 2 times
for i in range(1, 3):
    print(f"...Call {i}....")
    print(f"value is {plus5()}")
    print(plus5.__code__.co_freevars)
    print(plus5.__closure__)

print("_" * 30)


def counter(delta=1):
    count = 1

    def inc():
        nonlocal count, delta
        count += delta
        return count

    return inc


plus5 = counter(5)
print(plus5())
print(plus5.__code__.co_freevars)
print(plus5.__closure__)

print("........ Multiple instances of closure .......")


def counter(delta):
    count = 1

    def inc():
        nonlocal count, delta
        count += delta
        return count

    return inc


plus2 = counter(2)
plus3 = counter(3)

print(f"plus2: {plus2.__code__.co_freevars}")
print(f"plus2: {plus2.__closure__}")
print(f"plus3: {plus3.__code__.co_freevars}")
print(f"plus3: {plus3.__closure__}")

for i in range(4):
    print(plus2(), plus3())

# can we share extended scope ?
print("......Scope sharing ........")


def outer(delta):
    count = 0

    def inner1():
        nonlocal count
        nonlocal delta
        count += delta
        return count

    def inner2():
        nonlocal count, delta
        count += delta
        return count

    return inner1, inner2


f1, f2 = outer(2)
for i in range(4):
    print(f1(), f2())
    print(f"f1: {f1.__closure__}")
    print(f"f2: {f2.__closure__}")

print("Note issue with shared extended scope in below example:")
adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)

for adder in adders:
    print(adder(10))

# ---------
print("-------------------------------")
adders = []
for n in range(1, 4):
    adder = lambda x: x + n
    adders.append(adder)
    print(adder(10))

# since n refers to same value as in loop
# so n keeps changing and its final value is taken

for adder in adders:
    print(adder(10))
