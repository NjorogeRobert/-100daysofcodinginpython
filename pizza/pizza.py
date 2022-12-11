#A program that build an automatic order program
print("WELCOME TO AUTOMATIC PIZZA ORDER PROGRAM")
bill = 0
pizza = input("What size of pizza do you prefer? S, M, L ")
if pizza.lower() == "s":
   bill = 15
elif pizza.lower() == "m":
   bill = 20
elif pizza.lower() == "l":
    bill = 25
else:
    print("Enter a valid answer")
    exit()
pepperoni = input("Do you want with Pepperoni Y or N ")
if pepperoni.lower() == "y":
   if pizza.lower() == "s":
      bill += 2
   elif pizza.lower() == "m":
       bill += 3
   elif pizza.lower() == "l":
        bill += 5
cheese = input("Do you want Extra Cheese Y or N ")
if cheese.lower() == "y":
   bill +=3
print(f"Your total bill is ${bill}")
