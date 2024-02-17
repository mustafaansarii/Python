try:
    a =int(input("Enter a number: "))
    c=1/a
    print(c)

except ValueError as e:
    print("Exception1 occure")
    print("Please Enter a valid value!")
    print(e)
except ZeroDivisionError as e:
    print("Exception2 occure")
    print("Don't devide by zero!")
except:
    print("Valid input")
print("Thanks for using!")