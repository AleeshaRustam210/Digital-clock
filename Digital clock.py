import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("600x150")
root.configure(bg="yellow")


def update_time():
    current_time = strftime("%I:%M:%S %p  %d/%m/%Y")
    label.config(text=current_time)
    label.after(1000, update_time)


label = tk.Label(
    root,
    font=("Calibri", 35, "bold"),
    bg="yellow",
    fg="black"
)

label.pack(expand=True)

update_time()
root.mainloop()