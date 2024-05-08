class Student:
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name
    
    def setMarks(self,marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

n = int(input("Enter no.of students"))
for i in range(n):
    s = Student()
    s.setName(input("name"))
    s.setMarks(input("marks"))

    print(s.getName())
    print(s.getMarks())
    print()