class A:
    def sum(self):
        a=45
        b=40
        print(a+b)

class B(A):
    def displayB(self):
        print("welcom here")


obj=B()
obj.sum()
obj.displayB()