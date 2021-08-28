import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
word = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except:
    data = pd.read_csv("data/french_words.csv")
#data = pd.read_csv("data/french_words.csv")
        

to_learn = data.to_dict(orient="records")



#function that generates a new word from list
def new_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text = word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_img)
    flip_timer = window.after(3000, func=flip)
    

    
def flip():
    canvas.itemconfig(canvas_image, image=card_img_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word["English"], fill="white")
    
def is_known():
    to_learn.remove(word)
    new_word()
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)


window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip)


canvas = tk.Canvas(height=526,width=800)
card_img = tk.PhotoImage(file="images/card_front.png")
card_img_back = tk.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263,image=card_img)
title_text = canvas.create_text(400, 150,text="Title", font=("Ariel", 50, "italic"))
word_text = canvas.create_text(400,263, text="Word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)

cross_img = tk.PhotoImage(file="images/wrong.png")
cross_button = tk.Button(image=cross_img, highlightthickness=0, command=new_word)
cross_button.grid(row=1,column=0)

check_img = tk.PhotoImage(file="images/right.png")
check_button = tk.Button(image=check_img, highlightthickness=0, command=is_known)
check_button.grid(row=1,column=1)

new_word()

window.mainloop()