def line():
    print('-' * 30)


def outer():
    x = 'Python'

    def inner():
        print(f"{x} is for everyone")

    inner()


outer()
line()


def outer():
    x = 'Python'

    def inner():
        print(f"{x} is for everyone")

    return inner


f = outer()
print(type(f))
print(f.__code__.co_freevars)
print(f.__closure__)
f()
line()

card = "King"


def outer(newcard):
    global card
    card = newcard

    def inner():
        return f"card is {card}"

    return inner


ace = outer("Ace")
print(ace())
queen = outer("Queen")
print(queen())

# at the time of call of closure, value of card is checked and displayed
# if we changed the order it will display different values

nine = outer("9")
ten = outer("10")
print(nine())
print(ten())

line()


def outer():
    alpha = 1
    beta = 2

    def inner():
        alpha = 10
        print(f"addres of beta = {str.upper(hex(id(beta)))} ")
        print(f"alpha = {alpha}, beta={beta}")

    return inner


fn = outer()
fn()
print(fn.__code__.co_freevars)
print(fn.__closure__)
line()


# modify free variable
def outer():
    count = 1

    def inc():
        nonlocal count
        count += 1
        return count

    return inc


fn = outer()
for i in range(3):
    print(fn())

line()


def outer():
    count = 1

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


f1 = outer()
for i in range(3):
    print(f"f1: {f1()}")
f2 = outer()
for i in range(3):
    print(f"f2: {f2()}")

line()
