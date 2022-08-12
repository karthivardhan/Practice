s = "abcdsedgsbsvackqhjsa"
temp = []
for c in s:
    if c not in temp:
        temp.append(c)
print(temp)


num = [1,2,3,3,4,5,5,6,6,1,2,2,9,8,9,7]
temp = []
for a in num:
    if a not in temp:
        temp.append(a)
print(temp)