class A:
    def __init__(self):
        print('i am a')
class B(A):
    def __init__(self):
        print('i am b') 

class C(B):
    def __init__(self):
        print('i am c')
class E:
    def __init__(self):
        print('i am c')

class D(A,E):
    def __init__(self):
        print('i am d')

a=A()
b=B()
c=C()
d=D()       