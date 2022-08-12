def fun1(fName, lName, age):
    print("Name:", fName, lName, "\nAge:", age)

fun1('Karthikeya', 'Jajimoggala', 10)

# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
def fun2(food):
    for x in food:
        print(x)
items = ['Rice', 'Chicken', 'Icecream']
fun2(items)

