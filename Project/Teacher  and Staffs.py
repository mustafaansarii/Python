class Sttaf:
    def getstaffdetail(self,name,code):
        self.name=name
        self.code=code
    def displaystaff(self):
        print(f'staff name: {self.name}')
        print(f"code: {self.code}")
class Teacher(Sttaf):
    def getTeacher(self,subject,pup):
        self.subject=subject
        self.pup=pup
    def displayTeacher(self):
        print(self.subject)
        print(self.pup)
class Typist(Sttaf):
    def getTypist(self,speed):
        self.speed=speed
    def displayspeed(self):
        print(self.speed)
class Officer(Sttaf):
    def getofficer(self,grade):
        self.grade=grade
    def displayofficer(self):
        print(self.grade)
class Reguler(Sttaf):
    def getReguler(self,Salary):
        self.Salary=Salary
    def displayReguler(self):
        print(self.Salary)
class Casual(Typist):
    def getCasual(self,Wages):
        self.Wages=Wages
    def displayCasual(self):
        print(f"Wages of Casual Typist{self.Wages}")

ch=0
while ch!=5:
    print("""1. Teacher\n2.Officer\n3.Regular Typist\n4. Casual Typist\n5.Exit
    """)
    ch=int(input("Enter your choice: "))
    if ch==1:
        obj=Teacher()
        c=input("Enter the code: ")
        n=input("Enter Your Name: ")
        s=input("Enter Subject")
        p=input("Enter Publication:")
        obj.getstaffdetail(c,n)
        obj.getTeacher(s,p)
        obj.displaystaff()
        obj.displayTeacher()
    elif ch==2:
        c = input("Enter the code: ")
        n = input("Enter Your Name: ")
        g=input("Enter your grade: ")
    elif ch==3:
        object=Reguler()
        c = input("Enter the code: ")
        n = input("Enter Your Name: ")
        sal=input("Enter Salary: ")
        sp=input("Enter speed: ")
        object.getCasual(n)
        object.getReguler(sal)
        object.displaystaff()
        object.displayRegule
        object.displayCasual()
    elif ch==4:
        obj=Casual()
        c = input("Enter the code: ")
        n = input("Enter Your Name: ")
        w = input("Enter daily wages: ")
        sp = input("Enter speed: ")
        obj.getstaffdetail(c,n)
        obj.getCasual(sp)
        obj.getCasual(w)
        obj.displaystaff()
        obj.displayCasual()
        object.displayCasual()
    else:
        print("You Have choosen wrong Value! Progran Terminated")
        break

