print("Welcome to The Tip Calculator")

# Using float allows for decimal inputs for the total bill
amount = float(input("What was the total Bill?\n$"))

# Get the tip percentage
tip = int(input("How much Tip would you like to Give? 10, 12, 15\n"))

# Get the number of people
people = int(input("How many people would like to split the bill?\n"))

# 1. Calculate the tip amount: (tip / 100) * amount
# 2. Add it to the original amount to get the total bill
# 3. Divide by the number of people
bill = (amount + (amount * (tip / 100))) / people

# round(bill, 2) limits the final amount to 2 decimal places for currency formatting
print(f"Each person should pay: ${round(bill, 2)}")