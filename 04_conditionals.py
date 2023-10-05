# conditional statement if-else-elif

# example
yest_temp_degree_celcius = float(input("Enter yesterday's temperature:"))
today_temp_degree_celcius = float(input("Enter today's temperature:"))

if today_temp_degree_celcius > yest_temp_degree_celcius:
    print("Today is hotter than yesterday")
elif today_temp_degree_celcius < yest_temp_degree_celcius:
    print("Yesterday was hotter than today")
else:
    print("Today is same temperature as yesterday")

# example
statement = True
if statement:
    print("You spoke truth")
else:
    print("You lied")

# example
msg = ""
if not msg:
    print("there is is no message")
else:
    print(f"message is {msg}")

# categorise age
age = int(input("Enter age in years:"))

if 0 <= age <= 1:
    print("Infant")
elif 1 < age <= 3:
    print("Toddler")
elif 3 < age <= 5:
    print("Preschooler")
elif 5 < age <= 12:
    print("Childhood")
elif 12 < age <= 17:
    print("Teenager")
elif age > 17:
    print("Adult")

# example
signal = input("enter signal color:")
action = 'go' if signal == 'green' else 'wait'
print(f"You need to {action}")
