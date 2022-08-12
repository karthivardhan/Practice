for i in range(1, 21):
    if i%3==0:
        continue # it will not print the number which is divisible by 3 and continue the loop
    print(i)

########## While Loop ####################
x = 0
while x<20:
    x+=1
    if x%3==0 or i%5==0:
        continue
    print(x)

x = 0
while x<20:
    x+=1
    if x%3==0 and i%5==0: #it will skip numbers which are divisible by same number
        continue
    print(x)