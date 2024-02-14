class Ws:
    def display(self):
        print("this is a programe")
class overws(Ws):
    def display(self):
        super().display()  #super will inherit super class method
        print("this is a amazing! program")
obj=overws()
obj.display()
