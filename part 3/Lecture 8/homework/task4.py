class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit_amount(self,amount):
        if amount<0:
            print("Invalid amount")
        else:
            self.balance=self.balance+amount
    def show_balance(self):
        print(f"{self.owner}: Rs.{self.balance}")
class SavingsAccount(Account):
    def __init__(self,owner,balance,rate):
        super().__init__(owner,balance)
        self.rate=rate
    def add_interest(self):
        interest=self.balance*self.rate/100
        self.deposit_amount(interest)
bank=SavingsAccount("Meera",10000,5)
bank.deposit_amount(2000)
bank.add_interest()
bank.show_balance()