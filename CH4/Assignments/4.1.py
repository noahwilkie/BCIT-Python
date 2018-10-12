def averagesFunc(x, y):
    average = x/y
    return average
#opens the grades file
grades_file = open("grades.txt")

#initializes the variables
total = 0
numGrades = 0

#Start of the for loop
for currentGrade in grades_file:
    print()
    print("The grade is: " + str(currentGrade.strip()) + "%")
    total = total + float(currentGrade)
    numGrades = numGrades + 1


grades_file.close()
#passes the returned value of averageFunc to gradeAverages
gradeAverages = averagesFunc(total, numGrades)
print()
print("The average grade is:", str(gradeAverages)[0:5] + "%")
print()