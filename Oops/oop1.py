#Class Atributes

class Employee:
    company="Google"

name1=Employee()
name2=Employee()
print(name1.company)
print(name2.company)
Employee.company="Youtube"
print(name1.company)
print(name2.company)
Employee.company="Youtube"

print(name1.company)
print(name2.company)