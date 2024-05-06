#1.Generators

def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

g = mygen()
print(g)

#2. Countdown

# countdown

def countdown(num):
    print("Start countdown: ")
    while num>0:
        yield num
        num -=1

values = countdown(5)
for x in values:
    print(x)

'''
Start countdown: 
5
4
3
2
1

'''

#3. To generate first n numbers

def firstn(num):
    n=1
    while num>=n:
        yield n
        n +=1
        
values = firstn(10)
for x in values:
    print(x)

'''
1
2
3
4
5
6
7
8
9
10
'''    

#4. Fibonacci numbers

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
    
for f in fib():
    if f>100:
        break
    print(f,end='  ')    # 0  1  1  2  3  5  8  13  21  34  55  89

#5. Generators vs Normal functions wrt Memory utilization
#Normal funcrion
l = [x*x for x in range(1000000000000000000000)]
print(l[0])  #Memory error

#Generator function
l = (x*x for x in range(100000000000000000000000))
print(type(l))
print(next(l))
print(next(l)) 

'''
<class 'generator'>
0
1
'''

# Generators vs normal collections wrt Memory Utilization
import random
import time
names = ['pradeep','kumar','nani','siva']
subject = ['python','java','scala','c++']
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id':i,
            'name':random.choice(names),
            'subject':random.choice(subject)
        }
        result.append(person)
    return result
t1 = time.time()
peoples=people_list(1000000)

t2 = time.time()
print(f"Took: {t2-t1}")

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id':i,
            'name': random.choice(names),
            'subject': random.choice(subject)
        }
        yield person
t1 =time.time()
peoples = people_generator(1000000)

t2 = time.time()
print(f"Took: {t2-t1}")

'''
Took: 7.866150856018066
Took: 0.20787310600280762
'''

