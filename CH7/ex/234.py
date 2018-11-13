def correct_click():
    print("Correct!")

def wrong_click():
    print("Wrong")

from tkinter import *


app = Tk()
app.title("Your tkinter application")
app.geometry('450x100+200+100')


b2 = Button(app, text = "Correct", width = 10, padx=5, pady=10, command = correct_click )
b2.pack(side='left',padx=20,pady=20)

b3 = Button(app, text = "Wrong", width = 10, padx=5, pady=10, command = wrong_click )
b3.pack(side='right',padx=20,pady=20)

app.mainloop()