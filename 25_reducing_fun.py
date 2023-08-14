# These are functions that recombine iterable recursively, ending up with a single return value
# also called as accumulators, aggregators or folding functions

def find_max(*args):
    mx = args[0]
    for i in range(1, len(args)):
        if args[i] > mx:
            mx = args[i]
    return mx

print("Max:", find_max(4,6,12,3,9,5))

###############
max_value = lambda x, y: x if x > y else y
l = [10, 17, 12, 15, 19, 14]
def max_sequence(sequence):
    mx = sequence[0]
    for e in sequence[1:]:
        mx = max_value(mx, e)
    return mx

print("Max:", max_sequence(l))
####################
def sum_up(*args):
    s = 0
    for e in args:
        s += e
    return s

print("Sum:", sum_up(10, 11, 12, 13, 14))
########################
min_value = lambda x, y: x if x < y else y


def _reduce(fn, sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = fn(result, e)
    return result

print(f"max: {_reduce(max_value, l)}, min: {_reduce(min_value, l)}, sum:{_reduce(sum_up, l)}")
################

print(_reduce(lambda x,y: x if x > y else y, [10,11,12,13]))
print(_reduce(lambda x,y: x if x < y else y, [10,11,12,13]))
print(_reduce(lambda x,y: x+y, [10,11,12,13]))

# python has a reduce function that works with any iterable
from functools import reduce

l = [10, 11, 12, 13]
print(reduce(lambda x,y: x if x > y else y, l))

name='gaurav'
smallest_char = reduce(lambda x, y: x if x < y else y , name)
largest_char = reduce(lambda x, y: x if x > y else y, name)
distance_name = ord(largest_char) - ord(smallest_char)
print(f"distance of name: {distance_name}")

# some builtin reducing functions
# min , max, sum, any , all

reply = any([5> 6, 6==7, 7 < 8]) # if any element is true , it returns true
print(reply)

reply = all([1==1, 2>3]) # if all elements are true it returns true else false
print(reply)

def _any(sequence):
    for e in sequence:
        if e :
            return True
    else:
        return False

print(_any([10>11, 11>10, 11>12]))
print(_any([10>11, 11>12]))

def _all(sequence):
    for e in sequence:
        if not e:
            return False
    else:
        return True


print(_all([10>11, 11>10, 11>12]))
print(_all([10>9, 11>10]))

print(reduce(lambda x, y : bool(x) or bool(y), [10, None, '', 0]))
print(reduce(lambda x, y : bool(x) and bool(y), [10, None, '', 0]))

# product of all elements in iterable
def _mul(sequence):
    m = sequence[0]
    for e in sequence[1:]:
        m = m * e
    return m

print(_mul([10,11,12]))

# factorial n = 1 * 2 * 3 * ....n
n=6
facto = reduce(lambda x , y: x* y, range(1, n+1))
print('facto is ', facto)

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1), 1)

print('factorial of 5 is', factorial(5))

_any = lambda x, y: bool(x) or bool(y)
_all = lambda x, y: bool(x) and bool(y)

s1 = [1,2,3,4,5]
s2 = [True,None,'']
print(reduce(_any, s1), reduce(_all, s1))
print(reduce(_any, s2), reduce(_all, s2))
