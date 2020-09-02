numGrade = int(input("Enter the Numerical grade"))
if numGrade >= 90:
    letterGrade = "A"
elif numGrade >= 80:
    letterGrade = "B"
elif numGrade >= 70:
    letterGrade = "C"
elif numGrade >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"

print ("The letter grade is {}".format(letterGrade))
