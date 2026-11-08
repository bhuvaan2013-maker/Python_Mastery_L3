import requests
import csv
URL = "https://bank-backend-eywt.onrender.com"
def create_account():
    name = input("Enter your name:")
    payload = {
        "name": name
    }
    response = requests.post(f"{URL}/create-account",json=payload)
    fah=(response.json()) 
    print("This is your id:",fah['id'])  
def deposit():
    ID=int(input("Enter your account ID:"))
    deposit=int(input("Enter the amount you wish to add:"))
    deposition={"account_id":ID,
                "amount":deposit
    }
    response=requests.post(f"{URL}/deposit",json=deposition)
    answer=(response.json())
    print(answer)
    print("Successfully deposited")
    print("Amount credited is:",deposit)
    with open("deposit.csv","a") as req:
        writer=csv.writer(req)
        writer.writerow([answer["id"],deposit])
    reciept=f"""
                PyBank Receipt
            =======================
            ID number:{answer["id"]}
            Balance:{answer["balance"]}
            Amount deposited:{deposit}"""
    with open("deposit.txt","w") as response:
        response.write(reciept)
def withdraw():
    ID=int(input("Enter your account ID:"))
    withdraw=int(input("Enter the amount you wish to withdraw:"))
    withdrawnation={"account_id":ID,
                "amount":withdraw
    }
    response=requests.post(f"{URL}/withdraw",json=withdrawnation)
    answers=(response.json())
    print("Successfully withdrawn")
    print("Amount removed is:",withdraw)
    with open("withdraw.csv","a") as req:
        writer=csv.writer(req)
        writer.writerow([answers["id"],withdraw])
    reciept=f"""
                PyBank Receipt
            =======================
            ID number:{answers["id"]}
            Balance:{answers["balance"]}
            Amount withdrawn:{withdraw}"""
    with open("withdraw.txt","w") as response:
        response.write(reciept)
    
def transfer():
    ID_from=int(input("Enter your account ID:"))
    ID_to=int(input("Enter the reciever's account ID:"))
    transfer=int(input("Enter the amount you wish to transfer:"))
    transferring={"from_account":ID_from,
                "to_account":ID_to,
                "amount":transfer
    }
    response=requests.post(f"{URL}/transfer",json=transferring)
    answering=(response.json())
    print(answering)
    print("Successfully transferred")
    print("Amount transferred is:",transfer)
    with open("transfer.csv","a") as req:
        writer=csv.writer(req)
        writer.writerow([answering["from_account_id"],answering["to_account_id"],transfer])
    reciept=f"""
                PyBank Receipt
            =======================
            Your ID:{answering["from_account_id"]}
            Thier ID:{answering["to_account_id"]}
            Balance:{answering["balance"]}
            Amount transferred:{transfer}"""
    with open("withdraw.txt","w") as response:
        response.write(reciept)
    
def getloan():
    ID=int(input("Enter your account ID:"))
    loan=int(input("Enter the amount you wish to borrow:"))
    loanation={"account_id":ID,
                "amount":loan
    }
    response=requests.post(f"{URL}/loan",json=loanation)
    lanswer=response.json()
    print("Successfully borrowed")
    print("Amount borrowed is:",loan)
    with open("loan.csv","a") as req:
        writer=csv.writer(req)
        writer.writerow([lanswer["id"],loan])
    reciept=f"""
                PyBank Receipt
            =======================
            ID number:{lanswer["id"]}
            Balance:{lanswer["balance"]}
            Amount loaned:{loan}"""
    with open("loan.txt","w") as response:
        response.write(reciept)
def check_balance():
    ID=int(input("Enter your account ID:"))
    response=requests.get(f"{URL}/balance/{ID}")
    fah=response.json()
    print(f"Balance={fah["balance"]}")
print("Welcome to the bank API application")
while True:
    print("*"*50)
    print("You have 7 options:")
    print("1) Create an account")
    print("2) Deposit money in your account")
    print("3) Withdraw money from your account")
    print("4) Transfer money to another account")
    print("5) Apply for a loan")
    print("6) Check your account balance")
    print("7) Quit the program")
    print("*"*50)
    lumity=int(input("Enter the number of the choice you wish to execute:"))
    match lumity:
        case 1:
            create_account()
        case 2:
            deposit()
        case 3:
            withdraw()
        case 4:
            transfer()
        case 5:
            getloan()
        case 6:
            check_balance()
        case 7:
            print("Thank you for using the bank API")
            break
        case _:
            print("Invalid input")