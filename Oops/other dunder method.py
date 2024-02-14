class Number:
    def __init__(self, num):
        self.num = num
    def __add__(self, num2):
        print("Let's add")
        return self.num + num2.num
    def __mul__(self, num2):
        print("Let's mul")
        return self.num * num2.num
    def __str__(self):
        return f"this is decimal number{self.num}"
    def __len__(self):
        return 1
    
n1 = Number(1)
print(n1)
print(len(n1))