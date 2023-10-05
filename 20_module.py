# module : when module is loaded all the code is executed immediately

from datetime import datetime
import time


def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print(f"{dt}: {msg}")


log("hello world")
time.sleep(1)
log("how are you")
time.sleep(3)
log("All well")
time.sleep(1)
t1 = datetime.utcnow()
log("Jolly good", dt=t1)
time.sleep(1)
t2 = datetime.utcnow()
log(dt=t2, msg="Perfect")


# notice the issue below when we set mutable object as a default value
def f(days=['saturday', 'sunday'], msg=None):
    print(msg, 'before', days)
    days.insert(0, 'monday')
    print(msg, 'after', days)


f(msg='first')
f(msg='second')


def add_item(name, qty, unit, grocery):
    grocery.append(f"{name}: {qty}{unit}")
    return grocery


store1 = []
store2 = []
add_item('apples', 2, 'kg', store1)
add_item('banananas', 6, 'unit', store2)
add_item('guavas', 12, 'unit', store1)
print(store1, store2)


def add_item(name, qty, unit, grocery=[]):
    grocery.append(f"{name}: {qty}{unit}")
    return grocery


store1 = add_item('apples', 2, 'kg')
add_item('guavas', 12, 'unit', store1)
store2 = add_item('banananas', 6, 'unit')
print(store1, store2)
print(store1 is store2)


def add_item_fix(name, qty, unit, grocery=None):
    if not grocery:
        grocery = []
    grocery.append(f"{name}: {qty}{unit}")
    return grocery


store1 = add_item_fix('apples', 2, 'kg')
add_item('guavas', 12, 'unit', store1)
store2 = add_item_fix('banananas', 6, 'unit')
print(store1, store2)
print(store1 is store2)


def factorial(n):
    if n < 1:
        return 1
    else:
        print(f"Calculating {n}")
        return n * factorial(n - 1)


print(factorial(5))


def factorial_1(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print(f"Calculating {n}")
        result = n * factorial_1(n - 1)
        cache[n] = result
        return result


print(factorial_1(3))
print(factorial_1(5))
