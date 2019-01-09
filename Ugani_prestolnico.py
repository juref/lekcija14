#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import tkMessageBox
import random


window = Tkinter.Tk()

window.title("Ugani prestolnico")

country_capital_dict = {"Slovenija": "Ljubljana", "Hrvaška": "Zagreb", "Austrija": "Dunaj", "Italija": "Rim"}

x = random.randint(0, len(country_capital_dict.keys()) - 1)

selected_country = country_capital_dict.keys()[x]

prazna_vrstica = Tkinter.Label(window, text="")
prazna_vrstica.pack()

tekst_prvo = Tkinter.Label(window, text="%s ima za prestolnico mesto (vnesi spodaj)" % selected_country)
tekst_prvo.pack()

odgovor_tk = Tkinter.Entry(window)
odgovor_tk.pack()


def preveri():
    odgovor = odgovor_tk.get()
    selected_country = country_capital_dict.keys()[x]
    preveri_odgovor(odgovor, selected_country, country_capital_dict)


def preveri_odgovor(odgovor, country, cc_dict):
    capital = cc_dict[country]
    if odgovor.lower() == capital.lower():
        tkMessageBox.showinfo("Čestitamo", "Pravilno!")
        removeValue(odgovor_tk)
        exit()

    else:
        tkMessageBox.showinfo("Napačno", "Napačno! %s za prestolnico nima mesto %s." % (country, odgovor))
        removeValue(odgovor_tk)


def removeValue(event):
    event.delete(0, 'end')


submit = Tkinter.Button(window, text="Preveri", command=preveri)
submit.pack()

window.mainloop()
