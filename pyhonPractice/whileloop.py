i = 1

while i <= 6:
    print(i)
    i+=1

x = 1
while x <= 10:
    print(x)
    if x == 3:
        break
    x+=1

y = 0
while y <= 10:
    y+=1
    if y == 3:
        continue
    print("Continue statement:", y)

num = 2
while num <= 100:
    print("Even numbers:", num)
    if(num%2) == 0:
        num+=2


