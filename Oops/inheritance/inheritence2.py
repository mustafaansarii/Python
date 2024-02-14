class A:
    def __init__(self):
        print("This is parents inheritence")

class B:
    def b(self):
        print("this child inherited")

class C(A,B):
    def c(self):
        print("this is child2 inheritence")
obj=C()
obj.b()
obj.c()