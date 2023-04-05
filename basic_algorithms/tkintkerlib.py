from tkinter import *
from tkinter import messagebox

pencere = Tk()

pencere.title("deneme title")
pencere.geometry('400x400')

app = Frame(pencere)
app.grid()

Lb1 = Listbox(app)
Lb1.insert(1, "İstanbul")
Lb1.insert(2, "Ankara")
Lb1.insert(3, "İzmir")
Lb1.insert(4, "Kayseri")
Lb1.insert(5, "Antalya")
Lb1.grid(padx=110, pady=10)
 
pencere.mainloop()