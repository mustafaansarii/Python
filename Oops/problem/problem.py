class programmer:
    company="Google"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getinfo(self):
        print(f"the progremer is {self.name} and working on {self.product}")

object=programmer("mustafa","skype")
object.getinfo()
object=programmer("ram","office")
object.getinfo()