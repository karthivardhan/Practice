# An array is defined as a collection of items that are stored at contiguous memory locations.


array = ['Blue', 'White', 'Red']
a = array[1]
print(a)
print(len(array))
a = array[0]
a = array.index('White')
a = array.insert(1, 'Orange')
a = array.reverse()
print(a)
array.append('Brown')
array.append('Black')

print(array)
array.pop(4) # remove an
array.remove('Red') # remove

print(array)
array.clear()
print(array)

