menu = ["Burger", "Pizza", "Pasta"]
def order(option):
    if option>3 or option<0:
        raise IndexError("Invalid choice")
    elif not (isinstance(option,int)):
        raise ValueError("Invalid choice")
    else:
        print(f"You ordered {menu[option]}")
try:
    option=int(input())
    order(option)
except (IndexError,ValueError) as e:
    print(e)
except Exception as e:
    print(e)
    