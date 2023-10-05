# Functions are first class citizen/objects
# Functions have attributes like __doc__, __annotations__
# we can attach our own attribute with functions

def my_fun(a: 'number' = 0, b: 'number' = 0, *, verbose=False) -> 'number':
    '''
    This function returns sum of two input numbers
    :param a: first input number
    :param b: second input number
    :return: returns the sum of two input numbers
    '''
    if verbose:
        print(a + b)
    return a + b


print(my_fun(10, 5))

my_fun.category = 'math'
my_fun.sub_category = 'arithmetic'

print(my_fun.category)
print(my_fun.sub_category)
print(my_fun.__doc__)
print(my_fun.__annotations__)

# dir() it helps to find all attributes of a function
print(dir(my_fun))

x = my_fun
print(x(10, 20))
print(x.__name__)  # __name__ represents name of the function
print(x.__defaults__)  # to get default values of positional parameters
print(x.__kwdefaults__)  # to get default values of key word arguments
print(my_fun.__code__.co_varnames)
print(my_fun.__code__.co_argcount)

import inspect

print(inspect.isfunction(my_fun), inspect.ismethod(my_fun))
# difference between method and function is , a method is bound to an object whereas function is not.
print("Source Code of my_fun is")
print(inspect.getsource(my_fun))

p2 = lambda x: x ** 2
# to get source code of function
print(inspect.getsource(p2))

# to find module in which function was created
print(inspect.getmodule(p2))
print(inspect.getmodule(print))


def find_nth_largest(n, *args) -> 'nth largest number':
    '''
    Find nth largst number from given  numbers
    :param n: nth largest
    :param args: numbers
    :return: find nth largest number
    '''
    # TODO: complete the code
    pass


print(inspect.getcomments(find_nth_largest))


def f(a: int, b: int = 2, c: 'string' = None, *args: 'additional position args', s, d='key-2', **kwargs):
    pass


print('_' * 50)
for param in inspect.signature(f).parameters.values():
    print(f"{param.name}, {param.default}, {param.annotation}, {param.kind}")


# TODO: complete this function
def f(a: 'mandatory positional',
      b: 'optional positional parameter' = 2,
      c: 'optional positional parameter' = 3,
      *args: 'other positional parameters',
      kw1: 'mandatory keyword parameter',
      kw2: 'optional key word parameter' = 'OK',
      kw3: 'optional keyword parameter' = True,
      **kwargs: 'extra keyword parameters') -> 'print parameters':
    ''' a function with some parameters
    :param a: mandatory
    :param b: optional
    :param c: optional
    :param args: optional
    :param kw1: mandatory kw param
    :param kw2: optional kw param
    :param kw3: optional kw param
    :param kwargs: optional key word parameters
    :return:
    '''
    i, j = 10, 20
    print(a, b, c, args, kw1, kw2, kw3, kwargs)
    return i + j


print(f.__doc__)
print(f.__annotations__)
f.short_desc = 'a simple function'
print(f.short_desc)
print(dir(f))


def call_f(afunc):
    print(afunc.__name__)


def hello():
    return 'hello ' + x


def bye():
    return 'bye ' + x


for k in [hello, bye]:
    print(f"Calling {k.__name__}")

print(f.__defaults__)
print(f.__kwdefaults__)
print(f.__code__.co_varnames)

import inspect
from inspect import isfunction, ismethod, isroutine

print(isfunction(f), ismethod(f), isroutine(f))


class MyClass:
    def f1(self):
        pass


a = MyClass()
print(ismethod(a.f1), isfunction(MyClass.f1))

print(inspect.getsource(f))
print(inspect.getmodule(f))
print(inspect.getcomments(f))
print(inspect.signature(f))

sig = inspect.signature(f)
for param in sig.parameters.values():
    print(f"name: {param.name}")
    print(f"Default: {param.default}")
    print(f"Annotation: {param.annotation}")
    print(f"Kind:{param.kind}")
    print("_" * 30)

for param in inspect.signature(divmod).parameters.values():
    print(param.name, param.kind)

# callables
# any object that can be called using () is called callable
# callable always return a value
# functions, methods are callables
# many other objects are also callable
# to find whether an object is callable or not, we can use builtin function callable


print(f"is print callable? {callable(print)}")
print(f"string method is callable ? {callable('abc'.upper)}")


# different types of callables
# builtin functions: len, print
# builtin methods: str.upper , list.append
# user defined functions : functions created using def or lambda
# methods
# classes and class instances
# generators, coroutines

class MyClass:
    def __init__(self, x=0):
        print('initialising...')
        self.counter = x

    def __call__(self, x=1):
        print('updating counter...')
        self.counter += x


m = MyClass(100)
print(callable(MyClass), callable(a))

n = MyClass(200)
MyClass.__call__(n, 90)
print(n.counter)

print(callable(n))
n(60)
print(n.counter)
