x = 123 # Global variable can be accessed anywhere
def display():
    y = 456 # local variable, can be accessed within the function
    print(y)
print(x)
display()

### accessing global variable with same name #####
x = 123
def display():
    x = 456
    print(x)
    print(globals()['x'])
print(x)
display()

a = 10
def display():
    a = 15
    print('inside function', a)
display()
print('outside function', a)

################################
a = 10
def display():
    a = 15
    print('inside function', a)
    globals()['a'] = 20
display()
print('outside function', a)

## assign function to a variable ##
x = 123
def display():
    print(x)
z = display
z()
z()
