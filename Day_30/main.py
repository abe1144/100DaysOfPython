import random
import tkinter as tk
from tkinter.constants import END
from tkinter import messagebox
import json


# ---------------------------- Find PASSWORD ------------------------------- #

def find_password():
    with open("data.json", "r") as f:
        data = json.load(f)

    search_query = website_entry.get()
    if search_query in data.keys():
        messagebox.showinfo(title="{} Account Info".format(search_query), message="Email:{} \nPassword:{}".format(
            data[search_query]['email'], data[search_query]['password']))
    else:
        messagebox.showerror(title="Account not found",
                             message="account not found.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = ''.join(password_list)

    pw_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_info():
    website = website_entry.get()
    user = user_entry.get()
    pw = pw_entry.get()
    new_data = {website: {
        "email": user,
        "password": pw,
    }}

    if len(website) == 0 or len(pw) == 0:
        messagebox.showinfo(
            Title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as f:
                # reading old data
                data = json.load(f)
                # updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            user_entry.delete(0, END)
            pw_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
lock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

user_label = tk.Label(text="Email/Username:")
user_label.grid(row=2, column=0)

pw_label = tk.Label(text="Password:")
pw_label.grid(row=3, column=0)

website_entry = tk.Entry(width=21)
website_entry.grid(row=1, column=1)

user_entry = tk.Entry(width=40)
user_entry.grid(row=2, column=1, columnspan=2)

pw_entry = tk.Entry(width=21)
pw_entry.grid(row=3, column=1)

gen_btn = tk.Button(text="Generate Password", command=generate_password)
gen_btn.grid(row=3, column=2)

add_btn = tk.Button(text="Add", width=31, command=save_info)
add_btn.grid(row=4, column=1, columnspan=2)

search_btn = tk.Button(text="Search", width=15, command=find_password)
search_btn.grid(row=1, column=2)

window.mainloop()
