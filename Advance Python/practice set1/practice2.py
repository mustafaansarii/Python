def division(a, b):
    try:
        print(f"the devision of {a} and {b} is: {a / b}")
    except ZeroDivisionError:
        print("Enter valid value")
    except ValueError:
        print("Enter valid value")
    except TypeError:
        print("Enter valid number")
        
a=int(input("eter a:"))
b=int(input("Enter b: "))
division(a,b)