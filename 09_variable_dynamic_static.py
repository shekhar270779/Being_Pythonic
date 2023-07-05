# static vs dynamic type of variables

# languages like C, C++, Java, Swift are statically typed
# String my_var = "hello"   : we are declaring that my_var is of String datatype
# my_var = 10  : this will error out as we are trying to assign int to my_var , which is of String datatype

# Python is dynamically typed
# my_var = "Hello"  : my_var is just a reference to memory location where object "Hello" is stored
# No datatype is attached to my_var
# We can very easily make my_var point to some other object like my_var = 11
# what changed is the type of object that my_var has been referring to
# type() to find the datatype of object which variable refers to

my_var = 10
print(f"my_var is pointing to object of type: {type(my_var)} and object is {my_var}")

my_var = "hello"
print(f"my_var is pointing to object of type: {type(my_var)} and object is {my_var}")

my_var = lambda x : x * 5
print(f"my_var is pointing to object of type: {type(my_var)} and for arg 2 , value is {my_var(2)}")

a_var = 10
print(f"{a_var}: {hex(id(a_var))}")
a_var += 5
print(f"{a_var}: {hex(id(a_var))}")

throw1 = 6
throw2 = 6
print(f"{hex(id(throw1))}, {hex(id(throw2))}")
print(f"is throw1 and throw2 pointing to same location? {throw1 is throw2}")

# An object whose internal state can be changed is called mutable
# An object whose internal state can not be changed is called immutable

a = [1, 2]
b = [3, 4]

print("Before update of list")
t = (a, b)
print(f" address of list a : {hex(id(a))}")
print(f"tuple: {t}")
a.append(11)
print("After update of list")
print(f" address of list a : {hex(id(a))}")
print(f"tuple: {t}")

my_list = [11, 12, 4]
print(f"memory address of my_list : {hex(id(my_list))}")
my_list.append(15) # it changes internal state of list, so memory address of my_list will not change
print(f"memory address of my_list : {hex(id(my_list))}")

# concatenation changes creates a new list
my_list = my_list + [16]
print(f"memory address of my_list : {hex(id(my_list))}")

# function arguments and mutability

# immutable objects are safe from unintended side-effects

def greet(s):
    print(f"s: {s}, id of s: {hex(id(s))}")
    s = 'Hello ' + s
    print(f"s: {s}, id of s: {hex(id(s))}")
    return s

my_str = "World"
print(f"my_str: {my_str}, id of s: {hex(id(my_str))}")
print(greet(my_str)) # reference of my_str is passed to greet()
print(f"my_str: {my_str}, id of s: {hex(id(my_str))}")

# mutable objects are not safe from unintended side effects
def process(lst):
    print(f"elements of list are : {lst}")
    lst.append(10)


my_list = [10, 11, 12]
process(my_list)
print(my_list)

# Term shared reference means two variable referencing same object in memory

x = [1,2,3]
y = x
print(f"{hex(id(x)) == hex(id(y))}")
print(x, y)
y.append(4)
print(f"{hex(id(x)) == hex(id(y))}")
print(x, y)

# python creates shared memory reference for immutable object
u = 999
v = 999
print(f"{hex(id(u))}, {hex(id(v))}")
v = 1000
print(f"{hex(id(u))}, {hex(id(v))}")

# python does not create shared memory reference for immutable object
l = [1,2,3,4]
m = [1,2,3,4]
print(f"{hex(id(l))}, {hex(id(m))}")
print(f"{l==m}")

## variable comparison
# we can compare memory address of variables with operator 'is'
var_1 = "hello"
var_2 = "hello"

print(f"{var_1 is var_2}")

# to compare internal state i.e. data we use ==  [equality operator]
print(f"{var_1 == var_2}")

# None object
# None object is assigned to memory to indicate these are not set
# None is a real object, memory manager will always use shared reference when assigning variable to None object

print(f"id of None: {hex(id(None))}")
a = None
b = None
print(f"id of a: {hex(id(a))}")
print(f"id of b: {hex(id(b))}")
print(f"{a is None}")












