from random import randint


#5 Make the following code work correctly by putting in the correct indentations,
#AND by adding appropriate input statements which will initialize the two variables.
'''
fuel = input("How much fuel do you have in your car? : ")
fuel = int(fuel)

if fuel > 3:
    print("It's OK")
    print("You can drive downtown.")
else:
    money = input("How much money do you have left? : ")
    money = int(money)
    if money > 10:
        print("You should buy some gas.")
    else:
        print("You better stay at home.")
        print("What's next?")
'''

#6 Using the previous code, replace the input statements so that
#random numbers make the decision, rather than user input.

fuel = randint(0, 10)

if fuel > 3:
    print("It's OK")
    print("You can drive downtown.")
else:
    money = randint(0,20)
    if money > 10:
        print("You should buy some gas.")
    else:
        print("You better stay at home.")
        print("What's next?")
