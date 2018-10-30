line = "101;johnny 'wave-boy' Jones;USA;8.32;Fish;21"

s = {}
s['id'],s['name'],s['country'],s['avgscore'],s['board'],s['age'] = line.split(";")

print("ID:         ",s["id"])
print("Name:       ",s["name"])
print("Country:    ",s["country"])
print("Average:    ",s["avgscore"])
print("Board Type: ",s["board"])
print("Age:        ",s["age"])
print(s)
