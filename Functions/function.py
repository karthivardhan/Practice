def persion(name, age):
    print(name, age)
persion('Karthikeya',10)

############################
def persion(name, age):
    print('name:', name, 'Age:', age)
persion(age=10, name='Karthikeya') #  Generally we should pass arguments in correct possition to parameters,
#  if not passing in correct possition then we have to pass with that keyword


#############################
def add(a, *b): # *b->Tuple
    print(a)
    print(b) # (6,9,1)
    c = a
    for i in b:
        c+=i
    print(c)
add(5,6,9,1)  # a=5, b=6,9,1. This will be useful when we want to pass multiple arguments to one parameter

# Keyword variable length argument
def persion(name, **data): # ** -> means, passing multiple arguments with the help of keywords
    print('name', name)
    for i,j in data.items(): # i, j-> for keyword and its value. items()-> is a function
        print(i,j)
persion('Karthikeya', age=10, city='Kakinada', phoneno=1234567891)