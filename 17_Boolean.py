#PEP 285 bool class
# bool class was created to represent boolean values
# bool class is a subclass of int class, so it inherits all properties of an int class

# test whether bool is a subclass of int class
print(issubclass(bool, int))

# two constants are defined in Python, True and False
print(isinstance(True, bool), isinstance(False, bool))

# True and False are singleton objects of type

# is or == can be used
# is compares memory address
# ==  compares value

print((4>3) is True, (4>3) == True)

print(int(True), int(False))

# True and 1 are not same objects
# value of True is 1 tough
print(True is 1 , True == 1)

# bool(x) returns True is x is True , and False is x is False

# truth value of integer
# if integer is zero, its truth value is false , else True

print(f"Truth value of 0 is : {bool(0)}")
print(f"Truth value of 1 is {bool(1)}")
print(f"Truth value of -2 is {bool(-2)}")

# All objects in Python have associated truth values
# None , False, 0 , empty sequence , empty string, empty mapping evaluate to False
# classes have a special method, __bool__(self) or __len__(self)
# when we call bool(x) , python calls x.__bool__() or x.__len__() if dunder bool doesn't exist, if
# neither is defined then return True, else depends on return value of above dunder functions
# for integers
# __bool__(self):
#    return self != 0
# so when we say bool(100, python calls 100.__bool__()

print(bool([1,2,3]), bool([]))
print(bool((1,2)))
print(bool({}), bool({'1': 'one'}))
print(bool(''), bool('abc'))

from decimal import Decimal
from fractions import Fraction

print(bool(Fraction(0,1)), bool(Decimal('0.0')))

greek = ['alpha', 'beta', 'gamma']
if greek:
    print(greek[0])

# boolean operators : and, or , not

# operator precedence
# ()
# <, >, <=, >=, ==, !=, in, is
# not
# and
# or


print(True or True and False)
print((True or True) and False)

import string
# use parenthesis to make your code more readable
name = None

if name and name[0] in string.digits:
    print(name)
else:
    print('not found')


a = 3
b = 0

if b and a/b > 2:
    print("a is atleast twice of b")
else:
    print("otherwise")

name='K2'
import string

if not name:
    print('empty')
elif name[0] in string.digits:
    print('name should not start with digit')
elif name[0] in string.ascii_letters:
    print('alright, name starts with a letter')

# X or Y : if X is truthy return X else return Y
X,Y = 0,2
print(X or Y)

X,Y = -1,2
print(X or Y)

# X and Y : if X is false , return X else return Y

X,Y = 0,3
print(X and Y)

X,Y = 2,3
print(X and Y)

X, Y = [], [1,2,3]
print(X and Y)

X,Y = [1], [1,2,3]
print(X and Y)

name = input('enter name:')
name = name or 'N/A'  # can be used for setting up default values
print(name)

s, n = 1, 5
av = n and s/n
print(av)

s = None
def f(s):
    '''

    :param s:
    :return: if s is empty string or None, return empty string, else return first char
    '''
    return s and s[0] or ''
print(f(s))

# not: not is a builtin function that returns a boolean value
# not X : returns True if X is falsy , returns False if X is true

print(not [])
print(not [1,2])


