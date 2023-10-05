# When an object is assigned to a variable for eg. a = 10
# that variable points to some object and we say variable is bound to that object
# that object can be accessed using variable name in various parts of the code
# but not everywhere in the code
# that variable name and its binding (var name and object) only exist in specific parts of the code
# the portion of code where varname/binding is defined is called as lexical scope of the variable
# these bindings are stored in namespaces
# each scope has its own namespace

# The Global Scope
# The global scope is essentially the module scope
# It spans a single file only
# Global scopes are nested inside builtin scopes

# The Local Scope
# When we create functions, we can create variable names inside those functions using assignments
# variables defined in a function code are not created until function is called
# everytime function is called a new scope is created
# variables defined inside the func are assigned to the scope of that func : func local scope

# Nested scopes
# scopes are often nested

from functools import partial

a = 10  # global scope of variable a within the module


def line():
    print('_' * 30)


def my_func(b):
    line()
    print("builtin scope", True)  # picked up from builtin scope
    print("global a is ", a)  # picked up from global scope
    print("local b is ", b)  # from local scope of function


my_func('beta')  # function is called
my_func('gamma')  # function is called


# local -> global -> builtin

def my_func_2():
    line()
    a = 900  # assignment tells that a will be local to this func and it masks global a variable
    print("local a ", a)


my_func_2()
print("global a", a)


def my_func_3():
    line()
    global a
    a = 1010
    print("from my_func3 a is ", a)


my_func_3()
print("from main module a is ", a)

bond_code = '007'


def func1():
    print('func1 bond_code : ', bond_code)  # function is only referencing variable and not assigning value to variable
    # so during compile time this variable will marked as non-local to func1


def func2():
    bond_code = "009"  # we are assigning value to variable so it will make variable as local to func
    print("func2 bond_code", bond_code)


def func3():
    global bond_code
    bond_code = "1001"  # referring to global scope
    print("func3 bond_code", bond_code)


def func4():
    # print("func4 bond_code", bond_code) # will error
    bond_code = "9999"
    print("func4 bond_code", bond_code)


line()
print("main module bond_code", bond_code)
func1()
print("main module bond_code", bond_code)
func2()
print("main module bond_code", bond_code)
func3()
print("main module bond_code", bond_code)
func4()
print("main module bond_code", bond_code)

global_var = 0


def set_globals():
    global alpha, beta, gamma
    alpha, beta, gamma = 1, 2, 3


set_globals()
print('globals:', alpha, beta, gamma)


# NON local scope
def outer_func():
    outer_var = 1

    def inner_func():
        inner_var = 2
        print(f'inner func: global_var={global_var},outer_var={outer_var}, inner_var={inner_var}')

    inner_func()
    print(f'outer func: global_var={global_var}, outer_var={outer_var}')


outer_func()

a = 10


def outer():
    a = 15

    def inner():
        print(f"inner: a={a}")

    inner()
    print(f"outer: a={a}")


outer()
print(f"global: a={a}")

a = 10


def outer():
    global a
    a = 20
    print(f"outer: a={a}")


outer()
print(f"global: a={a}")


def outer():
    code = '001'

    def inner():
        code = '002'
        print(f"inner: code:{code}")

    inner()
    print(f"outer: code:{code}")


outer()

print("non local example---")


def outer():
    code = '001'

    def inner():
        nonlocal code
        code = '002'
        print(f"inner: code={code}")

    inner()
    print(f"outer: code={code}")


outer()

print("nonlocal nested func ---")


def outer():
    msg = "hello"

    def inner1():
        def inner2():
            nonlocal msg
            msg = "inner2-hello"

        inner2()

    inner1()
    print(f"outer: msg={msg}")


outer()

print("another example ------")


def outer():
    x = 'hello'

    def inner1():
        x = 'python'

        def inner2():
            nonlocal x
            x = 'monty'

        print(f'before inner2 call, x = {x}')
        inner2()
        print(f"after inner2 call, x={x}")

    print(f"before inner1 call x={x}")
    inner1()
    print(f"after inner1 call x={x}")


outer()

print("----- another example -----")


def outer():
    x = "hello from outer"

    def inner1():
        nonlocal x
        x = "hello from inner1"

        def inner2():
            nonlocal x
            x = "hello from inner2"

        print(f"before inner2 called, x={x}")
        inner2()
        print(f"after inner2 called, x={x}")

    print(f"before inner1 called, x={x}")
    inner1()
    print(f"after inner1 called, x={x}")


outer()

print("----- Another Example -----")
alpha = 100


def outer():
    alpha = 'python'

    def inner1():
        nonlocal alpha
        alpha = 'monty'

        def inner2():
            global alpha
            alpha = "hello"

        print(f"before inner2 call, alpha={alpha}")
        inner2()
        print(f"after inner2 call, alpha={alpha}")

    print(f"before inner1 call , alpha={alpha}")
    inner1()
    print(f"after inner1 call, alpha={alpha}")


print(f"before outer call, alpha={alpha}")
outer()
print(f"after outer call, alpha={alpha}")

############
print('-' * 30)
k = 1


def outer():
    k = 10
    print(f"in outer: k={k}")

    def inner1():
        global k
        k = 2
        print(f"in inner: k={k}")

        def inner2():
            nonlocal k
            k = 300
            print(f"inner2: k={k}")

        print(f"before inner2 call, k={k}")
        inner2()
        print(f"after inner2 call, k={k}")

    print(f"before inner1, k={k}")
    inner1()
    print(f"after inner1, k={k}")


print(f"before outer call, k={k}")
outer()
print(f"after outer call, k={k}")
