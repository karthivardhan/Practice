# if the variable value is same then the value will be stored in same memory location
# Works same for all data types number, string, boolean and etc

a = 10
b = 10
print(id(a))
print(id(b))
print(a is b)

x = "abc"
y = "xyz"
print(id(x))
print(id(y))
print(x is y)

a = True
b = True
print(id(a))
print(id(b))
print(a is b)

