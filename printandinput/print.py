print("Hello"*5)

a,b=10,5
print(a,b,sep='--') # sep -> seperator

name = "Karthikeya"
marks = 95
print("Student name is", name, "and his marks are", marks)
# %s, %i, %f - string, integer and float place holders
print("Student name is %s and his marks are %i" %(name, marks))
print("Student name is %s and his marks are %.2f" %(name, marks)) #two places after decimal
print("Student name is {} and his marks are {}" .format(name, marks))


