for i in range(0,10):
    i+=1
    print(i)

for i in range(1,10,2):
    i+=1
    print(i)

a = [1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i%2==0:
        print( i, end=" ")

colors = ['Red', 'Black', 'Blue', 'Yellow']
for lst in colors:
    print(lst)

for i in range(0,10):
    if i==5:
        break
    print(i)

for i in range(0,11):
    if i==6:
        continue
    print(i)

###### While loop
i=0
while i<=10:
    print(i, end=' ')
    i+=1

i=0
while i<=10:
    if i==6:
        break
    print(i)
    i+=1

i=0
while i<=10:
    i += 1
    if i==6:
        continue
    print(i)