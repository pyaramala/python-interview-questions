class  Test:

    def m1(self):
        print("No argument method")
    def m1(self,a):
        print(a)
    def m1(self,a,b):
        print(a,b)

t1=Test()
t1.m1(10,20)


# How to handle overload methods requirements in python

class Test:
    def sum(self,a=None,b=None,c=None):
        if a !=None and b != None and c!= None:
            print(a+b+c)
        elif a!=None and b !=None:
            print(a+b)
        else:
            print("provide 2 arguments")

Test().sum(10,20,30)


# Demo program with variable number of arguments

class Test:
    def sum(self, *a):
        total = 0
        for x in a:
            total = total+x
        print("Sum= ",total)


Test().sum(10)


# Constructor overloading

class Test:
    def __init__(self):
        print("No arg constructor")

    def __init__(self,a):
        print(a)

    def __init__(self,a,b):
        print(a,b)


Test(10,20)


# constructor with default arguments

class Test:
    def __init__(self,a=None,b=None,c=None):
        print("constructor")

t1 = Test()
t2 = Test(10,10,101)


# Constructor with varibale number of arguments

class Test:
    def __init__(self,*a):
        print("Hi")

Test()
Test(19)
Test(1,2,3)