import smtplib
import random
import datetime as dt


with open("quotes.txt") as file:
    quotes = file.readlines()


random_quote = random.choice(quotes)


my_email = "myemail@gmail.com"
password= "password"

now = dt.datetime.now()

if now.day == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
    #secures the connection to the server
        connection.starttls()

        #login
        connection.login(user=my_email, password=password)

        connection.sendmail(from_addr=my_email, 
        to_addrs="pohanlin05@gmail.com", 
        msg="Subject: Quote of the Week \n\n {}".format(random_quote))





