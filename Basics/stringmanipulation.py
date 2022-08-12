str = "Hello"
print(str[::-1])

print(str.lower())
print(str.upper())
print(str[0:1])
print(str[2:])
print(str.count('l'))
print(len(str))
print(str.replace('o', 'a'))
list1 = list(str)
print(list1)


####Reverse string#########
str = 'ab@#cdef$%ghij'
liststr = list(str)
i=0
j=len(liststr)-1
while i<j:
    if not liststr[i].isalpha():
        i+=1
    elif not liststr[j].isalpha():
        j-=1
    else:
        liststr[i], liststr[j]=liststr[j], liststr[i]
        i+=1
        j-=1

strout=''.join(liststr)
print(strout)

##############
str = 'How are you'
print(str[::-1])

list1 = list(str)
print(list1[::-1])

