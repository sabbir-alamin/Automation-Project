from tkinter import *

program = Tk()
program.minsize(width=300, height=150)
program.title("Mile to Km Converter")
program.config(padx=40, pady=40)

"""Input"""

given_mile = Entry(width=6, font="Caladea")
given_mile.grid(column=2, row=1)

"""Output"""

label4 = Label(text=0, font="Caladea")
label4.grid(column=2, row=2)

# output = Text(height=1, width=6, font="Caladea")
# print(output.get("1.0", END))
# output.grid(column=2, row=2)

"""Miles"""

label = Label(text="Miles", font="Caladea")
label.grid(column=3, row=1)
label.config(padx=10, pady=10)

"""is equal to"""

label2 = Label(text="is equal to", font="Caladea")
label2.grid(column=1, row=2)
label2.config(padx=10, pady=10)

"""calculate"""


def buttons():
    value = float(given_mile.get())
    kilometer = round((value*1.60), 2)
    label4.config(text=f"{kilometer}", font="Caladea")


button = Button(text="Calculate", font="Caladea", command=buttons)
button.grid(column=2, row=3)

"""km"""

label3 = Label(text="Km", font="Caladea")
label3.grid(column=3, row=2)
label3.config(padx=10, pady=10)

program.mainloop()
