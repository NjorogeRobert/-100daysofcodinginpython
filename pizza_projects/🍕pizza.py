"""PIZZA ORDER"""
print("🍕WELCOME TO PIZZA PARLOUR🍕")
bill = 0
size = int(input("What 🍕 size would you want? 1) small, 2) medium, 3)large "))

if size == 1:
    bill += 15
    #print(f"Your bill is {bill}")
elif size == 2:
    bill += 20
    #print(f"Your bill is {bill}")
elif size == 3:
    bill += 25
    #print(f"Your bill is {bill}")
else:
    raise ValueError("Enter valid Numbers which are 1,2, 3")

pepperoni = input("Would you want pepperoni? 🍕 Y or N  ")
pep = pepperoni.lower()
if pep == 'y':
    if size == 1:
        bill += 2
        #print(f"Your bill is {bill}")
    elif size == 2 or size == 3:
        bill += 3
       # print(f"Your bill is {bill}")
    else:
        raise TypeError("Invalid")
    
cheese = input("Extra cheese?🧀  Y or N: ")
cheese = cheese.lower()
if cheese == 'y':
    bill += 1
    print(f"Your Total bill 💵 is ${bill}")
else:
    print(f"Your Total bill 💵 is ${bill}")
    
    
