#A program that checks if the number keyed in is either Odd or Even

#input the number
number =int(input("Enter the number to check: "))

#Use conditional statement to check if it is even or odd. we use %2 sign to determine if a number is EVEN or ODD

if number % 2 == 0:
   print(f"{number} is an EVEN number")
else:
   print(f"{number} is an ODD number")

