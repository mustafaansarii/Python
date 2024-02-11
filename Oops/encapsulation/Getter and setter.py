class student():
    def __init__(self):
        self.name = ""

    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name

obj = student()
obj.setname("Mustafa")
name = obj.getname()
print(name)
