a = ('How', 'are', 'you')
b = ' '.join(a)
print(b)

###########

str = "Hello"
b = str[::-1]
print(b)

a = ('How', 'are', 'you')
b = a[::-1]
print(b)

str = 'abc@#efg$hij'
str_con_list = list(str)
print(str_con_list)
i = 0
j = len(str_con_list)-1
print(j)
while i<j:
    if not str_con_list[i].isalpha():
        i+=1
    elif not str_con_list[j].isalpha():
        j-=1
    else:
        str_con_list[i], str_con_list[j] = str_con_list[j], str_con_list[i]
        i+=1
        j-=1
strOut = ''.join(str_con_list)
print(strOut)
