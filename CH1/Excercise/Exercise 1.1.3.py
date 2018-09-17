from random import randint

print("Welcome to the Random Number generator")

bottom = input("Please enter your minimun number: ")
bottom = int(bottom)

top = input("Please enter your max number: ")
top = int(top)

playagain = "y"
while playagain != "n":  
    print(randint(bottom, top))
    playagain = input("Do you want another random number? [y or n]: ")

print("Thanks for playing")

#7 Write a loop that will print out random numbers (with a range of your choosing),
#and that prompts you whether you would like to play again, or not.

'''  It should look like the following:

Welcome to the Random Number generator

Please enter your top range number: 1
Please enter your bottom range number: 10

6
Do you want another random number: yes
3
Do you want another random number: yes
8
Do you want another random number:no

Thx for playing
'''    
