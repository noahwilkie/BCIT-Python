# Adding Machine (Integers Only)

# prompt user to enter numbers to add together. Print sum when they are done.

total = 0

data = input("Enter numbers - Then HIT ENTER to display total and quit: ")

while data != "":
    number = int(data)
    total = total + number
    data = input("Enter a number or just enter to quit: ")
    
print("The sum is ", total)
input() #Leave this line at end of code

# Result will look like this:
###############################################################
# Enter numbers - Then HIT ENTER to display total and quit: 2 #
# Enter a number or just enter to quit: 4                     #
# Enter a number or just enter to quit: 6                     #
# Enter a number or just enter to quit: 8                     #
# Enter a number or just enter to quit:                       #
# The sum is  20                                              #
###############################################################

# Code Magnets
# Cut & Paste the following code fragments in place of the empty "#" markers








