line = "101;Johnny 'wave-boy' Jones;USA;8.32;Fish;21"
id,name,country,avgscore,board,age = line.split(";")

s = {}
s["id"] = id
s["name"] = name
s["country"] = country
s["avg"] = avgscore
s["board"] = board
s["age"] = age

print("ID:         ",s["id"])
print("Name:       ",s["name"])
print("Country:    ",s["country"])
print("Average:    ",s["avg"])
print("Board Type: ",s["board"])
print("Age:        ",s["age"])
print(s)