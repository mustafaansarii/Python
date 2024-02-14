class Employee:
    company="Link glycer"
    salary=100

    def changesalary(self, sal):
        self.__class__.salary = sal  #dunder (__)

    @classmethod #decorator to change function
    def changecompany(cls, com):
        cls.company=com

obj=Employee()
print(obj.salary)
print(obj.company)
obj.changesalary(3443)
print(obj.salary)
print(Employee.salary)
obj.changecompany("Youtube")
print(Employee.company)