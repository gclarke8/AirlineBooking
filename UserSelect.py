from tkinter import *
# Importing library
import tkinter as tk

# Defining option list
OptionList = [
    "Business Select",
    "Business (Regular)",
    "Family(1 Child)",
    "Family(2 Children)",
    "Family(3 Children)",
    "Tourist",
]

app = tk.Tk()

# Font and orientation setup
app.geometry('500x500')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack(side="top")

# Confirm Button
labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

var = StringVar()
label = Label(app, textvariable=var, relief=RAISED)

var.set("Confirm")
label.pack()


# Function
def callback(*args):
    labelTest.configure(text="The selected item is {}".format(variable.get()))


variable.trace("w", callback)

app.mainloop()
