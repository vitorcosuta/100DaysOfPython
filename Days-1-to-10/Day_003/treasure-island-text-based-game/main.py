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

print("")
option1 = input("Which direction do you want to go? Left (\"L\") or right (\"R\")? ").lower()

if option1 == "l":
  print("")
  print("You choose to go to the left, and you see a lake in front of you. The water looks dim and murky.")
  option = input("What do you do? Swim (\"S\") or wait (\"W\")? ").lower()

  if option == "w":
    print("")
    print("A dazzlingly bright light starts to draw your attention to a forest away from the lake. You follow the light until you reach a small glade.")
    print("There seems to be three doors magically floating right in the middle of it, side by side. All three of them are slightly open and emiting")
    print("light of their respective colors, but you can't see what's inside.")
    option = input("What door do you enter? Red (\"R\"), blue (\"B\") or yellow (\"Y\")? ")

    if option == "y":
      print("")
      print("The yellow light was coming from a huge gilded treasure waiting for you to find it in there, inside the door.")
      print("CONGRATULATIONS! YOU WON.")
    elif option == "r":
      print("")
      print("The red light that was emanating from the red door was coming from a hell fire pit. You end up in flames and burn to death. Ouch!")
      print("GAME OVER")
    elif option == "b":
      print("")
      print("You open the blue door and get inside a huge cave. There are lots of lapis lazuli gems hanging from the ceiling. But wait.")
      print("It isn't lapis lazuli. It is blueberry cannibal bats! You end up getting eaten by then. I wonder if humans like you taste like")
      print("blueberry for them.")
      print("GAME OVER")
    else:
      print("")
      print("You choose to not enter any of the doors in front of you. You wait a minute and they're all gone. You hear a monstruous growl in the")
      print("distance. A ferocious beast is now coming after you. You have nowhere to run.")
      print("GAME OVER")
  else:
    print("")
    print("You were attacked by radioactive trouts while trying to swim to the other side.")
    print("GAME OVER")
else:
  print("")
  print("You fall into a hole.")
  print("GAME OVER")