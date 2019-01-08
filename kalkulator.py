#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import tkMessageBox

class textColor:
    RESET = '\033[0m'
    BOLD = '\033[01m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'

window = Tkinter.Tk()

window.title("K A L K U L A T O R")

prazna_vrstica = Tkinter.Label(window, text="")
prazna_vrstica.pack()

tekst_prvo = Tkinter.Label(window, text="Vnesite prvo število")
tekst_prvo.pack()

prvo_tk = Tkinter.Entry(window)
prvo_tk.pack()

tekst_drugo = Tkinter.Label(window, text="Vnesite drugo število")
tekst_drugo.pack()
drugo_tk = Tkinter.Entry(window)
drugo_tk.pack()

tekst_znak = Tkinter.Label(window, text="Vnesite željeno funkcijo + , - , * , / ")
tekst_znak.pack()
znak_tk = Tkinter.Entry(window)
znak_tk.pack()


class textColor:
    RESET = '\033[0m'
    BOLD = '\033[01m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'


### funkcija račun ###
def operacija(x, znak, y):
    if znak == "+":
        izracun = float(x) + float(y)
    elif znak == "-":
        izracun = float(x) - float(y)
    elif znak == "*":
        izracun = float(x) * float(y)
    elif znak == "/":
        izracun = float(x) / float(y)
    print textColor.GREEN + textColor.BOLD + str(x) + " + " + str(y) + " = " + (str(round(izracun, 3))).rstrip('0').rstrip('.') + textColor.RESET if '.' in (
        str(round(izracun, 3))) else (str(round(izracun, 3))) + textColor.RESET
    return str(x) + " + " + str(y) + " = " + (
        str(round(izracun, 3))).rstrip('0').rstrip('.') if '.' in (str(round(izracun, 3))) else (str(round(izracun, 3)))
### END funkcija račun ###


def removeValue(event):
    event.delete(0, 'end')


def kalkulator():

    todo_list = []
    result_text = ""
    while True:
        stevilo = prvo_tk.get()
        if not stevilo.isdigit() or len(stevilo) == 0:
            prvo_napaka = "Napaka v prvem polju! To ni število!"
            tkMessageBox.showinfo("Napaka", prvo_napaka)
            break
        else:
            todo_list.append(stevilo)
            break

    while True:
        znak = znak_tk.get()
        if not znak in ("+", "-", "*", "/"):
            znak_napaka = "Nepoznana funkcija!"
            tkMessageBox.showinfo("Napaka", znak_napaka)
            break
        else:
            todo_list.append(znak)
            break

    while True:
        stevilo = drugo_tk.get()
        if not stevilo.isdigit() or len(stevilo) == 0:
            drugo_napaka = "Napaka v drugem polju! To ni število!"
            tkMessageBox.showinfo("Napaka", drugo_napaka)
            break

        else:
            todo_list.append(stevilo)
            break

    if len(todo_list) == 3:
        history_list = operacija(todo_list[0], todo_list[1], todo_list[2])
        history.append(history_list)
        tkMessageBox.showinfo("Rezultat", history_list)
        removeValue(prvo_tk)
        removeValue(drugo_tk)
        removeValue(znak_tk)

def zgodovina():
    if len(history) == 0:
        tkMessageBox.showinfo("Napaka", "Ni zgodovine")
    tkMessageBox.showinfo(
        "Pretekli izračuni:",
        '\n'.join(history)
    )


history = []

submit = Tkinter.Button(window, text="izračunaj", command=kalkulator)
submit.pack()

prazna_vrstica = Tkinter.Label(window, text="")
prazna_vrstica.pack()

zgodovina = Tkinter.Button(window, text="Pokaži zgodovino", command=zgodovina)
zgodovina.pack()

window.mainloop()