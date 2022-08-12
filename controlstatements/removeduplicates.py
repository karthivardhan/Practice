l1 = eval(input("Enter list of values: "))
print(l1)
l2 = []
for eachValue in l1:
    if eachValue not in l2:
        l2.append(eachValue)
print(l2)

#####Second method#####
l1 = eval(input("Enter list of elements: "))
s1 = set(l1) # Set doesn't allow duplicates
print(s1)
