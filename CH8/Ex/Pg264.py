from tkinter import *

app = Tk()
app.title('Head-Ex Deliveries')
Label(app, text = "Depot:").pack()


Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()
app.mainloop()

