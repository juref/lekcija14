#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import Tkinter
import tkMessageBox


window = Tkinter.Tk()

window.title("ToDo")

prazna_vrstica = Tkinter.Label(window, text="")
prazna_vrstica.pack()

izbor_tekst = Tkinter.Label(window, text="Pozdravljeni v aplikaciji Loto, ki generira naključna števila.\nKoliko naključnih števil bi želeli imeti?")
izbor_tekst.pack()

izbor_tk = Tkinter.Entry(window)
izbor_tk.pack()

tekst_done = Tkinter.Label(window, text="Bi želel urediti števila od najmanšega do največjega")
tekst_done.pack()

v = Tkinter.IntVar()
Tkinter.Checkbutton(window, text="da", variable=v).pack()



def removeValue(event):
    event.delete(0, 'end')


def loto():
    if izbor_tk.get().isdigit():
        while True:
            if v.get() == 1:
                izpis = sorted(random.sample(range(1, 39), int(izbor_tk.get())))
                tkMessageBox.showinfo(
                    "Vaše generirane številke!", str(izpis))
                removeValue(izbor_tk)
                v.set(0)
                break
            else:
                izpis = random.sample(range(1, 39), int(izbor_tk.get()))
                tkMessageBox.showinfo("Vaše generirane številke!", str(izpis))
                removeValue(izbor_tk)
                v.set(0)
                break

    else:
        tkMessageBox.showinfo("Napaka!", "Prosim vnesite število")
        removeValue(izbor_tk)


submit = Tkinter.Button(window, text="Zgeneriraj", command=loto)
submit.pack()

window.mainloop()