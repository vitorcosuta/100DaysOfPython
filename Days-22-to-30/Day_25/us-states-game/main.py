import turtle
from game_manager import GameManager
from tkinter import messagebox

screen = turtle.Screen()
screen.title('U.S. States Game')

# Load in an image as a new shape
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

game_is_on = True
game_manager = GameManager()


while game_is_on:

    if not game_manager.there_are_correct_guesses():
        answer_state = screen.textinput(title='Guess the State!', prompt="What's another state game?").lower()
    else:
        answer_state = screen.textinput(title='Guess the State!', prompt=f"{game_manager.count_correct_guesses()}/50"
                                                                         f" States Correct").lower()

    if answer_state == 'exit':
        break
    elif game_manager.has_already_been_guessed(answer_state):
        messagebox.showinfo(title='WARNING', message=f"You've already guessed {answer_state.title()} state!")
    else:
        game_manager.check_answer(answer_state)

    if game_manager.count_correct_guesses() == 50:
        game_is_on = False

# Generating states_to_learn.csv file containing a list with missed states
game_manager.generate_to_learn_file()

turtle.mainloop()
