from tkinter import *

def save_data():
    fileD = open("deliveries.txt", "a")

    fileD.write("Depot:\n")
    fileD.write("%s\n" % depot.get())

    fileD.write("Description:\n")
    fileD.write("%s\n" % description.get())

    fileD.write("Address:\n")
    fileD.write("%s\n" % address.get("1.0", END))
    depot.set("Select Depot")
    description.delete(0, END)
    address.delete("1.0", END)

def read_depots(file):
    depots = []
    depots_f = open(file)
    for line in depots_f:
        depots.append(line.rstrip())
    return depots

app = Tk()
app.title('Head-Ex Deliveries')

Label(app, text = "Depot:").pack()
depot = StringVar()
depot.set("Select Depot")
options = read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()

'''
depots = ["Vancouver, BC, CA", "Montréal, QC, CA", "Cambridge, UK", "Seattle, WA, US", "Cambridge, MA, US"]
OptionMenu(app, depot, *depots).pack()

Radiobutton(app, text = "Vancouver, BC", value = "Vancouver, BC", variable = depot).pack()
Radiobutton(app, text = "Montréal, QC", value = "Montreal, QC", variable = depot).pack()
Radiobutton(app, text = "Cambridge, UK", value = "Cambridge, UK", variable = depot).pack()
Radiobutton(app, text = "Seattle, WA", value = "Seattle, WA", variable = depot).pack()
Radiobutton(app, text = "Cambridge, MA", value = "Cambridge, MA", variable = depot).pack()
'''

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()

app.mainloop()



