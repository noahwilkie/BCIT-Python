def save_data():
        try:
                fileD = open("deliveries.txt", "a")
                fileD.write("Depot:\n")
                fileD.write("%s\n" % depot.get())
                fileD.write("Description:\n")
                fileD.write("%s\n" % description.get())
                fileD.write("Address:\n")
                fileD.write("%s\n" % address.get("1.0", END))
                depot.set("")
                description.delete(0, END)
                address.delete("1.0", END)
        except Exception as ex:
            app.title("Can’t write to the file %s" % ex)



    
