import tkinter as tk
from tkinter import messagebox

def calc_call():
    mins = float(min_entry.get())
    if rate.get() == 1:
        cost = mins * 0.02
    elif rate.get() == 2:
        cost = mins * 0.12
    elif rate.get() == 3:
        cost = mins * 0.05
    messagebox.showinfo("Call Cost", "Total cost: $" + str(round(cost, 2)))

win = tk.Tk()
win.title("Call Charge Calculator")

tk.Label(win, text="Minutes:").pack()
min_entry = tk.Entry(win)
min_entry.pack()

rate = tk.IntVar()

tk.Radiobutton(win, text="Daytime ($0.02)", variable=rate, value=1).pack()
tk.Radiobutton(win, text="Evening ($0.12)", variable=rate, value=2).pack()
tk.Radiobutton(win, text="Off-Peak ($0.05)", variable=rate, value=3).pack()

tk.Button(win, text="Calculate Charge", command=calc_call).pack()

win.mainloop()
