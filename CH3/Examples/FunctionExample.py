import time

#First kind of function definition
def displayWelcome():
    print("####################################")
    print("#Welcome human to our alien world  #")
    print("#You are so welcome here           #")
    print("#We will love to EAT you           #")
    print("####################################")
    print()

#Second kind of function definition
def taxCalculation():
    price = 100            
    tax = 1.07
    revisedPrice = price * tax
    return revisedPrice

#Third kind of function definition
def taxCalculation2(price):
    tax = 1.07
    revisedPrice = price * tax
    return revisedPrice

#First kind of function call
displayWelcome()

#Second kind of function call
finalPrice = taxCalculation()
print("Final price is: " + str(finalPrice))
print()

#Third kind of function call
dollar = input("Please enter a cost value: ")
dollar = float(dollar)
adjustedPrice = taxCalculation2(dollar)
print("Final price is: " + str(adjustedPrice))



#dollar = input("Please enter a cost value: ")
#dollar = float(dollar)
#price = taxCalculation2(dollar)
#print("Final price is: " + str(price))
