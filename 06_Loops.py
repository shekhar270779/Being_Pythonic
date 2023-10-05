import string

# loops

# While loop

while True:
    print("while loop continues ...")
    response = input("type q to quit:")
    if str.lower(str.rstrip(response)) == "q":
        break


def check_password(x: str):
    ''''Check whether password meets conditions
    '''

    # check for minimum length 6
    def check_len(x):
        return str.__len__(x) >= 6

    # check for at least 1 upper case letter
    def check_uppercase(x):
        for _ in x:
            if _ in string.ascii_uppercase:
                return True
        else:
            return False

    return check_len(x) and check_uppercase(x)


for attempt in range(3):
    msg = input("enter password:")
    if check_password(msg):
        print("password ok")
        break
    else:
        if attempt < 2:
            print("password not ok,try again")
        else:
            print('all attempts exhausted')

# continue
for i in range(11):
    if i % 2 == 0:
        continue
    print(i, end=', ')
print()

# add number in list if not already there
nums = [1, 11, 5, 7, 9]
x = int(input("enter a number:"))
# using else of while loop
idx = 0
while idx < len(nums):
    if x == nums[idx]:
        print(f"Found {x} in list at index {idx}")
        break
    idx += 1
else:
    print(f"Number {x} not found in list, so adding it")
    nums.append(x)

print(f"list: {nums}")

##
x, y = 0, 3

while x < 6:
    x += 1
    y -= 1
    print('-' * 30)

    try:
        result = x / y
    except ZeroDivisionError:
        print(f"Zero division error: {x}/{y}")
        # continue
        break
    finally:
        print("finally always executes")
    print(f"result: {result}")
else:
    print("else block of finally")

# In Python, an iterable is an object capable of returning values one at a time

# range() is an iterable, when loop calls it , it returns a value
for i in range(5):
    print(i)

#  iterating over a list and unpacking each element
for tens, unit in [(1, 2), (3, 4), (5, 6)]:
    print(f"number: {tens * 10 + unit}")

# else in for loop
for i in range(5):
    try:
        res = 15 / (i - 2)
    except ZeroDivisionError:
        print('zero division error hit')
        break
    finally:
        print(f'end of for loop: {i}')
else:
    print("didn't hit break")

# enumerate
message = 'Hello'
for i, x in enumerate(message):
    print(f"index {i}: {x}")
