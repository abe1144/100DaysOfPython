# 1 - Greeting
print("Welcome to the tip Calculator!")

# 2 - Prompt for the bill amount
bill_total = float(input("What was the total bill? $"))

# 3 - Prompt for number of people to split between
split = int(input("How many people to split the bill? "))

# 4 - Prompt for Tip Percentage
tip = int(input("What percentage tip would you like to give? "))

# 5 - Output each individual's share total
your_share = round((float(bill_total) / split) * (1 + float(tip)/100), 2)
print("You should pay: ${}".format(your_share))
