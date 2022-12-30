from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")
def get_person_bid():
  person = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  dict[person] = bid
  clear()
def check_bidders():
  clear()
  return input("Are there any other bidders? Type 'yes' or 'no'.\n")
def get_highest_bidder():
  person = ""
  bid = 0
  for bidder in dict:
    value = dict[bidder]
    if value > bid:
      person = bidder
      bid = value
  print(f"{logo}\nAnd the winner is... {person}! with ${bid}!")
dict = {}

more_bidders = 'yes'

while more_bidders == 'yes':
  get_person_bid()
  more_bidders = check_bidders()
print(dict)
clear()
get_highest_bidder()