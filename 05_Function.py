# Functions

# builtin function
nums = [11, 21, 36]
num_of_elements = len(nums)
print(f"No. of elements: {num_of_elements}")

# sometimes we have to import
from math import sqrt

x = 256
sq = sqrt(x)
print(f"square root of {x} is {sq}")


# user defined function
def print_funny_msg():
    print("A funny message : ha ha ha")


# invoke function
print_funny_msg()


def replicate_message(msg: str, n: int = 1):
    return str.rstrip((msg + ' ') * n)


print(replicate_message("Hello"))
print(replicate_message("Echo", 3))


def parent_fun():
    return child_fun()


def child_fun():
    return ('Hey Parent, Child crying')


print(parent_fun())

# lambda

triple = lambda x: 3 * x
print(type(triple))
x = 100
triple_x = triple(x)
print(x, triple_x)
