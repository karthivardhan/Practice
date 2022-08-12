## Single, Multilevel Inheritance

class A:
    def fun1(self):
        print("Function1 is working")
    def fun2(self):
        print("Function2 is working")

class B(A):
    def fun3(self):
        print("Function3 is working")
    def fun4(self):
        print("Function4 is working")
class C(B):
    def fun5(self):
        print("Function5 is working")

obj1 = A()
obj1.fun1()
obj1.fun2()

obj2 = B()
obj2.fun1()
obj2.fun2()
obj2.fun3()
obj2.fun4()

obj3 = C()
obj3.fun1()
obj3.fun2()
obj3.fun3()
obj3.fun4()
obj3.fun5()

########### Multiple #########################

class A:
    def fun1(self):
        print("Function1 is working")
    def fun2(self):
        print("Function2 is working")

class B():
    def fun3(self):
        print("Function3 is working")
    def fun4(self):
        print("Function4 is working")
class C(A,B):
    def fun5(self):
        print("Function5 is working")

obj1 = A()
obj1.fun1()
obj1.fun2()

obj2 = B()
obj2.fun3()
obj2.fun4()

obj3 = C()
obj3.fun1()
obj3.fun2()
obj3.fun3()
obj3.fun4()
obj3.fun5()


