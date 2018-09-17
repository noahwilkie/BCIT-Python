#Created By Noah PW (A01019928)

print()
print("Welcome, This program will determine where you can legally drink")
print()

retry = "yes"
while retry == "yes":
    
    print()
    age = int(input("How old are you?: "))
    print()

    if age >= 21:
        print("You can legally drink in Washington and BC!")
        print()
    else:
        if age >= 19:
            print("You can legally drink in BC but not Washington")
            print()
        else:
            print("You are too young to legally drink in BC or Washington")
            print()

    retry = input("Would you like to retry?[yes or no]: ")

print()   
print("Bye")