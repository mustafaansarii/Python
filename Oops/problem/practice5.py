class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getstatus(self):
        print(f"the train name {self.name}")
        print(f"the seats availble {self.seats}")
    def traininfo(self):
        print(f"the fare is {self.fare}")
    def bookticket(self):
        if (self.seats>0):
            print(f"your ticket is booked! {self.seats}")
            self.seats=self.seats-1
        else:
            print("sorry, seat is unvailble! kindly try in tatkal")
    def cancelticket(self,seats):
        pass




trainobje=Train("intracity exp",580,2)
trainobje.getstatus()
trainobje.traininfo()
trainobje.bookticket()

trainobje.getstatus()
#
trainobje.bookticket()
trainobje.getstatus()
#
trainobje.bookticket()