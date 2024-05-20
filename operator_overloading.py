# Demo program to use + operator for our class objects

class Book:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,other):
        return self.pages+other.pages

b1 = Book(10)
b2 = Book(20)

print(b1+b2)


# Overloading > and <= operator for student class objects

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __gt__(self,other):
        return self.marks>other.marks
    
    def __lt__(self,other):
        return self.marks<other.marks
    
s1 = Student('pradeep',10)
s2 = Student('kumar',20)
print(s1<s2)


# Program to overload multiplication operator to work on employee objects

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __mul__(self,other):
        return self.salary*other.days
    
class Timesheet:
    def __init__(self,name,days):
        self.name = name
        self.days = days

e = Employee('pradeep',100)
t = Timesheet('pradeep',30)
print(e*t)