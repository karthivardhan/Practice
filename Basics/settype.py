# doesn't allow duplicates, if we include then it will be omitted
s = {10,20,'Test',5,9}
s.update([99,56])
s.remove(20)
print(s)

f = frozenset(s) # doesn't allow to update and remove after this is set
f.remove('Test')
print(s)


