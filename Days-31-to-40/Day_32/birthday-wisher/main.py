import datetime as dt
import pandas
import random
import smtplib

PLACEHOLDER = '[NAME]'
LETTER_FORMATS = ('letter_1', 'letter_2', 'letter_3')
SMTP_ADDRESS = "outlook.office365.com"
EMAIL = "test@outlook.com"
PASSWORD = "abc123()"


def create_birthday_message(receiver_name):

    letter_format = random.choice(LETTER_FORMATS)

    with open(f'letter_templates/{letter_format}.txt', mode='r') as starting_letter:
        original_letter = starting_letter.read()

    edited_letter = original_letter.replace(PLACEHOLDER, receiver_name)

    return edited_letter


def send_birthday_message(recipient_email, message):

    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=recipient_email,
            msg=f'Subject:Happy Birthday!\n\n{message}'
        )


now = dt.datetime.now()
birthday_data = pandas.read_csv('birthdays.csv')

for (index, row) in birthday_data.iterrows():

    birth_day = row['day']
    birth_month = row['month']

    if birth_day == now.day and birth_month == now.month:

        send_birthday_message(row['email'], create_birthday_message(row['name']))
