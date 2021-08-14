import random
import tkinter as tk
from tkinter.constants import END
from tkinter import messagebox

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

    if len(website) == 0 or len(pw) == 0:
        messagebox.showinfo(
            Title="Oops", message="Please make sure you haven't left any fields empty.")
    else:

        is_ok = messagebox.askokcancel(
            title=website, message="These are the details entered: \nEmail:{} \nPassword: {} \nIs it ok to save?".format(user, pw))

        if is_ok:
            with open("data.txt", "a") as f:
                f.write("{}|{}|{} \n".format(website, user, pw))
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

website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

user_entry = tk.Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)

pw_entry = tk.Entry(width=21)
pw_entry.grid(row=3, column=1)

gen_btn = tk.Button(text="Generate Password", command=generate_password)
gen_btn.grid(row=3, column=2)

add_btn = tk.Button(text="Add", width=30, command=save_info)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
