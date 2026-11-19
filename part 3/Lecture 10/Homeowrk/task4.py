try:
    number=int(input())
except ValueError:
    print("Please enter a whole number")
else:
    print(f"Total: Rs.{number*150}")
finally:
    print(f"Thank you for visiting")