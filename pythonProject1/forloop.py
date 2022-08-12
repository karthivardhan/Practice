fruits = ['Apple', 'Orange', 'Banana']
for x in fruits:
    print(x)

fruits = ['Apple', 'Orange', 'Banana'] # prints Apple and Orange
for x in fruits:
    if x == 'Banana':
        break
    print(x)

fruits = ['Apple', 'Orange', 'Banana'] # prints Apple and Orange
for x in fruits:
    print(x)
    if x == 'Orange':
        break

for i in range(5): # Prints 0 to 4
    print(i)

for i in range (1,6):
    print(i)

for i in range(1,30,3):
    print(i)

rows = 5
for i in range(0, rows):  # outer loop to handle number of rows
    for j in range(0, i+1):  # inner loop to handle number of columns.values are changing according to outer loop.
        print('* ', end="")  # printing stars
    print()  # ending line after each row

## Reverse
rows = 5
for i in range(0, rows):
    for j in range(0, rows-i):
        print('* ', end="")
    print()

## Pyramid

n = 10
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print('* '*i)
