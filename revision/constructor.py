class base:
    def __init__(self,h: int):
        print("this is base")
        print(h)

    def add(self,a,b):
        print(a+ b)

class deroved(base):
    def __init__(self,k):
        print("hello",k)
    def multiplie(self,a,c):
        print(a*c)


if __name__ == '__main__':
    deroved("k").add(23,54)
    deroved("k2").multiplie(21,2)