class Person:
    def __init__(self):
        self.salary = 30000
        self.company = "GOOGLE"
        print(self.salary)
        print(self.company)
    def person2(self):
        print("This is a parent class")

class Person2(Person):
    def subclass(self):
        print("This is a sub class")

    def call(self):
        print("This is super")
        super().person2()

class Person3(Person2):
    def subclass2(self):
        print("This is a child class2")

    def __init__(self):
        super().__init__()
        print("This is Employee")

obj = Person3()



