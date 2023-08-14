from functools import reduce, partial
import operator as op
l = [2, 3, 4, 5]
multiply_result = reduce(lambda x,y: x*y, l)
print(multiply_result)

smallest_result = reduce(lambda x, y: x if x < y else y, l)
sum_result = reduce(lambda x, y: x + y, l)
largest_result = reduce(lambda x, y: x if x > y else y, l)
print(smallest_result, sum_result, largest_result)

concat_result = reduce(lambda x, y: x + '-' + y, ['red', 'blue', 'green'])
print(concat_result)

########
print("Arithmetic functions in operator module")
print("add", op.add(10,15))
print("mul", op.mul(10, 15))
print("pow", op.pow(2,5))
print("mod", op.mod(10, 3))
print("floordiv", op.floordiv(10, 3))
print("negate", op.neg(-10), op.neg(10))

nums = [2, 3, 4, 5]
print("sum", reduce(op.add, nums))
print("mul", reduce(op.mul, nums))

print("Comparison and Boolean operators")
print("lt", op.lt(10, 6))
print("le", op.le(10, 10))
print("eq", op.eq(5,5))

s1 = ["hello", "welcome"]
s2 = ["thank you", "please"]
print("concat", op.concat(s1, s2))
print("contains", op.contains(s1, "hello"))
print("getitem", op.getitem(s1, 0))

ith_item = lambda x, i: op.getitem(x, i)
first = partial(ith_item, i=0)
last = partial(ith_item, i=-1)
print("first", first(s1))
print("last", last(s1))

z_list = ['alpha', 'beta']
print("z_list", z_list)
set_ith = lambda s, value, i: op.setitem(s, i, value)

set_first = partial(set_ith, i=0)
set_first(z_list, 'numero uno')
print(first(z_list))

set_last = partial(set_ith, i=-1)
set_last(z_list, 'end')
print(last(z_list))

z_list.append("final")
print("z_list", z_list)
delete_ith = lambda x, i: op.delitem(x, i)
delete_first = partial(delete_ith, i=0)
delete_last = partial(delete_ith, i=-1)

delete_first(z_list)
print(first(z_list))
delete_last(z_list)
print(last(z_list))
print("z_list", z_list)

y_list = ["pi", "epsilon", "lambda", "g", "G"]
second = op.itemgetter(1)
print("second", second(y_list))
third = op.itemgetter(2)
print("third", third(y_list))

first_3 = op.itemgetter(0,1,2)
print(first_3(y_list))

last_3 = op.itemgetter(-1, -2, -3)
print(last_3(y_list))

# Attribute getter attrgetter
class XYZ:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


obj = XYZ(10, 20, 30)
first = op.attrgetter('a')
print(first(obj))

second = op.attrgetter('b')
print(second(obj))

third = op.attrgetter('c')
print(third(obj))

first_two_attributes = op.attrgetter('a', 'b')
print(first_two_attributes(obj))

print("First 3 attributes:", op.attrgetter('a', 'b', 'c')(obj))

s = "python"
print(op.attrgetter("upper")(s)())

print(op.methodcaller("upper")(s))

smaller = lambda x,y: x if op.lt(x, y) else y
smallest = lambda sequence: reduce(smaller, sequence)
some_nums = [19, 16, 29, 34, 20]
print("smallest of some_nums", smallest(some_nums))

class SomeClass:
    def __init__(self):
        self.x, self.y, self.z = 24, 25, 26
        self.e, self.j, self.o, self.t, self.m, self.h = 5, 10, 15, 20, 13, 8

obj = SomeClass()
for prop in ['x', 'y', 'z', 't','m']:
    print(op.attrgetter(prop)(obj))

larger = lambda x, y: x if op.gt(x, y) else y
largest = lambda sequence: reduce(larger, sequence)
print("largest of some_nums", largest(some_nums))

complex_nums = [5+2j, -4+3j, 6+5j, 3+4j]
print(sorted(complex_nums, key = op.attrgetter('real')))

# emp (name, age, weight)
emp = [('Ram', 32, 90), ('Shyam', 23, 76),  ('Abhiram', 42, 89), ('Ria', 42, 67)]

# sort on the basis of age, older first
print("older first", sorted(emp, key = op.itemgetter(1,0), reverse=True))


class Wish:
    def __init__(self, msg='hello'):
        self.msg = msg
    def lets_wish(self, person):
        print(f"{self.msg}, {person}")


bday = Wish("Happy B'day")
anniversary = Wish("Happy Anniversary")

greet = lambda ppl, wish_obj: op.methodcaller('lets_wish', ppl)(wish_obj)
some_people = ["Ravi", "Gaurav", "Anushree"]
for p in some_people:
    for w in [bday, anniversary]:
        greet(p, w)












