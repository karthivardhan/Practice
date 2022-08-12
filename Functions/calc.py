def add(a,b):
    x = a+b
    print(x)
add(1,4)

def calc(a,b):
    x = a+b
    y = a-b
    z = a*b
    d = a/b
    return x, y, z, d
result = calc(10,20)
print(result);

def add_sub(x,y):
    a = x+y
    b = x-y
    return a,b
result1, result2 = add_sub(10,5)
print("Add:", result1, "Sub:", result2 )
