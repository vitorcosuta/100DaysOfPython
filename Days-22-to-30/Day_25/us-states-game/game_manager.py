from turtle import Turtle
import pandas

FONT = ('Courier', 10, 'bold')
FONT_ALIGNMENT = 'center'
PATH = '50_states.csv'


def find_state_coordinate(state_name):
    data = pandas.read_csv(PATH)
    state_data = data[data.state == state_name]
    coordinate = (int(state_data.x), int(state_data.y))
    return coordinate


class GameManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_states = pandas.read_csv(PATH).state.to_list()
        self.correct_guesses = []
        self.penup()
        self.pencolor('black')
        self.hideturtle()

    def check_answer(self, answer):

        answer = answer.title()
        if answer in self.all_states:
            self.correct_guesses.append(answer)
            self.print_state_name(answer)
            return True

        return False

    def has_already_been_guessed(self, answer):

        answer = answer.title()
        for guess in self.correct_guesses:
            if answer == guess:
                return True
        return False

    def there_are_correct_guesses(self):
        return len(self.correct_guesses) > 0

    def count_correct_guesses(self):
        return len(self.correct_guesses)

    def print_state_name(self, state_name):

        self.setposition(find_state_coordinate(state_name))
        self.write(arg=state_name, font=FONT, align=FONT_ALIGNMENT)

    def generate_to_learn_file(self):

        missed_states = [state for state in self.all_states if state not in self.correct_guesses]

        file_data_dict = {
            'Missed States': missed_states
        }

        file_data = pandas.DataFrame(file_data_dict)
        file_data.to_csv('states_to_learn.csv')
