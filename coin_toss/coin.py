#program that randomly prints heads or tails
#Use Random module
import random
test_seed = int(input("Enter a number "))
random.seed(test_seed)

check = random.randint(0, 1)

if check == 1:
   print("Heads")
else:
   print("Tails")
