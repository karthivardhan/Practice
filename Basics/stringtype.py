str = " you are awasome!! "
print(str)

strMultiline = '''test1
test2
test3'''
print(strMultiline)

print(str[2])
print(len(str))

# Slicing a string
print(str[0:5]) # you a

print(str[0:]) # print entire from 0
print(str[:9]) # print upto 9

print(str[-3]) # from last
print (str[0:9:2]) # print alternative
print(str[::-1]) # Reverse

# strip the spaces - remove white spaces
print(str.strip())
print(str.lstrip())
print(str.rstrip())
print(str.rsplit())

print(str.count("a")) # count number of occurrences
print(str.replace("awasome", "Super")) # replace string

print(str.upper())
print(str.lower())
print(str.title())