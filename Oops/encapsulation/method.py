
class MyClass:
    def __init__(self, x):
        self.__x = x  # Private attribute

    def get_x(self):  # Public method
        return self.__x

    def set_x(self, x):  # Public method
        self.__x = x

obj = MyClass(5)
print(obj._MyClass__x)  # Accessing private attribute (not recommended)
obj._MyClass__x = 10


