def move_by(die_input):
    if die_input <= 0:
        raise ValueError("Invalid input: Die number should be > 0")
    elif die_input > 6:
        raise ValueError("Invalid input: Die number should be <=6")
    else:
        print(f"move by {die_input}")


# Test cases

try:
    result = move_by(-3)
except ValueError as e:
    print(e)

try:
    result = move_by(7)
except ValueError as e:
    print(e)

try:
    result = move_by(5)
except ValueError as e:
    print(e)


# define custom user defined exception
# exception is defined as class

class DieInputError(Exception):
    pass


class DieInputLowerBoundError(DieInputError):
    pass


class DieInputUpperBoundError(DieInputError):
    pass


def move_by(die_input):
    if die_input <= 0:
        raise DieInputLowerBoundError("Invalid input: Die number should be > 0")
    elif die_input > 6:
        raise DieInputUpperBoundError("Invalid input: Die number should be <=6")
    else:
        print(f"move by {die_input}")


print("... Many throws ...")
for die in [-1, 4, 7, 2, 0]:
    try:
        move_by(die)
    except DieInputLowerBoundError as e:
        print(e)
    except DieInputUpperBoundError as e:
        print(e)


def get_data(data, index):
    try:
        return data[index]
    except IndexError:
        print('Invalid index')


letters = ['A', 'B', 'C', 'D']
try:
    print(letters[11])
except IndexError as e:
    print(f"We got exception related to Index : {e}")
except Exception as e:
    print(e)

print(".... add_elements...")


def add_elements(data1, data2, index):
    try:
        return data1[index] + data2[index]
    except IndexError as e:
        print("invalid index, plz check")
    except TypeError as e:
        print("datatype mismatch to add")


try:
    sum_up = add_elements([1, 2, 3, 4], [4, 5, 6, 7, 8, 9], 5)
except IndexError as e:
    print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print(e)
