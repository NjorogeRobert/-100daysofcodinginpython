rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("What do you choose?")
choose = int(input("Type 0 for Rock, 1 for paper, 2 for scissors  "))

computer = random.randint(0, 2)


if choose == 0:
  print("You choose ", rock)
  #print(computer)
  if computer == 0:
    print("Computer chose", rock)
    print("You draw")
  elif computer == 1:
    print("Computer chose", paper)
    print("You loose")
  elif computer == 2:
    print("Computer chose", scissors)
    print("You win")
elif choose == 1:
  print("You choose ", paper)
  if computer == 0:
    print("Computer chose", rock)
    print("You Win")
  elif computer == 1:
    print("Computer chose", paper)
    print("You draw")
  elif computer == 2:
    print("Computer chose", scissors)
    print("You loose")
elif choose == 2:
  print("You choose ", scissors)
  if computer == 0:
    print("Computer chose", rock)
    print("You loose")
  elif computer == 1:
    print("Computer chose", paper)
    print("You win")
  elif computer == 2:
    print("Computer chose", scissors)
    print("You draw")