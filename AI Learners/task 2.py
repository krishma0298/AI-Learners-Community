def calculate_min_investment(x, y, t):
    taxable_income = x - y
    if taxable_income <= 0:
        return 0
    else:
        min_investment = taxable_income / (t / 100)
        return min_investment
x = 1000000
y = 500000  
t = 20     
min_investment = calculate_min_investment(x, y, t)
print(f"The minimum amount of money you must invest to avoid paying taxes is {min_investment} rupees.")