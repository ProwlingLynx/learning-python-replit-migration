#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float( input("What was your total bill? $") )
number_of_people = int(input("How many people are on the bill? "))
tip_amount = float( input("How much tip would you like to leave? 10, 12, or 15? ") )
tip_percent = round( tip_amount/100 + 1, 2 )
total_bill = bill * tip_percent
print( f"Each person must pay ${round(total_bill / number_of_people, 2)}" )