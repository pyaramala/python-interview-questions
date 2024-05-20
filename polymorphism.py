# Duck typing philosophy of python

class Duck:
    def bark(self):
        print("Quack.....Quack")

class Dog:
    def talk(self):
        print("Bow...Bow")

class Cat:
    def talk(self):
        print("Meow...Meow")

class Goat:
    def talk(self):
        print("Myaah Myaah...")

def f1(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    if hasattr(obj,'bark'):
        obj.bark()

l= [Duck(),Cat(),Goat()]
for obj in l:
    f1(obj)