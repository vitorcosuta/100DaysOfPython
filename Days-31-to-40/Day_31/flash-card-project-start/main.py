from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
TARGET_LANGUAGE = 'French'
BASE_LANGUAGE = 'English'
timer = None
current_card = {}


def next_card():

    if len(data_dict) == 0:
        inform_end_of_deck()
        return

    global timer, current_card

    # We need to reset the timer in case the user triggers the next_card() function multiple times by repeatedly
    # pressing the buttons.
    if timer is not None:
        window.after_cancel(timer)

    current_card = choice(data_dict)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(lang_title, text=TARGET_LANGUAGE, fill='black')
    canvas.itemconfig(word_display, text=current_card[TARGET_LANGUAGE], fill='black')
    timer = window.after(3000, show_back_card, current_card)


def show_back_card(card):

    if len(data_dict) == 0:
        inform_end_of_deck()
        return

    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(lang_title, text=BASE_LANGUAGE, fill='white')
    canvas.itemconfig(word_display, text=card[BASE_LANGUAGE], fill='white')


def learn_card():
    """Removes a card that the user have already learnt."""
    data_dict.remove(current_card)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


def inform_end_of_deck():
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(lang_title, text='You successfully finished this deck.', fill='black')
    canvas.itemconfig(word_display, text='Congrats!', fill='black')


# Configuring the screen
window = Tk()
window.title('Flashcards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(900, 760)

# Card front setup
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
lang_title = canvas.create_text(400, 150, font=('Ariel', 40, 'italic'))
word_display = canvas.create_text(400, 263, font=('Ariel', 60, 'bold'))

# Buttons setup
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=learn_card)
right_button.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

try:
    DATA = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    DATA = pandas.read_csv('data/french_words.csv')
    data_dict = DATA.to_dict(orient='records')
else:
    data_dict = DATA.to_dict(orient='records')

next_card()

window.mainloop()
