from art import logo, vs
from game_data import data
from os import name, system
import random

def check_higher(item_A, item_B):
    if item_A['follower_count'] > item_B['follower_count']:
        return 'a' 
    elif item_A['follower_count'] < item_B['follower_count']:
        return 'b'
    return 'NONE'

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def choose_celebrity():
    return random.choice(data)


def game():
    score = 0
    should_continue = True
    temp = choose_celebrity()
    
    while should_continue:
        print(logo)    
        item_A = temp
        item_B = choose_celebrity()

        #We should guarantee that A is not the same thing as B.
        while item_B['name'] == item_A['name']:
            item_B = choose_celebrity()

        if score > 0:
            print(f"You're right! Your current score is {score}")
        
        print(f"\nCompare A: {item_A['name']}, a {item_A['description']}, from {item_A['country']}")
        # print(f"Followers: {item_A['follower_count']}")
        print(vs)
        print(f"\nAgainst B: {item_B['name']}, a {item_B['description']}, from {item_B['country']}")
        # print(f"Followers: {item_B['follower_count']}")

        answer = input("Who has more followers? Type 'A' or 'B':  ").lower()

        while answer != 'a' and answer != 'b':
            answer = input("Please type a valid answer:  ")

        if answer == check_higher(item_A, item_B):
            score += 1
            temp = item_B
            clear()
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. FINAL SCORE: {score}")
            should_continue = False

    answer = input("Play again? Type 'yes' or 'no':  ").lower()

    while answer != 'yes' and answer != 'no':
        answer = input("Please type a valid answer:  ")

    if answer == 'yes':
        game()
    else:
        print("\nThank you for playing!")
        return

game()