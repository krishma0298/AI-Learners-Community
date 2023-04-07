t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    result = ""
    balance = k
    
    for i in range(n):
        if a[i] <= balance:
            result += "1"
            balance -= a[i]
        else:
            result += "0"
    
    print(result)