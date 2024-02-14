class Employee:
    salary = 1000
    increament = 1.5

    @property
    def salaryafterincreament(self):
        return self.salary * self.increament

    @salaryafterincreament.setter
    def salaryafterincreament(self, sai):
        self.increament = sai / self.salary

e = Employee()
print(e.salaryafterincreament)
print(e.increament)
e.salaryafterincreament=2000
print(e.salaryafterincreament)
print(e.increament)
