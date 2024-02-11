class Employee:
    company="Google"
    def getsalary(self):
        print(f"{name1.name} salary {self.salary} in {self.company}")
    @staticmethod #without use self
    def greeet():
        print("hi, Good Morning!")
    @staticmethod
    def work():
        print("this is amazing")
    @staticmethod
    def time():
        print("9 AM")

name1=Employee()
name1.salary=10000
name1.name="Mustafa"
name1.getsalary()
name1.greeet()
name1.work()
name1.time()



