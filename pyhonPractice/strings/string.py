from os import replace

str = "Hello"
print(str)
l = len(str)
print(l)
list1 = list(str)
print(list1)
lower = str.lower()
upper = str.upper()

reverse = str[::-1]
re =''.join(reversed(str))

print(lower, upper, reverse, re)

str2 = "how are you"
strc = (str + ' ' + str2)
print(strc)

c = str2.capitalize() # 'How are you'
s = str2.split() # ['how', 'are', 'you']
print(s)

str3 = ['Hello', 'how are you']
jo = ' '.join(str3)
print(jo) # Hello how are you

i = str[0]
print(i)

count = str.count('o') # number of occurrences
print(count)

# f-string
fs = f'{str}{str2}'
print(fs)

# Interpolate a variable into a string using format()
difficulity = 'easy'
thing = 'exam'
pr = 'This {} was so {}'.format(thing, difficulity)
print(pr) # This exam was so easy

num1 = '1000'
num2 = '1.0'
numeric1 = num1.isnumeric()
numeric2 = num2.isnumeric()
print(numeric1) # True
print(numeric2) # False

print('aPPLE'[0].islower()) # True
print('aPPLE'[0].isupper()) # False

# Capitalize the first character of each word in a string
new = "hello how are you"
prn = new.title()
#prn = new[0].upper() + new[1:5] + new[6].upper() + new[7:9] + new[10].upper() + new[11:13] + new[14].upper() + new[15:17]
print(prn)


# Replace instances of a substring in a string
str5 = 'Hello, How are you'
print(str5.replace('How', 'how')) # Hello, how are you

str6 = 'abc123'
print(str6.isalnum()) # True

print(str5.startswith('Hello'), str5.endswith('you')) # True True

print(str5.isspace()) # False -> white space between all the char

print(str * 3) # prints 3 times

#partition() function - Coupa Interview question
str10 = 'deabf'
spl = str10.partition('ab')
print(spl)
print(len(spl))
ji = ''.join(spl[1]+spl[0]+spl[2])
print(ji)

# Remove vowels from a string
string = "Hellohowareyou"
vowels = 'aeiou'
#vowels = ('a', 'e', 'i', 'o', 'u')

for i in string:
    if i not in vowels:
        print(i)

str11 = " hello hai"
print(str11.rstrip())
print(str11.split())
print(list(str11))
ab = print(str11.partition('ll'))

half = int(len(str)/2)
print(half)


# Python program to print even length words
str12 = "This is a Python program"
s = str12.split()
for words in s:
    if len(words) % 2 ==0:
        print(words)

# Uppercase Half String
hu = "abcdefghijkl"
half = len(hu) // 2
print(half)

res = ''.join(hu[:half] + hu[half:].upper())
print(res)
res1 = ''.join(hu[0:6].upper() + hu[6:12])
print(res1)

# upper case First and last letters
hu1 = 'abcdefghiklmnopqr'
res3 = ''.join(hu1[0].upper() + hu1[1:-1]) + hu1[-1:].upper()
print(res3)


# Print common letter in both the strings
s1 = 'abcdefghijks'
s2 = 'abdefklmniks'

for i in s1:
    if i in s2:
        print(i)


# Max
def repa(rep1):
    rep1 = rep1.replace(',', '.')
    #rep1 = rep2.replace('.', ',', ' ')
    return rep1

repc1 = "129.123,10.12,1"
print(repa(repc1))

# Convert numeric words to numbers

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',

}
test = "one two five four six"
res = ''.join(help_dict[ele] for ele in test.split())

print(res)



string = "how are you"
spt = string.split()
first_letter = spt[0].title() + ' ' +spt[1].title() + ' ' +spt[2].title()
print(first_letter)

last_letter =''.join(first_letter[0:2] + first_letter[2].upper() + first_letter[3:6] +
                     first_letter[6].upper() + first_letter[7:10] + first_letter[10].upper())

print(last_letter)

# Capitalize first and last letters of each word

string = "how are you"
string = string.title()
result = ""
for word in string.split():
    result += word[:-1] + word[-1].upper() + " "
print(result)
