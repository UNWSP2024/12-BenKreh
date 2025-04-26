import tkinter as tk

def calc_mpg():
    gallons = float(gal_user.get())
    miles = float(miles_entry.get())
    mpg = miles / gallons
    result_label.config(text="MPG: " + str(round(mpg, 2)))

window = tk.Tk()
window.title("MPG Calculator")

gal = tk.Label(window, text="Gallons:")
gal.pack()
gal_user = tk.Entry(window)
gal_user.pack()

miles_label = tk.Label(window, text="Miles:")
miles_label.pack()
miles_entry = tk.Entry(window)
miles_entry.pack()

calc_button = tk.Button(window, text="Calculate MPG", command=calc_mpg)
calc_button.pack()

result_label = tk.Label(window, text="MPG:")
result_label.pack()

window.mainloop()
