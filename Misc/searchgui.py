from tkinter import *
from tkinter.ttk import *
import webbrowser
def search():
    term = searchBox.get()
    url = "https://www.google.ca/search?q={}".format(term)
    webbrowser.open_new_tab(url)
app = Tk()
app.title("Search")
app.geometry("350x100")
app.columnconfigure(0, weight=1)
app.columnconfigure(3, weight=1)
app.rowconfigure(0,weight=1)
app.rowconfigure(3,weight=1)
Label(app,text="Totally Official Google Search GUI").grid(row=1,column=1)
searchBox = Entry(app, width=35)
searchBox.focus()
searchBox.grid(column=1,row=2)
Button(app, text="Search", command=search).grid(column=2,row=2)

app.mainloop()