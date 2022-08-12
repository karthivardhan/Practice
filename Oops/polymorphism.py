class A:

    def __init__(self):
        print("init A")
    def fun1(self):
        print("Function1 is working")
    def fun2(self):
        print("Function2 is working")

class B(A):

    def __init__(self):
        print("init B")
    def fun3(self):
        print("Function3 is working")
    def fun4(self):
        print("Function4 is working")
class C(B):

    def __init__(self):
        print("init C")
    def fun5(self):
        print("Function5 is working")

obj3 = C()


class A:
    def __init__(self):
        super().__init__()
        print('init A')
    def f1(self):
        print('Test1')

class B(A):
    def __init__(self):
        super().__init__()
        print('init B')
    def f2(self):
        print('Test2')

class C(A,B):
    def __init__(self):
        print('init C')
    def f3(self):
        print('Test3')

obj = C()