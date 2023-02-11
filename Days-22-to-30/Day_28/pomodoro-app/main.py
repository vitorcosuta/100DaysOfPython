from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    checkmark_label.config(text='')

    global repetitions
    repetitions = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repetitions
    repetitions += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repetitions % 8 == 0:
        timer_label.config(text='long break', fg=RED)
        countdown(long_break_sec)
    elif repetitions % 2 == 0:
        timer_label.config(text='short break', fg=PINK)
        countdown(short_break_sec)
    else:
        timer_label.config(text='work', fg=GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_min = count // 60
    count_sec = count % 60

    if count_sec // 10 == 0:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()

        marks = ''
        for _ in range(repetitions//2):
            marks += '✔'
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 115, image=tomato_img)
timer_text = canvas.create_text(102, 135, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=1, column=1)

timer_label = Label(text='Timer')
# We can change the text color using the kwarg 'fg=', which stands for 'foreground'
timer_label.config(fg=GREEN, font=(FONT_NAME, 40, 'bold'), bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text='START', command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='RESET', command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_label = Label(font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)

window.mainloop()
