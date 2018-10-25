#Iniatializes the Array & Variables
gradeTotal = []
total = 0
avg = 0 

#Displays   
print("Welcome")
print()
print("This program will calculate your average grade")
print("Please enter all your grades, one at a time,")
print("and when you are finished, press the 'Enter' key")
print()

#Prompts user for input
gradeInput = input("Please enter a grade: ")

#Loop that appends user input to the array
while gradeInput != "":
    gradeTotal.append(gradeInput)
    gradeInput = input("Please enter a grade: ")

#Itterates through the array and totals them together 
for calc in gradeTotal:
    total = total + float(calc)
    avg = avg + 1


#Calculates the average
gradeAverage = total/avg
print()
print("Your average grade is ", gradeAverage)    
