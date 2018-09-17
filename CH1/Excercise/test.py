from random import randint

print("Welcome to the Random Number generator")

bottom = int(input("Please enter your minimun number: "))
top = int(input("Please enter your max number: "))

while bottom >= top:
    print("Invalid range! Your Minimum Number can't be bigger then your max number")
    bottom = int(input("Please enter your minimun number: "))
    top = int(input("Please enter your max number: "))
    


playagain = "y"
while playagain != "n":  
    print("Your number is: " + randint(bottom, top)  )
    playagain = input("Do you want another random number? [y or n]: ")

print("Thanks for playing")