import ctypes
import sys
import gc

# Python memory manager takes care of storing/ retrieving objects from Heap
# when we write say x = 10, an integer object 10 is created in memory, and x is a reference
# to memory address pointing to object 10
# So variables in Python are references to objects in memory
# we can find out memory address referenced by variable using id()
# id() returns base 10, we can convert it to hexadecimal using hex()

x = 10
print(f"{id(x)} --> {x}")
print(f"{hex(id(x))} --> {x}")

message = "Hello"
print(f"{hex(id(message))} --> {message}")

y = x    # point y to same reference as x is pointing to in memory
print(f"{hex(id(y))} --> {y}")

print(f"y and x have same reference ? {y is x}")

# Reference count
print(f"Reference count of x : {sys.getrefcount(x) - 1}")
print(f"Reference count of x : {ctypes.c_long.from_address(id(x)).value}")

# list
my_list = [11, 3, 6, 7, 9, 13, 23, 15, 1]
print(f"Ref count for my_list: {sys.getrefcount(my_list)-1}")
print(f"Ref count for my_list: {ctypes.c_long.from_address(id(my_list)).value}")

your_list = my_list
print(f"Ref count for my_list: {ctypes.c_long.from_address(id(my_list)).value}")

your_list = None
print(f"Ref count for my_list: {ctypes.c_long.from_address(id(my_list)).value}")

id_my_list = id(my_list)
my_list = None
print(f"Ref count for memory address earlier referenced by my_list: {ctypes.c_long.from_address(id_my_list).value}")


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object found in gc"
    else:
        return "Object not found in gc"


class A:
    def __init__(self):
        self.b = B(self)
        print(f"A --> self: {hex(id(self))}, self.b: {hex(id(self.b))}")

class B:
    def __init__(self, a):
        self.a = a
        print(f"B --> self: {hex(id(self))}, self.a: {hex(id(self.a))}")


gc.disable()
my_var_a = A()

id_a = id(my_var_a)
id_b = id(my_var_a.b)
print(f"id_a: {id_a}, {hex(id_a)}")
print(f"id_b: {id_b}, {hex(id_b)}")

print(f"ref_count of id_a ({hex(id_a)}): {ref_count(id_a)}")
print(f"ref_count of id_b ({hex(id_b)}): {ref_count(id_b)}")

print(f"{hex(id_a)}: {object_by_id(id_a)}")
print(f"{hex(id_b)}: {object_by_id(id_b)}")

my_var_a = None
print(f"ref_count of id_a ({hex(id_a)}): {ref_count(id_a)}")
print(f"ref_count of id_b ({hex(id_b)}): {ref_count(id_b)}")

print(f"{hex(id_a)}: {object_by_id(id_a)}")
print(f"{hex(id_b)}: {object_by_id(id_b)}")

gc.collect()
print("Garbage collector ran")
print(f"{hex(id_a)}: {object_by_id(id_a)}")
print(f"{hex(id_b)}: {object_by_id(id_b)}")

print(f"ref_count of id_a ({hex(id_a)}): {ref_count(id_a)}")
print(f"ref_count of id_b ({hex(id_b)}): {ref_count(id_b)}")

gc.enable()



