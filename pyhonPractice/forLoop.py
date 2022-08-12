
for a in range(1,10):
    print(a)

for i in range(2,100,2):
    print("Even numbers:", i)

for num in range(2,100):
    if (num%2)==0:
        print("Even numbers:", num)
        num+=1

# Nested loops
num1 = [1, 2, 3, 4, 5]
num2 = [1, 2, 3, 4, 5]

for x in num1:
    for y in num2:
        print(x,y)


adj = ["Red", "Big", "Tasty"]
fruits = ["Apple", "Banana", "Cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# Add first 5 natural numbers
n = 0
for i in range(1,6):
    n+=i
print(n)

# print even number from list
a = [1,2,3,4,5,6,7,8,9,10]
for i in a:
    if (i%2==1):
        print(i, end=" ")

char = "RV49CJ0AUTS172Y"
split_strings = []
n = len(char) // 3
for index in range(0, len(char), n):
    split_strings.append(char[index: index + n])
print(" ".join(split_strings))



rows = 5
for i in range(0, rows):
    for j in range(0, i+1):
        print('*', end=" ")
    print()

r = 5
for a in range(0, r):
    for b in range(0, r-a):
        print('1', end=" ")
    print()

#Pyramid#
n = 10
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print('* '*i)

students = {"John":['Python', 'Selenium'], "Mike":['Java', 'Angular'], "David": ['Cypress', 'JavaScript']}
keys = students.keys()
for eachkey in keys:
    print("Courses taken by", eachkey,':')
    for eachCourse in students[eachkey]:
        print(eachCourse)

# Reverse letters
strSpecial = 'abc$#efghi&&^%jk'
liststr = list(strSpecial)
i=0
j=len(liststr)-1
while i<j:
    if not liststr[i].isalpha():
        i+=1
    elif not liststr[j].isalpha():
        j-=1
    else:
        liststr[i], liststr[j] = liststr[j], liststr[i]
        i+=1
        j-=1
strOut = ''.join(liststr)
print(strOut)

#### print vowels ####
sentence = input("Enter a sentence: ")
for letter in sentence:
    if letter in 'aeiouAEIOU':
        print(letter, end=' ')