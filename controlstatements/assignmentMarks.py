mathsMarks = 95
chemistryMarks = 60
physicsMarks = 55
if (mathsMarks>=35 and chemistryMarks>=35 and physicsMarks>=35):
    print("Student is passed")
else:
    print("Student failed")
avg = (mathsMarks+chemistryMarks+physicsMarks)/3
if (avg>=70):
    print("Student scored grade A")
elif (avg>=59):
    print("Student scored grade B")
else:
    print("Student scored grade C")

###################################################################################################
# Second method
#maths,chemistry,physics = [int(x) for x in input("Enter Maths,Chemistry,Physics marks: ").split()]
maths = int(input("Enter Maths marks: "))
chemistry = int(input("Enter Chemistry marks: "))
physics = int(input("Enter Physics marks: "))
if (maths>=35 and chemistry>=35 and physics>=35):
    print("Student is passed exams")
else:
    print("Student failed in exams")
avgMarks = (maths+chemistry+physics)/3
print("Percentage scored: ", avgMarks, "%")
if (avgMarks>=60):
    print("Student scored grade A")
elif (avgMarks>=59):
    print("Student scored grade B")
else:
    print("Student scored grade C")

