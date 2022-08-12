lst = [10,20,30,40,50]
print(type(lst)) #int class
b = bytes(lst) # bytes cannot be assigned new values via index
print(type(b))

b1 = bytearray(lst) # bytearray can be assigned new values through index
b1[2]=5
print(type(b1))
