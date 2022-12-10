''' A program that interprets the Body Mass Index(BMI) based on the User's weight and height.
instructions
..............
1) Under 18.5 they are under weight
2)Over 18.5 but below 25 they have a normal weight
3) Over 25 but below 30 they are overweight
4)Over 30 but below 35 they are obese
5)Above 35 they are clinically obese

BMI = weight/ height * height
'''

height = float(input("Enter your height in M: "))
weight = float(input("Enter your Weight in Kg: "))

#compute the bni
result = (weight/(height ** 2))
#round the answer to two decimal places
BMI = round(result, 2)

if BMI < 18.5:
   print(f"Your BMI is {BMI}, you are underweight.")
elif BMI >= 18.5 and BMI < 25.0:
     print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25.0 and BMI < 30.0:
     print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >= 30.0 and BMI < 35.0:
     print(f"Your BMI is {BMI}, you are obese.")
else:
     print(f"Your BMI is {BMI}, you are clinically obese.")
