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