import tkinter

window = tkinter.Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=100)


def output():
    miles = float(entry.get())
    km = round(1.60934 * miles)
    label_result.config(text=str(km))


entry = tkinter.Entry()
entry.grid(column=1, row=0)

label = tkinter.Label(text="is equal to", font=("Arial", 12, "bold"))
label.grid(column=0, row=1)

label_m = tkinter.Label(text="Miles", font=("Arial", 12))
label_m.grid(column=2, row=0)

label_km = tkinter.Label(text="Km", font=("Arial", 12))
label_km.grid(column=2, row=1)

label_result = tkinter.Label(text="", font=("Arial", 12))
label_result.grid(row=1, column=1)

button = tkinter.Button(text="Calculate", command=output)
button.grid(column=1, row=2)


window.mainloop()
