from tkinter import *

window = Tk()
window.title("Mile to Kilometer converter")
window.minsize(width=350, height=100)

def mile_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    nb_km_label.config(text=f"{km}")


miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

nb_km_label = Label(text="0")
nb_km_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
