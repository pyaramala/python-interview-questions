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


