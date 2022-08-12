class ABC():
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

    def fun1(self):
        print("Name:", self.fName, self.lName)

class XYZ(ABC):
    def __init__(self, fname, lname, age):
        self.age = age
        super().__init__(fname, lname)

    def fun2(self):
        print("Age:", self.age, "Years")

obj = XYZ('Karthikeya', 'Jajimoggala',10)
obj.fun1()
obj.fun2()