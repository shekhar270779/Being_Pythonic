class Greet:
    def say_hello(self, name):
        print(f"Hello {name} !!")


greet = Greet()
greet.say_hello("Sam")


#########
class Car:
    def __init__(self, name, brand):
        self.model_name = name
        self.brand_name = brand

    def launch(self):
        print(f"{self.brand_name} has launched a new model car {self.model_name}")


c1 = Car("i10", "Hyundai")
c1.launch()


##########
class Bike:
    def __init__(self):
        self.current_state = 'Stop'
        self.speed = 0

    def start(self):
        self.current_state = 'Start'
        self.speed = 10

    def stop(self):
        self.current_state = 'Stop'
        self.speed = 0

    def speed_up(self, speed):
        if self.current_state == 'Stop':
            self.start()
        self.speed += speed

    def speed_down(self, speed):
        self.speed = self.speed - speed
        if self.speed <= 0:
            self.stop()

    def get_status(self):
        return f"Bike is {self.current_state}, speed = {self.speed} Kmph"


b1 = Bike()
print(b1.get_status())
b1.speed_up(30)
print(b1.get_status())
b1.speed_down(50)
print(b1.get_status())


#######
class SportsBike(Bike):
    def get_status(self):
        return f"Sports Bike is {self.current_state}, speed:{self.speed}"

    def park(self):
        self.stop()


s1 = SportsBike()
print(s1.get_status())
s1.speed_up(100)
print(s1.get_status())
s1.park()
print(s1.get_status())


class Hayabusa():
    name = 'Hayabusa'
    launch_year = 2023

    @classmethod
    def get_details(cls):
        return f"{cls.name}, {cls.launch_year}"

    def __init__(self):
        self.status, self.speed = 'Stop', 0

    def speed_up(self, speed):
        if self.status == 'Stop':
            self.status = 'Running'
        self.speed += speed

    def get_status(self):
        return f"{self.status}, speed: {self.speed}"


h1 = Hayabusa()
h2 = Hayabusa()

print(h1.get_status())
print(h2.get_status())

h1.speed_up(100)
print(h1.get_status())
print(h2.get_status())

print(h1.get_details())
print(h2.get_details())
