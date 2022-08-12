lst = [1,2,3,4,5,6]
for i in lst:
    if (i==5):
        break #the loop will break at 5 and print numbers before to number 5
    print(i)

###### While loop #######

choc = 5 # available chocolates
x = int(input("How many chocolates you want?: "))
i = 1
while i<=x:
    if i>choc:
        print("Out of stock")
        break
    print('Chocolates')
    i+=1

