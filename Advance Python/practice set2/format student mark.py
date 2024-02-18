name=input("Enter your name: ")
marks=input("Enter your marks: ")
phone=input("Enter your phone number: ")

template="The Name of Student is {} and marks is {} and phone number is {}".format(name,marks,phone)
print(template)
template="The Name of Student is {1} and marks is {2} and phone number is {0}".format(phone,name,marks)
print(template)