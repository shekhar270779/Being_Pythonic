# Class

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height > 0:
            self._height = height
        else:
            raise ValueError

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def __str__(self):
        return f"Rectangle : width =  {self._width}, height = {self._height}"

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self._width, self._height) == (other._width, other._height)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(5, 10)
print(str(r1))
print(f"Area of rectangle: {r1.area()}")
print(f"Perimeter of rectangle: {r1.perimeter()}")
print(r1)

r2 = Rectangle(5, 10)
if r1 == r2:
    print("r1 and r2 are equal")
else:
    print("r1 and r2 are not equal")

r3 = Rectangle(4, 4)
r4 = Rectangle(10,  10)

if r1 < r3:
    print(f"{r1} is less than {r3}")
else:
    print(f"{r1} is not less than {r3}")

if r4 > r2:
    print(f"{r4} is greater than {r2}")
else:
    print(f"{r4} is not greater than {r2}")

print(f"width of r1 is {r1.width}")
print(f"height of r1 is {r1.height}")

r1.width = 15
r1.height = 25
print(f"{r1}")

try:
    r1.width = -10
except ValueError:
    print("Incorrect value")

try:
    r5 = Rectangle(-10, -10)
    print(f"r5 is {r5}")
except ValueError:
    print("Value error in instantiating rectangle object")