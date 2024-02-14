class Employee:
    company="Google"

    def showdetail(self):
        print("this is an employee")
class programmer(Employee):

    name="mustafa"
    company="Youtube"
    def getname(self):
        print(f"in {self.company} company work {self.name}")

object=programmer()
object.getname()
object.showdetail()
