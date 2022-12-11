# A program that tickets a ride at a fan fare

print("Welcome To Ticket FunFare")
height = int(input("What is your height in CM? "))
bill = 0

if height >=120:
    print("Congrats you can ride with us")
    age = int(input("How old are you? "))
    if age < 12:
       bill = 5
    elif age <=18:
         bill = 7
    else:
        bill = 15
    camera = input("Would you want a picture? Y or N ")
    if camera.lower() == "y":
       bill +=3
    print(f"Your total bill is ${bill}")
else:
 print("Kindly try other rides")

		
