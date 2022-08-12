class MyClass():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun1(self):
        print("My name is", self.name, "and age", self.age, "Years")

obj = MyClass('Karthikeya', 10)
obj.fun1()