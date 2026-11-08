print("Welcome to file manager")
while True:
    print("You have the following options:")
    print("1.Read a file")
    print("2.Add to a file")
    print("3.Leave")
    choice=int(input("Enter the choice you wish to execute:"))
    if choice==1:
        f_name=input("Enter the file name you wish to open:")
        f_read="r"
        document=open(f_name,f_read)
        content=document.read()
        print(content)
    if choice==2:
        f_name=input("Enter the file name you wish to amend:")
        document=open(f_name,"a")
        addi=input("Enter the information you wish to enter:")
        document.writelines()
        document.writelines(addi)
    if choice==3:
        print("Thank you for using our services-bye")
        break