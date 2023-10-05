def outer():
    x = "Python"

    def inner():
        print(f"{x=}")

    inner()


outer()


############################
def outer():
    x = "Python"

    def inner():
        print(f"{x=}")
        print(f"memory add of x : {hex(id(x))}")

    return inner


fn = outer()
print("freevars:", fn.__code__.co_freevars)
print("closure:", fn.__closure__)
print(fn())


##################
def outer():
    skill = 'Java'

    def inner():
        nonlocal skill
        skill = 'Python'
        return skill

    return inner


fn = outer()
print(fn.__code__.co_freevars)
print(fn())


############

def outer():
    counter = 0

    def increase_counter():
        nonlocal counter
        counter += 1
        return counter

    return increase_counter


fn = outer()
print(fn.__code__.co_freevars)
for i in range(1, 5):
    print(f"Counting {fn()}")


###########
def outer():
    dummy = 0

    def inc():
        nonlocal dummy
        dummy += 1
        return dummy

    return inc


fn = outer()
print(fn.__code__.co_freevars, fn.__closure__)
print(hex(id(0)))
print(fn())
print(fn.__code__.co_freevars, fn.__closure__)
print(hex(id(1)))

############
print("POWER")


def power(n):
    def inner(x):
        return x ** n

    return inner


square = power(2)
cube = power(3)
print(fn.__code__.co_freevars)
for i in range(2, 6):
    print(square(i), cube(i))

#########
print("Adder")
adders = []
for n in range(1, 5):
    adders.append(lambda x: x + n)

for i in range(len(adders)):
    print(adders[i](10))


def outer():
    adders = []

    def inner():
        for n in range(1, 5):
            adders.append(lambda x: x + n)
        for i in range(len(adders)):
            print(adders[i].__code__.co_freevars, adders[i].__closure__)
            print(adders[i](10))

    inner()


fn = outer()
print(fn())
