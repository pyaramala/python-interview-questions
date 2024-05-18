# Demo program

class Animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print(f"{name} walk with legs {cls.legs}")


Animal.walk('Dog')
Animal.walk("Cat")

# Program to track number of objects created for a class

class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count+1

    @classmethod
    def noofobjects(cls):
        print("Number of objects created: ",cls.count)

t1 = Test()
t2 = Test()
Test.noofobjects()
t3 = Test()
t4 = Test()
Test.noofobjects()


'''
Dog walk with legs 4
Cat walk with legs 4
Number of objects created:  2
Number of objects created:  4
'''
