class Staff:
    def getStaffDetail(self, name, code):
        self.name = name
        self.code = code

    def displayStaff(self):
        print(f'Staff name: {self.name}')
        print(f"Code: {self.code}")

class Teacher(Staff):
    def getTeacherDetail(self, subject, publication):
        self.subject = subject
        self.publication = publication

    def displayTeacher(self):
        print(f"Subject: {self.subject}")
        print(f"Publication: {self.publication}")

class Typist(Staff):
    def getTypistDetail(self, speed):
        self.speed = speed
    def displaySpeed(self):
        print(f"Speed: {self.speed}")

class Officer(Staff):
    def getOfficer(self, grade):
        self.grade = grade

    def displayOfficer(self):
        print(f"Grade: {self.grade}")


class Regular(Staff):
    def getRegular(self, salary):
        self.salary = salary

    def displayRegular(self):
        print(f"Salary: {self.salary}")


class Casual(Typist):
    def getCasual(self, wages):
        self.wages = wages

    def displayCasual(self):
        print(f"Wages of Casual Typist: {self.wages}")


ch = 0
while ch != 5:
    print("""1. Teacher\n2. Officer\n3. Regular Typist\n4. Casual Typist\n5. Exit\n""")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        obj = Teacher()
        c = input("Enter the code: ")
        n = input("Enter Your Name: ")
        s = input("Enter Subject: ")
        p = input("Enter Publication: ")
        obj.getStaffDetail(n, c)
        obj.getTeacherDetail(s, p)
        obj.displayStaff()
        obj.displayTeacher()
    elif ch == 2:
        c = input("Enter the code: ")
        n = input("Enter Your Name: ")
        g = input("Enter your grade: ")
    elif ch == 3:
        obj = Regular()
        c = input("Enter the code: ")
        n = input("Enter Your Name: ")
        sal = input("Enter Salary: ")
        sp = input("Enter speed: ")
        obj.getStaffDetail(n, c)
        obj.getRegular(sal)
        obj.displayStaff()
        obj.displayRegular()
    elif ch == 4:
        obj = Casual()
        c = input("Enter the code: ")
        n = input("Enter Your Name: ")
        w = input("Enter daily wages: ")
        sp = input("Enter speed: ")
        obj.getStaffDetail(n, c)
        obj.getCasual(w)
        obj.displayStaff()
        obj.displayCasual()
    elif ch == 5:
        print("Exiting...")
    else:
        print("You have chosen the wrong value! Program Terminated")
        break
