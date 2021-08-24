import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", font=(
        FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
    tracker.config(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12))
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        title.config(text="Work!", fg=GREEN)
        countdown(work_sec)
    elif reps % 2 == 0:
        title.config(text="Break", fg=RED)
        countdown(short_break_sec)
    elif reps % 8 == 0:
        title.config(text="Break", fg=PINK)
        countdown(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):

    min = math.floor(count / 60)
    sec = count % 60

    if sec < 10:
        sec = "0{}".format(sec)

    canvas.itemconfig(timer_text, text="{}:{}".format(min, sec))
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)

    else:
        start_timer()

        if reps % 2 == 0:
            tracker.config(text=tracker.cget("text") + checkmark)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(200, 200, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="0:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title = tk.Label(text="Timer", font=(
    FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
title.grid(row=0, column=1)

start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)


tracker = tk.Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12))
tracker.grid(row=3, column=1)


window.mainloop()
