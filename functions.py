#1. write a function to take name of the student as input and print wish message by name
def wish(name):
    print("Hello",name)

wish("pradeep")
wish("yaramala")

'''
Hello pradeep
Hello yaramala
'''
#2. write a function to take number as input and print its square value

def square(num):
    return num*num
square(2) #4
square(4) #16

#3. Write a function to accept two numbers as input and return sum
def add(x,y):
    return x+y
add(2,3) #5

#4. Write a function to check whether given number is even or odd
def even_odd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
even_odd(10) #Even
even_odd(15) #odd

# 5.write a function to find factorial of given number
def fact(num):
    result = 1
    for i in range(1,num+1):
        result = result*i
    print(f"Factorial of {num}! is: {result}")
fact(5)  # Factorial of 5! is: 120

# 6. write a function to return multiple values

def sum_sub(a,b):
    sum = a+b
    sub = a-b
    return sum,sub

sum,sub=sum_sub(100,50)
print("Sum: ",sum)
print("Sub: ",sub)

'''
Sum:  150
Sub:  50
'''

# 7. caliculate
def calc(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div

sum,sub,mul,div = calc(100,50)
print(f"sum: {sum} sub: {sub} mul: {mul} div: {div}")

#8. write a python function to find factorial of given number with recursion
def factorial(num):
    if num == 0:
        return 1
    else:
        fact = 1
        fact = num*factorial(num-1)
    return fact
    
print(factorial(5)) #120

#9. Write a program to create a lambda function to find square of a given number
sqr = lambda x:x*x
print(sqr(5)) #25

#10. Lambda function to find sum of two given numbers
sum = lambda a,b:a+b
print(sum(10,20)) #30

#11. Lambda function to find biggest of given values

big = lambda a,b,c,d:max(a,b,c,d)
print(big(1,2,3,4))