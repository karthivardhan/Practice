lst = [5, 10, 'Test', 2.9, True, -10]
print(lst)
print(lst[1])
print(lst*2) #repeated 2 times

lst.append(1)
lst.remove(2.9)
del(lst[2])
lst.insert(3, 99) # insert in 3rd index
print(lst)
print(min(lst)) #min value
print(max(lst)) #max value

lst.sort()
print(lst)
lst.sort(reverse=True) #Desending order
print(lst)

#Assignment
lst1 = ['India', 'United States', 'South Africa']
lst1.append('Canada')
print(lst1)
del (lst1[1])
print(lst1)
lst1.insert(1, 'Spain')
print(lst1)

#Escape Characters
print("Karthieya is 'Awasome and cool' ")
print("Devaansh is \"Awasome and cool\" ")
print("You are \nAwasome and cool ")