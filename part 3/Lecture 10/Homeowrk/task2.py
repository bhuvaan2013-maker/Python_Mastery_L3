class NoFreindsError(Exception):
    pass
def pizza_party(slices,friends):
    if friends==0:
        raise NoFreindsError("Nobody to share with")
    elif not(isinstance(slices,int) and isinstance(friends,int)):
        raise ValueError("Please enter whole numbers")
    else:
        print(f"Each friend gets {friends//slices} slices")
try:
    friends=int(input())
    slices=int(input())
    pizza_party(slices,friends)
except Exception as e:
    print(e)
    