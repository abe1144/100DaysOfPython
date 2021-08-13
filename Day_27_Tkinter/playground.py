import tkinter

window = tkinter.Tk()

window.title("GUI")
window.minsize(width=500, height=300)

# label
mylabel = tkinter.Label(text="a label", font=("Arial", 24, "bold"))
# places the label on screen
mylabel.pack()


# button
def button_clicked():
    mylabel.config(text="Button got clicked")
    print(input.get())


button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

# entry
input = tkinter.Entry(width=10)
input.pack()

# keeps the window in the screen and listens for interactivity
# needs to be at end of program
window.mainloop()
