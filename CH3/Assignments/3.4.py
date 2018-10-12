#defines the function search()
def search(Search, Phrase):
    index = Phrase.find(Search)
    return index

#Greets the user
print("Hello, User :)")
print()

#start of the replay loop
replay = 'Y'
while replay == 'Y':
    
    #prompts user to input a phrase
    userInput = input("Please enter a phrase - any phrase: ")
    print()
    print("Thank you User - the phrase you entered reads as follows: \n", userInput)
    print()
    #prompts user to input word that is inside of the phrase they entered above
    userSearch = input("Please enter one of the words of the phrase you just entered, or some consecutive characters from that phrase, and I will search for them: ")
    #stores the result of the function call in a variable
    indexNum = search(userSearch,userInput)
    print()
    print("Thank you, User")
    print()
    print("Your word or characters are located at the following index location:\n", indexNum)
    print()
    #Asks user if tehy would like to run the program again
    replay = input("Thanks for playing.  Would you like to play again(Y/N)? ").upper()
    print()

#displays a leaving message
print("Goodbye, User")