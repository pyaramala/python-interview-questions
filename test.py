class Test:
    def __init__(self):
        self.a =10
    def m1(self):
        self.b = 20
    
t = Test()
t.m1()
t.c  = 30
print(t.__dict__)