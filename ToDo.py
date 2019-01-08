#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import tkMessageBox


window = Tkinter.Tk()

window.title("ToDo")

prazna_vrstica = Tkinter.Label(window, text="")
prazna_vrstica.pack()

tekst_opravilo = Tkinter.Label(window, text="Vnesite opravilo")
tekst_opravilo.pack()

opravilo_tk = Tkinter.Entry(window)
opravilo_tk.pack()

tekst_done = Tkinter.Label(window, text="Ali je opravilo že končano?")
tekst_done.pack()

v = Tkinter.IntVar()

Tkinter.Radiobutton(window, text="DA, je končano", variable=v, value=1).pack()
Tkinter.Radiobutton(window, text="NE, ni končano", variable=v, value=2).pack()

finished = []
unfinshed = []


def todo():
    opravilo = opravilo_tk.get()
    if v.get() == 1:
        finished.append(opravilo)
        removeValue(opravilo_tk)
        v.set(0)
    else:
        unfinshed.append(opravilo)
        removeValue(opravilo_tk)
        v.set(0)


def koncana_opravila():
    if finished:
        tkMessageBox.showinfo(
            "končana opravila so!",
            '\n'.join(finished)
        )
    else:
        tkMessageBox.showinfo("Ni končanih opravil", "V vašem spisku ni končanih opravil")


def nekoncana_opravila():
    if unfinshed:
        tkMessageBox.showinfo(
            "nekončana opravila so!",
            '\n'.join(unfinshed)
        )
    else:
        tkMessageBox.showinfo("Ni nekončanih opravil", "V vašem spisku ni nekončanih opravil")


def vsa_opravila():
    finished.insert(0, "Končana opravila so:")
    unfinshed.insert(0, "\n\nNekončana opravila so:")
    tkMessageBox.showinfo("vsa opravila", '\n'.join(finished) + '\n'.join(unfinshed))


def removeValue(event):
    event.delete(0, 'end')


submit = Tkinter.Button(window, text="vnesi", command=todo)
submit.pack()

prazna_vrstica = Tkinter.Label(window, text="")
prazna_vrstica.pack()

submit = Tkinter.Button(window, text="Pokaži končana opravila", command=koncana_opravila)
submit.pack()

submit = Tkinter.Button(window, text="Pokaži nekončana opravila", command=nekoncana_opravila)
submit.pack()

submit = Tkinter.Button(window, text="Pokaži vsa opravila", command=vsa_opravila)
submit.pack()

window.mainloop()