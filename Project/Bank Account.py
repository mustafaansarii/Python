class Bankdetail:
    print("My Bank details")
    def Accountdetail(self,Bank_name,Acount_Holder_name,Account_no,balance,account_type):
        self.Bank_name = Bank_name
        self.Acount_Holder_name=Acount_Holder_name
        self.Account_no=Account_no
        self.balance=balance
        self.account_type=account_type
        print(f"Acount_Holder_name: {self.Acount_Holder_name}\nAccount_no: {self.Account_no}\nTotal Balance: {self.balance}\naccount_type: {self.account_type}\nBank_name: {Bank_name}")
    def Deposite(self,Deposite_balance,Depositer_name):
        self.Deposite_balance=Deposite_balance
        self.Depositer_name=Depositer_name
        if self.Deposite_balance>0:
            print(f"The Balance {self.Deposite_balance} Has been deposited to your account A/C no: {self.Account_no} Toatal Available balce is {self.Deposite_balance+self.balance}")
            return self.Deposite_balance+self.balance
        else:
            print("Deposite More money")

obj=Bankdetail()
obj.Accountdetail("Bank of india","Mustafa",123456,5000.00,"saving")
obj.Deposite(1000,"Mustafa")
obj.Deposite(2000,"Mustafa")