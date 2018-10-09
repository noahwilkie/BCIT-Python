def search(Search, Phrase):
    index = Phrase.find(Search)
    return index

print("Hello, User :)")
print()
replay = 'Y'
while replay == 'Y':

    userInput = input("Please enter a phrase - any phrase: ")
    print()
    print("Thank you User - the phrase you entered reads as follows: \n", userInput)
    print()
    userSearch = input("Please enter one of the words of the phrase you just entered, or some consecutive characters from that phrase, and I will search for them: ")
    
    userSearch = search(userSearch,userInput)
    
    print()
    print("Thank you, User")
    print()
    print("Your word or characters are located at the following index location:\n", userSearch)
    print()
    replay = input("Thanks for playing.  Would you like to play again(Y/N)? ").upper()
    print()

print("Goodbye, User")