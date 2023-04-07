def can_hear_frequency(x):
    """
    Determines if Binary can hear Chef's commands.
    x: the frequency of Chef's commands in Hz
    returns: "YES" if Binary can hear the commands, "NO" otherwise
    """
    if x >= 67 and x <= 45000:
        return "YES"
    else:
        return "NO"
t = int(input()) 
for i in range(t):
    x = int(input())  
    print(can_hear_frequency(x))
