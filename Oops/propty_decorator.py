class Employee:
    company="Bharat Gas"
    salary=12000
    salarybonus=4500
    #totalsalary= salary + salarybonus

    @property
    def totalsalary(self):
        return self.salary + self.salarybonus
    
    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus=val- self.salary


object=Employee()
print(object.totalsalary)
object.totalsalary=5600
print(object.salary)
print(object.salarybonus)