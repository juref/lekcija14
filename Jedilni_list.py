#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import tkMessageBox


window = Tkinter.Tk()

window.title("Jedilni List")

prazna_vrstica = Tkinter.Label(window, text="")
prazna_vrstica.pack()

tekst_jed = Tkinter.Label(window, text="Prosim vnesite jed")
tekst_jed.pack()

jed_tk = Tkinter.Entry(window)
jed_tk.pack()

tekst_cena = Tkinter.Label(window, text="Prosim vnesite ceno za jed")
tekst_cena.pack()

cena_tk = Tkinter.Entry(window)
cena_tk.pack()

jedilnik = {}


def vnos():
    jed = jed_tk.get()
    cena = cena_tk.get()
    jedilnik[jed] = cena
    removeValue(jed_tk)
    removeValue(cena_tk)


temp = []


def izpis():
    for k, v in jedilnik.iteritems():
        temp.insert(len(temp), "jed: " + k + " cena: " + v + " EUR")
    tkMessageBox.showinfo("Jedilnik", '\n'.join(temp))


def removeValue(event):
    event.delete(0, 'end')


submit = Tkinter.Button(window, text="vnesi", command=vnos)
submit.pack()

submit = Tkinter.Button(window, text="izpiši jedilnik", command=izpis)
submit.pack()


window.mainloop()