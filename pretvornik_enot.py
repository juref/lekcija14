#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
from Tkinter import *
import tkMessageBox

window = Tkinter.Tk()

window.title("Pretvornik enot")

prazna_vrstica = Tkinter.Label(window, text="")
prazna_vrstica.pack()

tekst = Tkinter.Label(window, text="Izberite željeno pretvorbo")
tekst.pack()

izbor = StringVar(window, "izberi")


w = OptionMenu(window, izbor, "kilometri v milje", "milje v kilometre")
w.pack()

prazna_vrstica = Tkinter.Label(window, text="")
prazna_vrstica.pack()

vnost_tekst = Tkinter.Label(window, text="Vnesite število ki ga želite pretvoriti")
vnost_tekst.pack()

vnos_tk = Tkinter.Entry(window)
vnos_tk.pack()


def convert():
    km = vnos_tk.get().replace(',','.')
    if not km.isalpha():
        if izbor.get() == "kilometri v milje":
            pretvorba = float(km) * 0.62137119
            tkMessageBox.showinfo("izračun", str(km) + " km = " + str(round(pretvorba, 2)) + " mi")
        elif izbor.get() == "milje v kilometre":
            pretvorba = float(km) * 1.61
            tkMessageBox.showinfo("izračun", str(km) + " mi = " + str(round(pretvorba, 2)) + " km")
        else:
            tkMessageBox.showinfo("napaka!", "Prosim izberite pretvorbo")
    else:
        tkMessageBox.showinfo("napaka!", "Prosim vnesite število")


submit = Tkinter.Button(window, text="izračunaj", command=convert)
submit.pack()


window.mainloop()