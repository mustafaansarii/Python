class Bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("Total availble Bikes", self.stock)
    def rentforbike(self,quantity):
        self.quantity=quantity
        if quantity<=0:
            print("Enter valid value")
        elif quantity>self.stock:
            print("sorry! Bike is unavailble")

        else:
            print("Total Price",quantity*100)
            self.stock=self.stock-quantity
            print("Total available Bikes ",self.stock)

while True:
    object = Bikeshop(100)
    uc=int(input('''
    1 Display Bike
    2 Rent Bike
    3 Exit\n choose above option:'''))

    if uc==1:
        object.displaybike()
    elif uc==2:
        buy = int(input(f"Enter qty: "))
        object.rentforbike(buy)
    elif uc==3:
        print("Thanks for Visiting")
        break
    else:
        print("Please choose valid option")
