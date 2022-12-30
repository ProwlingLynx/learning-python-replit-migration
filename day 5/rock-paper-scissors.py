import random
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
choices = [rock, paper, scissors]
user = int(input("Welcome to RPS! Choose 0 - rock, 1 - paper, 2 - scissors. Good luck!\n"))
computer = random.randint(0, 2)
outcome = "Tie!"
if (user == 0 and computer == 2):
  outcome = "You win!"
elif (user == 1 and computer == 0):
  outcome = "You win!"
elif (user == 2 and computer == 1):
  outcome = "You win!"
elif (not user == computer):
  outcome = "Computer win!"
if user < 3 and user >= 0:
  print(f"Computer chose\n{choices[computer]}")
  print(f"You chose\n{choices[user]}")
  print(outcome)
else:
  print("Invalid input! Please choose 0, 1, or 2.")