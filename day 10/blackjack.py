from art import logo
def add_nums(a, b):
  return a + b
def sub_nums(a, b):
  return a - b
def mult_nums(a, b):
  return a * b
def div_nums(a, b):
  return a / b
dict = {
  "+" : add_nums,
  "/" : div_nums,
  "x" : mult_nums,
  "-" : sub_nums,
}
running_total = 0
print(logo)
print("Welcome to the calculator!\n")
first_loop = True
more_operations = "y"
use_previous = "n"
while more_operations == "y":
  if not first_loop:
    use_previous = input("Use previous result? (y/n): ")
  if use_previous == "y":
    user_input_a = running_total
  else:
    user_input_a = float(input("Input a number: "))
    first_loop = False
  
  print("What would you like to do with this?")
  for key in dict:
    print(key)
  user_operation = input()
  user_input_b = float(input("Input a second number: "))
  running_total = dict[user_operation](user_input_a, user_input_b)
  print(f"{user_input_a} {user_operation} {user_input_b} = {running_total}")
  more_operations = input("Would you like to do more math? (y/n)\n")

print("Thank you for stopping by!")