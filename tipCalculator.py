bill = float(input("Welcome to the tip calculator\nPlease enter total bill amount?\n"))
members = float(input("How many people to split your bill?\n"))
tip = float(input("What percentage tip you would like to give?\n"))

# calculating the tip amount
money = int(bill*(1+(tip/100)))/members
money2 = round(money,2)
print("Each person should pay: ",money2)