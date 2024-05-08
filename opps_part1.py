# Example class

class Student:
    """ Developed by pradeep kumar"""
    def __init__(self):
        self.name = 'pradeep'
        self.age = 40
        self.marks = 80
    def talk(self):
        print("Hello my name is: ",self.name)
        print("Age: ",self.age)
        print("marks: ",self.marks)
obj = Student()
obj.talk()

# Write a python program to create a student class and creates an object to it.
# call the method talk() to dispaly student details

class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def talk(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Marks: ",self.marks)
    
obj = Student('pradeep',30,80)
obj.talk()

'''
Name:  pradeep
Age:  30
Marks:  80
'''

# Program to demonestarte constructor will execute only once per object
class Test:
    def __init__(self):
        print("Constructor executing")
    def talk(self):
        print("Method executing")

obj=Test()
obj1 = Test()
obj2 = Test()
obj1.talk()

'''
Constructor executing
Constructor executing
Constructor executing
Method executing
'''


# Program to create student class

class Student:
    """ This is a student class with required data"""
    def __init__(self,x,y,z):
        self.name = x
        self.rollno = y
        self.marks = z
    def dispaly(self):
        print(f"Name: {self.name} Rollno: {self.rollno} marks: {self.marks}")

obj1 = Student("kumar",101,80)
obj1.dispaly()


#Instance variables inside the constructor by using self variable

class Employee:
    def __init__(self):
        self.eno = 100
        self.ename = 'Durga'
        self.esal = 10000
e = Employee()
print(e.__dict__)

#Instance variable inside instance method by using self variable

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
    def m1(self):
        self.c = 30

t = Test()
t.m1()
print(t.__dict__)


# Instance variable ,outside of the class by using object reference variable
class Test:
    def __init__(self):
        self.a =10
    def m1(self):
        self.b = 20
    
t = Test()
t.m1()
t.c  = 30
print(t.__dict__)  # {'a': 10, 'b': 20, 'c': 30}

# How to access instance variables 

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def dispaly(self):
        print(self.a)
        print(self.b)

t = Test()
print(t.a)
print(t.b)


# How to delete instance variables from the object

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d =40
    
    def del_d(self):
        del self.d
    
t = Test()
del t.del_d()
del t.c
print(t.__dict__)

'''
{'a': 10, 'b': 20}
'''


#The instnace variables which are deleted from one object ,will not be deleted from other objects

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
    
t1 = Test()
del t1.a
t1.b =99999
t2 = Test()
del t2.c
print(t1.__dict__)
print(t2.__dict__)

'''
{'b': 99999, 'c': 30}
{'a': 10, 'b': 20}
'''

#Static variables

class Test:
    x = 10

    def __init__(self):
        self.y = 20

t1 = Test()
t2 = Test()
print("t1: ",t1.x,t2.y)
print("t2: ",t1.x,t2.y)
t1.x =999999
print("t1: ",t1.x,t2.y)
print("t2: ",t1.x,t2.y)


'''
t1:  10 20
t2:  10 20    
t1:  999999 20
t2:  999999 20

'''

# Various places to declate static variables

class Test:
    a = 10
    def __init__(self):
        Test.b = 20
    def m1(self):
        Test.c = 30
    @classmethod
    def m2(cls):
        cls.d = 40
        Test.d2 = 50
    @staticmethod
    def m3():
        Test.e = 60

#print(Test.__dict__)
t = Test()
t.m1()
t.m2()
t.m3()
print(Test.__dict__)  

'''
{'__module__': '__main__', 'a': 10, '__init__': 
<function Test.__init__ at 0x000001BF60F79940>, 
'm1': <function Test.m1 at 0x000001BF60F799E0>, 
'm2': <classmethod(<function Test.m2 at 0x000001BF60F79A80>)>, 
'm3': <staticmethod(<function Test.m3 at 0x000001BF60F79B20>)>, 
'__dict__': <attribute '__dict__' of 'Test' objects>, 
'__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': 
None, 'b': 20, 'c': 30, 'd': 40, 'd2': 50, 'e': 60}
'''

# access instance variables

class Test:
    a = 10
    def __init__(self):
        print(self.a)
        print(Test.a)
    def m1(self):
        print(self.a)
        print(Test.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)
    @staticmethod
    def m3():
        print(Test.a)

t = Test()
print(Test.a)
print(t.a)
t.m1()
t.m2()
t.m3()

'''
10
10
10
10
10
10
10
10
10
'''
# Where we can modify the value of static variables

class Test:
    a = 777
    @classmethod
    def m1(cls):
        cls.a = 999
    @staticmethod
    def m2():
        Test.a =5555

print(Test.a)
t = Test()
t.m1()
print(t.a)
t.m2()
print(t.a)

'''
777
999
5555
'''

# If we change the value of the static variable by using either self or object reference variable

class Test:
    a = 10
    def m1(self):
        self.a = 8888

print(Test.a)
t = Test()
t.m1()
print(Test.a)
Test.a =30
print(Test.a)

'''
10
10
30
'''

class Test:
    x = 10
    def __init__(self):
        self.y =20

t1 = Test()
t2 = Test()
print(t1.x,t2.y)
print(t2.x,t2.y)
t1.x = 9999
t2.y =0999
print(t1.x,t2.y)
print(t2.x,t2.y)

'''
10 20
10 20
9999 8888
10 20
PS C:\Us
'''


class Test:
    a = 10
    def __init__(self):
        self.y = 20

t1 = Test()
t2 = Test()
Test.a = 100
print(t1.a,t1.y)
print(t2.a,t2.y)

'''
100 20
100 20
'''


class Test:
    a = 10
    def __init__(self):
        self.b =20

    def m1(self):
        self.a =888
        self.b = 999

t1 = Test()
t2 = Test()
#t1.m1()
print(t1.a,t1.b)
print(t2.a,t2.b)

'''
888 999
10 20
'''

class Test:
    a = 10
    def __init__(self):
        self.b = 20
    @classmethod
    def m1(cls):
        cls.a =200
        cls.b = 300

t = Test()
t1 = Test()
t.m1()
print(t.a,t.b)
print(t1.a,t1.b)
print(t1.a,Test.b)

'''
200 20
200 20
200 300

'''

