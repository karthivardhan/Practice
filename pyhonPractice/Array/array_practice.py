# Arrays are a collection of similar data items stored at contiguous memory locations

arr1 = ['Orange', 'Apple', 'Banana']
arr1.pop()
print(arr1)
for x in arr1:
    print(x)
print(arr1[1])
print(arr1[0:2])
arr1.append("Grapes")
print(arr1.insert(2, 'Peach'))
arr1.append('Apple')
i = arr1[1]
print('Index:', i)
print(arr1.index('Banana'))
print(arr1.insert(3, 'CustodApple'))
arr1.remove('Orange')
print(arr1)
arr1.reverse()
print(arr1)
a=len(arr1)
print(a)
arr1.sort()
print(arr1)
arr1.pop(1)
print(arr1)
print(arr1.clear())
print(arr1.copy())





