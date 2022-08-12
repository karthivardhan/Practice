x = 10

if x>1:
    print("X is greater than 1")
else:
    print("x is smaller than 1")

# Nested if

a = int(input("Enter a number: "))

if a > 10:
    print('a is greater than 10')
    if a > 20:
        print("also above 20")
    else:
        print("a is equal to 10")


y = 10
z = 20

if y > z:
    print('y is more than z')
elif y==z:
    print("Y is equal to z")
else:
    print("y is less than z")


i = int(input("Enter a number: "))
if (i%2) == 0:
    print(i, "is an even number")
else:
    print(i, "is an odd number")


