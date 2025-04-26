import tkinter as tk

def calc_total():
    total = 0
    if oil.get():
        total += 30
    if lube.get():
        total += 20
    if rad.get():
        total += 40
    if trans.get():
        total += 100
    if insp.get():
        total += 35
    if muff.get():
        total += 200
    if tire.get():
        total += 20
    total_label.config(text="Total amount due: $" + str(total))

root = tk.Tk()
root.title("Joe's Automotive")

oil = tk.IntVar()
lube = tk.IntVar()
rad = tk.IntVar()
trans = tk.IntVar()
insp = tk.IntVar()
muff = tk.IntVar()
tire = tk.IntVar()

tk.Checkbutton(root, text="Oil Change ($30)", variable=oil).pack()
tk.Checkbutton(root, text="Lube Job ($20)", variable=lube).pack()
tk.Checkbutton(root, text="Radiator Flush ($40)", variable=rad).pack()
tk.Checkbutton(root, text="Transmission Fluid ($100)", variable=trans).pack()
tk.Checkbutton(root, text="Inspection ($35)", variable=insp).pack()
tk.Checkbutton(root, text="Muffler Replacement ($200)", variable=muff).pack()
tk.Checkbutton(root, text="Tire Rotation ($20)", variable=tire).pack()

tk.Button(root, text="Show Total", command=calc_total).pack()
total_label = tk.Label(root, text="Total: $0")
total_label.pack()

root.mainloop()
