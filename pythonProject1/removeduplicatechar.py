'''you will have to loop through the list having duplicates and add the unique items to the temporary list.
Later the temporary list is assigned to the main list'''

s = 'aaabbbsssaaddeecc'
temp = []
for c in s:
    if c not in temp:
        temp.append(c)
print(temp)

my_list = [1,1,2,2,3,3,4,44,5,5]
my_final_list = set(my_list)
print(list(my_final_list))

my_list = ['a', 'b', 'a', 'c', 'a', 'b', 'd']
my_final_list = list(dict.fromkeys(my_list))
print(my_final_list)


s='tewqdsnasdnm'
temp=[]
for a in s:
    if a not in temp:
        temp.append(a)
print(temp)