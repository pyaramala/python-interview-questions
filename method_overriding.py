# Demo program for method overriding

class P:
    def property(self):
        print("Gold+cash+car")
    def marry(self):
        print("Appalamma")

class C(P):
    def marry(self):
        super().marry()
        print("Katrina kaif")

obj = C()
obj.marry()



# Constructor overriding

class P:
    def __init__(self):
        print("Parent")

class C(P):
    def __init__(self):
        print("Child")

obj = C()


# Call Parent class constructor by using super()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self,name,age,eno,sal):
        super().__init__(name,age)
        self.eno = eno
        self.sal = sal

    def display(self):
        print(self.name)
        print(self.age)
        print(self.eno)
        print(self.sal)

e1 = Employee('pradeep',30,11,100)
e1.display()
