# Different operators can perform different operations depending on the operands' types.
class overloading:
    def displayinfo(self,name=''):
        print("welcome!"+name)
object=overloading()
object.displayinfo()

object.displayinfo("Mustafa")