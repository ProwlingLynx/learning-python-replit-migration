print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
path = input("Before you is a fork in the road, do you choose to go left or right? ").lower()
if path == "left":
  action = input("There is a bridge to cross the river ahead. The slightest breeze seems to make the roof shake. Do you wait or swim?").lower()
  if action == "wait":
    door = input("After many close encounters you arrive at the final chamber. Choose riches or death says the sign. There are three doors: Red, Blue, or Yellow. Choose ").lower()
    if door == "red":
      print("You chose the red door. You cautiously enter. Checking every corner when you found the largest ruby you had ever seen on the floor! As you inspected the gem, the door shuts you in as gouts of angry fire come to life. Game over!")
    elif door == "blue":
      print("You chose the blue door. try as you might, the hinges squeal in protest to your efforts when a final mighty heave shoved your past the door way and into the waiting maw of a great beast. Game Over!")
    else:
      print('''
      You chose the yellow door in the end. Sometimes the greatest treasure is the most unexpected. You have found your treasure. A treasure most valuable and most secret. You Win!
      ''')
  else:
    print("You decide not to take any chances. Going to get wet anyways you tell yourself as you wade into the chilly waters. A school of trout suddenly appear and push you down stream. Game over!")
else:
  print("The path is dark, but the hole you fell in is darkest. Game Over")