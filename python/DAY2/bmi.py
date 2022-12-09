#the program should calculate the BMI of a person
#get inputs from the clients

height= input("Enter your height in M: ")
weight = input("Enter your weight in Kg: ")

#CHANGE FROM STR TO FLOAT
num1 = float(height)
num2 = float(weight)

#calculate the bmi
result = (num2 / (num1 ** 2))

#The result should be a whole number so change to int
BMI = int(result)

#print the result
print(f"Your BMI is {BMI}")
