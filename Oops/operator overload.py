class Number:
    def __init__(self, num):
        self.num = num
    def __add__(self, num2):
        print("Let's add")
        return self.num + num2.num
    def __mul__(self, num2):
        print("Let's mul")
        return self.num * num2.num
n1 = Number(1)
n2 = Number(6)
print(n1 + n2)
print(n1*n2)
