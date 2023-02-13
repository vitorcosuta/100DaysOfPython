from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ('Arial', 10, 'normal')


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website_name = website_entry.get()
    try:
        with open(file='password_list.json', mode='r') as password_file:
            data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showwarning(title='Error', message='No data file found.')
    else:
        if website_name in data:
            saved_email = data[website_name]['email']
            saved_password = data[website_name]['password']
            messagebox.showinfo(title=f'{website_name}', message=f'Email: {saved_email}\nPassword: {saved_password}')
        else:
            messagebox.showwarning(title='Error', message="There's no info regarding the input website.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)  # Deleting the previous password
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Transferring the password to the user's clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_entry(*args):

    for entry in args:
        entry.delete(0, END)


def is_valid_entry(*args):

    for entry in args:
        if entry == '':
            messagebox.showwarning(title='Oops!', message="Please don't leave any fields empty.")
            return False
    return True


def save_new_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:
        {
            'email': email,
            'password': password,
        }
    }

    valid_entries = is_valid_entry(website, email, password)

    if valid_entries:

        is_ok_to_save = messagebox.askokcancel(
            title='Please confirm your data',
            message=f"These are the details entered:\n\nEmail: {email}\nPassword: {password}\n\nIs this ok to save?"
        )

        if is_ok_to_save:
            try:
                with open(file='password_list.json', mode='r') as password_file:
                    # Reading old data
                    data = json.load(password_file)
            except FileNotFoundError:
                with open(file='password_list.json', mode='w') as password_file:
                    json.dump(new_data, password_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open(file='password_list.json', mode='w') as password_file:
                    # Saving updated data
                    json.dump(data, password_file, indent=4)
            finally:
                clear_entry(website_entry, password_entry)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.minsize(width=480, height=385)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_text = Label(text='Website:')
website_text.config(font=FONT)
website_text.grid(row=1, column=0)

email_text = Label(text='Email/Username:')
email_text.config(font=FONT)
email_text.grid(row=2, column=0)

password_text = Label(text='Password:')
password_text.config(font=FONT)
password_text.grid(row=3, column=0)

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, sticky='EW')
website_entry.focus()

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky='EW')
email_entry.insert(0, 'test@email.com')

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky='EW')

# Buttons
gen_password_button = Button(text='Generate Password', command=generate_random_password)
gen_password_button.grid(row=3, column=2, sticky='EW')

add_button = Button(text='Add', width=50, command=save_new_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text='Search', command=search_password)
search_button.grid(row=1, column=2, sticky='EW')

window.mainloop()
