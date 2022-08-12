"""x=int(input("Enter min value: "))
y=int(input("Enter max value: "))
i=x
if(i%2==0):
    i=i+1
while(i<=y):
    print(i)
    i=i+2"""

###################################

for x in range(2,51,2):
    print(x)

for i in range(1,50,2):
    print(i)

list1 =[1,2,3,4,5,6,7,8,9,10]
for num in list1:
    if(num%2==0):
        print(num)

list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for num in list2:
    if(num%2==1):
        print(num)