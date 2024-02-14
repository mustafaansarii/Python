class Bankdetail:
    print("My Bank details")
    def Account_details(self,Bank_name,Acount_Holder_name,Account_no,balance,account_type):
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
            self.balance = self.Deposite_balance + self.balance
            print(f"The Balance {self.Deposite_balance} Has been deposited to your account, A/C no: {self.Account_no} Toatal Available balce is {self.balance}")
        else:
            print("Deposite More money")

    def Withdrawal(self,Amount):
        self.Amount=Amount
        self.balance = self.balance - self.Amount
        print(f"The Balance {self.Amount} Has been Debited from your account, A/C no: {self.Account_no} Toatal Available balce is {self.balance}")
obj=Bankdetail()
while True:
    Form=int(input('''
    1 About bank details
    2 Deposite money
    3 Withdraw money
    4 Exit\n choose above option:'''))
    if Form==1:
        obj.Account_details("Bank of india", "Mustafa", 123456, 5000.00, "saving")
    elif Form==2:
        obj.Deposite(500,"Mustafa")
    elif Form==3:
        obj.Withdrawal(500)
    elif Form==4:
        break
    else:
        print("Please choose valid option")
