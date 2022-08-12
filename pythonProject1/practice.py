str = "Hello"
print(len(str))
print(str[::-1])
print(str.upper())
print(str.lower())
print(str[0:2])


strSpecial = 'abc$#efghi&&^%jk'
liststr = list(strSpecial)
i=0
j=len(liststr)-1
while i<j:
    if not liststr[i].isalpha():
        i+=1
    elif not liststr[j].isalpha():
        j-=1
    else:
        liststr[i], liststr[j] = liststr[j], liststr[i]
        i+=1
        j-=1
strOut = ''.join(liststr)
print(strOut)

## Reverse words##
string = "How are you"
words = string.split()[::-1]
print(' '.join(words))

string = "How are you"
words = string.split()
r = list(reversed(words))
print(' '.join(r))

#### Upper case - half ####
string1 = "somestring"
sl= len(string1)
lowerString=string1.lower()
print(lowerString)
upperString=string1.upper()
print(upperString)
cutlen=sl-(sl//2)
prtstr=lowerString[:cutlen]+upperString[cutlen:]
print(prtstr)

#### print vowels ####
sentence = input("Enter a sentence: ")
for letter in sentence:
    if letter in 'aeiouAEIOU':
        print(letter, end=' ')

def fun(sentence1):
    for letter in sentence1:
        if letter in "aeiouAEIOU":
            lst = list(letter)
            print(lst, end=' ')

sentence1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
fun(sentence1)

s1 = "Hello"
s2 = "How are you"
print(s1,''+ s2)


def fun1(s1,s2):
    print(s1,''+s2)
fun1('Hello', 'How are you')
