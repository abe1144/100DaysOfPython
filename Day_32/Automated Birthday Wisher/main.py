##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import smtplib
import pandas as pd
import random

birthdays = pd.read_csv('birthdays.csv')

letters = []
for i in range(3):
    with open("letter_templates/letter_{}.txt".format(i+1)) as f:
        letter = f.readlines()
        letters.append(letter)

my_email = "test@gmail.com"
password = "testpassword"

#today's datetime
now = dt.datetime.now()


#loop through dateframe
for index, row in birthdays.iterrows():
    if row['month'] == now.month and row['day'] == now.day:
        # modify letter
        letter = random.choice(letters)
        letter = ''.join(letter)
        letter = letter.replace("[NAME]", row['name'])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            #secures the connection to the server
            connection.starttls()

            #login
            connection.login(user=my_email, password=password)

            connection.sendmail(from_addr=my_email, 
            to_addrs=row['email'], 
            msg="Subject: Happy Birthday! \n\n {}".format(letter))
    else:
        continue