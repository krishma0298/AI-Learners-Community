def can_enter_token(x):

    if x == 6:
        return True
    else:
        return False
t = 3  

for i in range(t):
    x = int(input())  
    if can_enter_token(x):
        print("Chef can enter a new token.")
    else:
        print("Chef cannot enter a new token.") 