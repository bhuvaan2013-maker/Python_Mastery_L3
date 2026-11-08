class BankAccount: 
    def __init__(self,holder,number,balance):
        self.account_holder=holder
        self.account_number=number
        self.balance=balance
    def set_account_holder(self,name):
        if name=="":
            print("Invalid name")
        else:
            self.account_holder=name
    def set_account_number(self,number:str):
        if len(number)==6 and number[:3]=="ACC":
            self.account_number=number
        else:
            print("Invalid account number")
    def set_balance(self,amount):
        if amount<1:
            print("Invalid balance")
        else:
            self.balance=amount
    def get_account_holder(self):
        return self.account_holder
    def get_account_number(self):
        return self.account_number
    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        if amount<1:
            print("Invalid amount")
        else:
            self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount>self.balance or amount<1:
            print("invalid amount")
        else:
            self.balance=self.balance-amount
    def display_account_details(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Account number: {self.account_number}")
        print(f"Balance: {self.balance}")
account = BankAccount("Rahul", "ACC101", 5000)
print(account.get_account_holder())# Rahul
print(account.get_balance())# 5000
account.deposit(2000)
print(account.get_balance())# 7000
account.withdraw(1500)
print(account.get_balance())# 5500
account.set_account_number("ACC676")
account.display_account_details()