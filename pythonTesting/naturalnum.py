import re
# first 5 natural num = (1,2,3,4,5) =15
cal=0
for i in range(1,6):
    cal+=i
print(cal)


char = "RV49CJ0AUTS172Y"
split_strings = []
n = len(char) // 3
for index in range(0, len(char), n):
    split_strings.append(char[index: index + n])
print(" ".join(split_strings))

