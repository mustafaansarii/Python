class calculator:
    calculator="this is a simple calculator"
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def sum(self):
        print(f"the sum of two number is {self.num2+self.num1}")
    def sbs(self):
        print(f"The substraction of two number is {self.num1-self.num2}")
    def sqr(self):
        print(f"square root is {self.num1**2}")
    def qube(self):
        print(f"qube {self.num1**3}")
number1=int(input("Enter the number: "))
number2=int(input("Enter the number: "))
object=calculator(number1,number2)
object.sbs()
object.sqr()
object.sum()
object.qube()
