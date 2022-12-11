print("WELCOME TO LOVE CALCULATOR")
name1 = input("Enter your Name ")
name2 = input("Enter their name ")
#concatenate the names
name = name1 + name2
#change to lower case
name_lower = name.lower()
#look how many letters are similar to love using count() function
L = name_lower.count("l")
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")
love = L + o + v + e
#similarity with true
t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")
true = t + r + u + e

#concatenate the two words
final_name = str(true) + str(love)

#change to int
final_name_int = int(final_name)

if final_name_int < 10 or final_name_int > 90:
    print(f"Your score is {final_name_int} you go together like coke and montos")
elif final_name_int >=40 and final_name_int <= 50:
    print(f"Your score is {final_name_int} you are alright together")
else:
    print(f"Your score is {final_name_int}")

