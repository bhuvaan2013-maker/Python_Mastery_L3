class WeakPasswordError(Exception):
    pass
def check_password(password):
    if len(password)>7:
        pass
    else:
        raise WeakPasswordError("Weak password: needs at least 8 characters")
try:
    password=input()
    check_password(password)
except WeakPasswordError as e:
    print(e)
else:
    print("Password accepted")