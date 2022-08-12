
class computer:
    def fun1(self):
        print("Mac book Air, 8GB Ram")

obj1 = computer()
obj1.fun1()


class Persion():
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName
    def name(self):
        print(self.fName, self.lName)

obj = Persion("Karthikeya", "Jajimoggala")
obj.name()


class Student:
    def __init__(self, m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

obj1 = Student(99,98,96)
print(obj1.avg())

############ Use the super() Function #################
class School:
    def __init__(self, fName, lName, yoj):
        self.fName = fName
        self.lName = lName
        self.yoj = yoj

class Student(School):
    def __init__(self, fName, lName, yoj):
        super().__init__(fName, lName, yoj)

    def welcome(self):
        print("Welcome", self.fName, self.lName, 'joined in year', self.yoj)

obj = Student('Karthikeya', 'Jajimoggala', 2021)
obj.welcome()

############ without super function ################

class School:
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

class Student(School):
    def __init__(self, fName, lName):
        School.__init__(self, fName, lName)

    def welcome(self):
        print("Welcome", self.fName, self.lName)

obj = Student('Karthikeya', 'Jajimoggala')
obj.welcome()
