class A:
    def sum(self):
        a=45
        b=40
        print(a+b)
class B:
    def displayB(self):
        print("welcom here")
class C:
    def displayc(self):
        print("welcom here")

class D(A,B,C):
    def displayd(self):
        print("this is thirt class")
obj=D()
obj.sum()
obj.displayB()
obj.displayc()
obj.displ`ayd()