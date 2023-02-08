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

print("What do you choose? Type \"0\" for Rock, \"1\" for Paper and \"2\" for Scissors: \n")
player_choice = int(input())

computer_choice = random.randint(0, 2)
game_drawings = [rock, paper, scissors]

if player_choice >= 0 and player_choice <= 2:

  # Drawing the player's choice
  print(game_drawings[player_choice])

  # Drawing the computer's choice
  
  print("\nComputer chose:\n")

  if computer_choice == 0:
    print(rock)
    
  elif computer_choice == 1:
    print(paper)
    
  elif computer_choice == 2:
    print(scissors)

  # Deciding the match

  print("\n")
  
  if player_choice == 0:
    if computer_choice == 0:
      print("It's a draw.")
    elif computer_choice == 1:
      print("You lose.")
    else:
      print("You win.")
      
  elif player_choice == 1:
    if computer_choice == 0:
      print("You win.")
    elif computer_choice == 1:
      print("It's a draw.")
    else:
      print("You lose.")
      
  elif player_choice == 2:
    if computer_choice == 0:
      print("You lose.")
    elif computer_choice == 1:
      print("You win.")
    else:
      print("It's a draw.")
  
else:
  print("You typed an invalid value. You lose!")