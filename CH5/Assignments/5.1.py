#  function that displays a menu to the user
def contactsMenu():
    print("Contact List Menu:\n")
    print("1. Add a Contact")
    print("2. Display Contacts")
    print("3. Exit\n")

#  function that adds a new contact to the contacts file
def newContacts():
    contactFile = open("Contacts.txt", "a+")
    contactName = input("Enter Contact Name [First & Last]: ")
    contactFile.write(contactName + ':')
    contactNumber = str(input("Enter Contact Number [nnn-nnn-nnnn]: "))
    contactFile.write(contactNumber + "\n")
    contactFile.close()
    
#  function that displays the contents of the contacts file
def showContacts():
    showTxt = open("Contacts.txt")
    for contact in showTxt:
        conHash = {}
        conHash['name'], conHash['number']= contact.split(":")
        print("Name: ", conHash['name'])
        print("Number: ", conHash['number'])
    print("Shows contacts\n")

# Start of the code body
print("Welcome to the Contact List Program")

# displays a menu to the user
contactsMenu()

# loop to prompt user input
option = int(input("What would you like to do?: "))
while option != 3:
     if option == 1:
        # calls the newContact function
         newContacts()
     elif option == 2:
        # calls the showContact function
         showContacts()
     contactsMenu()
     option = int(input("What would you like to do?: "))

# goodbye msg
print("Thanks for using my Contact List Program")

