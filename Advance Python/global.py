a= 54 #global variable
def func1():
    global a
    print(a)
    a = 5 # local
    print(a)

func1()
print(a)