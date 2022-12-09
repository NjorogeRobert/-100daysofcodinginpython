#a program tha calculates the tip and the amount to pay for each member

print("Welcome to the tip calculator")

bill = float(input("What was the total bill? Ksh"))
percentage_given = float(input("What percentage tip would you like to give? 10, 12, or 15 "))

people_to_split = int(input("How many people to split the bill? "))

tip_percentage = (percentage_given / 100)
total_tip = (bill * tip_percentage)
total_bill = (bill + total_tip)
each_bill = (total_bill / people_to_split)
complete_bill = round(each_bill, 2)

print(f"Each person should pay Ksh{complete_bill}")
