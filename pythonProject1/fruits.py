fruits = ["Mango", "Banana", "Orange", "Apple", "Grapes"]
a, b, c, d, e = fruits
print(a)
print(b)
print(c)
print(d)
print(e)

std_marks = 71
if std_marks>=70:
    print("Student scored A grade")
elif std_marks>=60:
    print("Student scored B Grade")
else:
    print("Student scored C grade")

a = 10
b = 15
print("A") if a > b else print("=") if a == b else print("<")

a = 10
b = 5
c = 20
if a>b and a<c:
    print("Both the conditions are true")
else:
    print("Both the conditions are false")

# Nested-if:- You can have if statements inside if statements, this is called nested if statements.
x = 10
if x>1:
    print("above 1")
    if x>5:
        print("above 5")
    else:
        print("more than 10")