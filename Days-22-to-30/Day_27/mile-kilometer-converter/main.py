from tkinter import *

FONT = ('Arial', 9, 'normal')
MI_TO_KM_CONVERSION_CONSTANT = 1.609


def convert():
    mile_dist = int(entry.get())
    km_dist = round(mile_dist * MI_TO_KM_CONVERSION_CONSTANT, 3)
    return km_dist


def show_conversion():
    result_label.config(text=str(convert()))


window = Tk()
window.title('Mi-Km Converter')
window.minsize(width=300, height=200)
window.config(padx=30, pady=50)

# Creating text labels
text_label_1 = Label(text='is equal to')
text_label_1.config(font=FONT, pady=10, padx=10)
text_label_1.grid(row=1, column=0)

text_label_2 = Label(text='Miles')
text_label_2.config(font=FONT, pady=10, padx=10)
text_label_2.grid(row=0, column=2)

text_label_3 = Label(text='Kilometers')
text_label_3.config(font=FONT, pady=10, padx=10)
text_label_3.grid(row=1, column=2)

result_label = Label(text='0')
result_label.config(font=('Arial', 9, 'bold'), pady=10, padx=10)
result_label.grid(row=1, column=1)

# Creating an entry
entry = Entry(width=10)
entry.insert(END, string='0')
entry.grid(row=0, column=1)

# Creating button
button = Button(text='Calculate', command=show_conversion)
button.grid(row=2, column=1)

window.mainloop()
