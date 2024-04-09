"""This project is to create a desktop program that converts kilometers to miles."""
from src import Converter
from tkinter import *
from tkinter import ttk

def calculate(*args):
    value = Converter.km_to_miles(float(kilometer.get()))
    miles.set(round(value, 4))


if __name__ == '__main__':
    root = Tk()
    root.title("Kilometer to Miles Converter")
    
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    kilometer = StringVar()
    kilometer_entry = ttk.Entry(mainframe, width=7, textvariable=kilometer)
    kilometer_entry.grid(column=2, row=1, sticky=(W, E))

    miles = StringVar()
    ttk.Label(mainframe, textvariable=miles).grid(column=2, row=2, sticky=(W, E))

    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

    ttk.Label(mainframe, text="kilometer").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
    ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    kilometer_entry.focus()
    root.bind("<Return>", calculate)
    
    root.mainloop()