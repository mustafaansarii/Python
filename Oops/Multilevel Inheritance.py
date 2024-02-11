class A: #Superclass/Base class
    def sum(self):
        a=45
        b=40
        print(a+b)

class B(A):  #Subclass/Derived class
    def displayB(self):
        print("welcom here")

class C(B):
    def displayc(self):
        print("this is thirt class")

obj=C()
obj.sum()
obj.displayB()
obj.displayc()