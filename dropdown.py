from Tkinter import *

master = Tk()

variable = StringVar(master)
variable.set("kilometri v milje") # default value

w = OptionMenu(master, variable, "kilometri v milje", "milje v kilometre")
w.pack()

mainloop()