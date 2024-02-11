class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Creating an instance of the Rectangle class
rectangle1 = Rectangle(5, 4)

# Calling methods on the instance
print("Area:", rectangle1.area())  # Output: Area: 20
print("Perimeter:", rectangle1.perimeter())  # Output: Perimeter: 18
