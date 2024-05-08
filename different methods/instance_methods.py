# Instance methods

class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)
    
    def grade(self):
        if self.marks >= 60:
            print("First Grade")
        elif self.marks >=50:
            print("Second Grade")
        elif self.marks>=35:
            print("Thirrde Grade")
        else:
            print("Failed")
n = int(input("Enter number of syudents: "))
for i in range(n):
    name = input("Name: ")
    marks = int(input("Marks: "))
    s = Student(name,marks)
    s.display()
    s.grade()
    print()

'''
Enter number of syudents: 2
Name: pradeep
Marks: 60
Name:  pradeep
Marks:  60
First Grade

Name: kumar
Marks: 55
Name:  kumar
Marks:  55
Second Grade
'''


# Setters and getters

class Student:
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name
    
    def setMarks(self,marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

n = input("Enter no.of students")
for i in range(n):
    s = Student()
    s.setName('pradeep')
    s.setMarks(40)

    print(s.getName())
    print(s.getMarks())
    print()


'''
Enter no.of students2
namepradeep
marks4
pradeep
4

namekumar
marks30
kumar
30

'''