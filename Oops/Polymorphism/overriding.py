class overriding:
    def displayinfo(self):
        print("welcome!")
class overriding2(overriding):
    def displayinfo(self):
        print("welcome! to overriding")
        super().displayinfo()
object=overriding2()
object.displayinfo()

