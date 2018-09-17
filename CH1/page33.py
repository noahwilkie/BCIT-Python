from random import randint
secret = randint(1, 10)

print("Welcome to my program")

guess = 0
while guess != secret:

    g = input("Guess the number: ")
    guess = int(g)

    if guess == secret:
        print("You Win!")
    else:
        if guess > secret:
            print("Too High")
        else:
            print("Too Low")

print("Game Over")
