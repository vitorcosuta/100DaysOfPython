from art import LOGO
from os import system, name
import random

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def draw_game_logo():
    print(LOGO)

def print_greetings():
    print("\n\n")
    print("Welcome to GUESS THE NUMBER!")
    print("Are you ready to try to guess which number I have in mind?")
    print("I'm thinking of a number between 1 and 100.")
    print("\n")

def pick_difficulty():
    difficulty = input("Choose a difficulty! \"Easy\" or \"Hard\"?  ").lower()

    while difficulty != 'easy' and difficulty != 'hard':
        print("\nPlease select a valid difficulty.")
        difficulty = input("Choose a difficulty! \"Easy\" or \"Hard\"?  ").lower()
        
    return difficulty 
    
def choose_number_to_guess():
    return random.randint(1, 100)

def is_valid_number(input_str):
    if input_str.isdigit():
        number = int(input_str)
        if number >= 1 and number <= 100:
            return True
        return False
    return False
        
def check_number_proximity(guessed_number, actual_number):
    
    if guessed_number < actual_number:
        difference = actual_number - guessed_number
        if difference <= 5:
            print("You are very close to the number I'm thinking!")
        elif difference <= 10:
            print("You are somewhat close to the number I'm thinking. Almost there!")
        else:
            print("You're guessing way too low.")
            
    elif guessed_number > actual_number:
        difference = guessed_number - actual_number
        if difference <= 5:
            print("You are very close to the number I'm thinking!")
        elif difference <= 10:
            print("You are somewhat close to the number I'm thinking. Almost there!")
        else:
            print("You're guessing way too high.")
            
    else: #if actual_number == guessed_number
        print(f"\nYou guessed it! {actual_number} was the number I've had in mind all this time. You nailed it!")

def run_game():
 
    draw_game_logo()
    print_greetings()

    difficulty = pick_difficulty()

    if difficulty == 'easy':
        number_of_attempts = 10
    elif difficulty == 'hard':
        number_of_attempts = 5

    random_number = choose_number_to_guess()
    should_continue = True

    while should_continue:
        guess = input("\nMake a guess: ")

        while not is_valid_number(guess):
            print("\nPlease inform a valid number between 1 and 100.")
            guess = input("\nMake a guess: ")

        guess = int(guess)
        check_number_proximity(guess, random_number)
        
        if random_number != guess:
            number_of_attempts -= 1

        if number_of_attempts > 0 and random_number != guess:
            print(f"You have {number_of_attempts} attempts remaining.")
        
        if number_of_attempts == 0:
            print(f"You've run out of attempts to guess. You lost. The number I was thinking of was {random_number}.")
            should_continue = False

        if random_number == guess:
            should_continue = False

    answer = input("\nDo you want to play again? \"Yes\" or \"No\"?  ").lower()

    while not answer == 'yes' and not answer == 'no':
        print("\nPlease inform a valid answer.")
        answer = input("\nDo you want to play again? \"Yes\" or \"No\"?  ").lower()

    if answer == 'yes':
        clear()
        run_game()
    elif answer == 'no':
        print("\nThank you for playing!")

run_game()