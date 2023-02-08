############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

from art import logo
import random
from os import name, system

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def is_valid_answer(answer):
    if answer == 'yes' or answer == 'no':
        return True
    return False

def pick_random_card():
    return random.choice(cards)

def calculate_hand_total(hand):
    """Returns the total value of a given hand of cards in a Blackjack game."""
    total = 0
    
    for card in hand:
        total += int(card)

    return total

def decide_winner(player_score, computer_score):
    """Decides the winner of the round in a Blackjack game."""
    if player_score == computer_score:
        print("\nDraw.\n")
    elif sum(player_hand) == 21 and len(player_hand) == 2:
        print("\nYou've got a blackjack! You won!\n")
    elif sum(computer_hand) == 21 and len(computer_hand) == 2:
        print("\nComputer's got a blackjack! It means you lost.\n")
    elif player_score > 21: 
        print("\nIt's a bust! You lost.\n")
    elif computer_score > 21:
        print("\nA bust on computer's side. You won!\n")
    elif player_score > computer_score:
        print("\nYou were the one who reached the closest to 21. You won!\n")
    elif player_score < computer_score:
        print("\nThe computer was the one who reached the closest to 21. You lost.\n")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
computer_hand = []

def blackjack():

    print(logo + "\n\n")

    for i in range(2):
        player_hand.append(pick_random_card())
        computer_hand.append(pick_random_card())

    player_score = calculate_hand_total(player_hand)
    computer_score = calculate_hand_total(computer_hand)

    # If player's score is equal to 21 in the first draw, then the player won't be able to choose to pick another card
    # That said, we ignore the while loop if their score is already 21 in the first turn
    wants_to_draw_card = True
    
    while player_score < 21 and wants_to_draw_card:
        
        print(f"Your cards are {player_hand}, and your current score is {player_score}.")
        print(f"Computer's first card is [{computer_hand[0]}]")

        answer = input("Do you wish to draw one more card? \"Yes\" or \"No\"?  ")
        while not is_valid_answer(answer):
            print("\nYou did not informed a valid answer.")
            answer = input("Do you wish to draw one more card? \"Yes\" or \"No\"?  ")

        if answer == 'yes':
            random_card = pick_random_card()

            # Ace card becomes 1 automatically if player score plus 11 exceeds 21
            if random_card == 11 and player_score + random_card > 21:
                random_card = 1
                player_hand.append(random_card)
            else:
                player_hand.append(random_card)
            
        elif answer == 'no':
            wants_to_draw_card = False

        player_score = calculate_hand_total(player_hand)
    
        
    # Now's the dealer's (computer's) turn! The rule also states that if the dealer ends up with a hand worth less than 17, they must
    # draw another card.
    while computer_score < 17:
        random_card = pick_random_card()
    
        # Ace card becomes 1 automatically if computer score plus 11 exceeds 21
        if random_card == 11 and computer_score + random_card > 21:
            random_card = 1
            computer_hand.append(random_card)
        else:
            computer_hand.append(random_card)

        computer_score = calculate_hand_total(computer_hand)

    print(f"\nYour cards are {player_hand}, and your final score is {player_score}.")
    print(f"Computer's cards are {computer_hand}, and its final score is {computer_score}.")
    decide_winner(player_score, computer_score)

    answer = input("\nLet's play another game of Blackjack? \"Yes\" or \"No\"?  ").lower()

    while not is_valid_answer(answer):
        print("\nYou did not informed a valid answer.")
        answer = input("Let's play a game of Blackjack? \"Yes\" or \"No\"?  ")

    if answer == 'yes':
        player_hand.clear()
        computer_hand.clear()
        clear()
        blackjack()
    else:
        print("\nThank you for playing!")
    
answer = input("Let's play a game of Blackjack? \"Yes\" or \"No\"?  ").lower()

while not is_valid_answer(answer):
    print("\nYou did not informed a valid answer.")
    answer = input("Let's play a game of Blackjack? \"Yes\" or \"No\"?  ")

if answer == 'yes':
    blackjack()
else:
    print("\nWell, maybe another time then!")