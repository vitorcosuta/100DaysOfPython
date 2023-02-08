from os import system, name
import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#declaring functions
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def print_game_logo():
    print('''88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,   8b,dPPYba, 
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  88P'   `"8a 
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  88       88
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  88       88
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  88       88
                                    aa,    ,88                                
                                     "Y8bbdP"                                 
''')

def print_stickman(number_of_lives):
    match number_of_lives:
        case 6:
            print(HANGMANPICS[0])
        case 5:
            print(HANGMANPICS[1])
        case 4:
            print(HANGMANPICS[2])
        case 3:
            print(HANGMANPICS[3])
        case 2:
            print(HANGMANPICS[4])
        case 1:
            print(HANGMANPICS[5])
        case 0:
            print(HANGMANPICS[6])

def print_word_to_guess(word_to_guess):
    word = ""
    for element in word_to_guess:
        word += element
    print(f"{word}")

def check_win(word_to_guess):
    for element in word_to_guess:
        if element == "_":
            return False
    return True
    
def letter_is_right(letter, word):
    for word_letter in word:
        if word_letter == letter:
            return True
    return False

def is_a_letter(text):
    if text.isalpha():
        return True
    return False
    

#inicializing variables

game_ended = False
number_of_lives = 6
words = ['apple', 'pear']
word = list(random.choice(words))
word_to_guess = list(word)

for i in range(len(word_to_guess)):
    word_to_guess[i] = "_"

print_game_logo()

while not game_ended:
    if number_of_lives > 0:
        if check_win(word_to_guess) == False:

            guess = str(input("Guess a letter: ").lower())
            clear()
            
            while not is_a_letter(guess):
                print("\nThe text you've inserted is not a letter.")
                guess = str(input("Guess a letter: ").lower())
                
            if not letter_is_right(guess, word):
                print(f"\nYou guessed {guess}, that's not in the word. You lose a life.\n")
                number_of_lives -= 1
            else:
                for i in range(len(word)):
                    if word[i] == guess:
                        word_to_guess[i] = guess
    
            print_word_to_guess(word_to_guess)
            print_stickman(number_of_lives)
            
        else:
            clear()
            print_word_to_guess(word_to_guess)
            print("\nYou won!\n")
            print_stickman(number_of_lives)
            game_ended = True
    else:
        clear()
        print_word_to_guess(word_to_guess)
        print("\nYou've run out of lives. You lose.\n")
        print_stickman(number_of_lives)
        game_ended = True