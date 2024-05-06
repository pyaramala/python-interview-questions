# Decorator example
def decor(func):
    def inner(name):
        if name == "pradeep":
            print("Hello pradeep ")
        else:
            func(name)
    return inner

@decor
def wish(name):
    print("Welcome",name)

wish("nani") # elcome nani
wish("pradeep") # Hello pradeep

# 2.How to call the function with decorator and without decorator

def decor(func):
    def inner(name):
        if name=='pradeep':
            print("Hello Boss!")
        else:
            func(name)
    return inner

def wish(name):
    print("welcome",name) # welcome pradeep

wish('pradeep')
decorfunction = decor(wish)
decorfunction('pradeep')  #welcome pradeep
                         # Hello Boss!

# 3. decorator for division

def smart_division(func):
    def inner(a,b):
        print("We are dividing",a,"with",b)
        if b == 0:
            print("oops...cant devide") 
            return
        else:
            return func(a,b)
    return inner

@smart_division
def division(a,b):
    return a/b

print(division(20,2))

'''
We are dividing 20 with 0
oops...cant devide       
None
We are dividing 20 with 2
10.0
'''

#4. Decorator chaining concept

def decor(func):
    def inner():
        x=func()
        return x*x
    return inner
@decor
def num():
    return 10

num()



#5. Demo program decorator chaining
def decor(func):
    def inner(name):
        print("Decorator first (decor) executing")
        func(name)
    return inner
def decor1(func):
    def inner(name):
        print("Decorator second function(decor1)")
        func(name)
    return inner
@decor1
@decor
def wish(name):
    print("Hello",name,"Good Morning")

wish("Pradeep")


# 6. Program to filter only even numbers from the list by using filter() function?

l = [0,5,15,20,25,30]
l1 = list(filter(lambda x:x%2==0,l))
print(l1)