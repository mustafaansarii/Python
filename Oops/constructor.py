class Employee:
    company="Google"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print("Employee")
    def getdetail(self):
        print(self.name)
        print(self.salary)
    def getsalary(self):
        print(f"{name1.name} salary {self.salary} in {self.company}")
    @staticmethod #without use self
    def greeet():
        print("hi, Good Morning!")

mustafa=Employee("mustafa",1000)
mustafa.getdetail()