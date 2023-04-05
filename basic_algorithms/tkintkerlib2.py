from tkinter import *
from tkinter import messagebox

pencere = Tk()

pencere.title("deneme2")
pencere.geometry("320x175")

app=Frame(pencere)
app.grid()

L1 = Label(app, text="İfade Girin")
L1.grid(padx=110, pady=10)

E1 = Entry(app, bd=2)
E1.grid(padx=100, pady=3)

pencere.mainloop()