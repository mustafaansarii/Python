class Employee:
    company="Google"
    salary=100

name1=Employee()
name2=Employee()
name1.salary=200
print(name2.salary)
print(name1.salary)
