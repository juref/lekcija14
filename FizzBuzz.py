#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import tkMessageBox

window = Tkinter.Tk()

window.title("FizzBuzz")

prazna_vrstica = Tkinter.Label(window, text="")
prazna_vrstica.pack()

vnos_tekst = Tkinter.Label(window, text="Vnesi številko od 1 do 100:")
vnos_tekst.pack()

izbor_tk = Tkinter.Entry(window)
izbor_tk.pack()


def fizzbuzz():
    izbor = izbor_tk.get()
    if izbor.isdigit() == 0:
        napaka = "To ni število!"
        tkMessageBox.showinfo("Napaka", napaka)
    else:
        izpis = []
        for y in range(1, int(izbor) + 1):
            if y % 3 == 0 and y % 5 == 0:
                print "fizzbuz"
                izpis.append("fizzbuz")
            elif y % 3 == 0:
                print "fizz"
                izpis.append("fizz")
            elif y % 5 == 0:
                print "buzz"
                izpis.append("buzz")
            else:
                print y
                izpis.append(str(y))

        tkMessageBox.showinfo(
            "FizzBuzz goes like this:",
            '\n'.join(izpis)
        )
        removeValue(izbor_tk)


def removeValue(event):
    event.delete(0, 'end')

submit = Tkinter.Button(window, text="Do the FizzBuzz", command=fizzbuzz)
submit.pack()

window.mainloop()