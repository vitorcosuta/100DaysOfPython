import smtplib
import datetime as dt
import random

EMAIL = "test@outlook.com"
PASSWORD = "abc123()"

now = dt.datetime.now()
weekday = now.weekday()

# weekday() method returns an int which correspond as follows:
# 0 = Monday        4 = Friday
# 1 = Tuesday       5 = Saturday
# 2 = Wednesday     6 = Sunday
# 3 = Thursday

if weekday == 0:
    with open('quotes.txt', mode='r') as quote_file:
        monday_quotes = quote_file.readlines()

    today_quote = random.choice(monday_quotes)

    # SMTP stands for Simple Mail Transfer Protocol. Each email provider has its own SMTP address:
    #
    # Gmail: smtp.gmail.com
    # Hotmail: smtp.live.com
    # Outlook: outlook.office365.com
    # Yahoo: smtp.mail.yahoo.com
    with smtplib.SMTP("outlook.office365.com") as connection:
        # We need to call the starttls() method in order to encrypt and protect our message via TLS (Transport Layer
        # Security) protocol.
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f'Subject:Hello!\n\n{today_quote}'
        )
