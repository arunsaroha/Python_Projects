import smtplib
import datetime as dt
import random

my_email = "arunsaroha080@gmail.com"
my_password = "einpeinsafetypin"

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
#       the above line will save all the quotes
#       as a list
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="arunsaroha94@gmail.com",
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )


















