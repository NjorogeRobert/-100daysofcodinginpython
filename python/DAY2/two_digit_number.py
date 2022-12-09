#the program should print the sum of the two digit number

#input the two digit number
two_digit_number = input("Type a two digit number: ")
#find the data type of the input
type(two_digit_number)
#change the type of data type from string to int
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

#sum the two numbers
print("The sum is: ", num1 + num2)
