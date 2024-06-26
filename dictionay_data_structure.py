# 1.How to access data from dictionary
d = {100:'pradeep',200:'kumar',300:'yaramala'}
for key,val in d.items():
    print(f"key: {key} val: {val}")

# 2. Write a program to enter name and percentage marks in a dictionary and dispaly information on the screen
d={}
n = int(input("Enter no.of students"))  
for i in range(n):
    name = input("Enter name: ")
    percentage_marks = int(input("Enter percentage%"))
    d[name] = percentage_marks

print(d)


'''
Enter no.of students3
Enter name: pradeep
Enter percentage%90
Enter name: kumar
Enter percentage%30
Enter name: yaramala
Enter percentage%100         
{'pradeep': 90, 'kumar': 30, 'yaramala': 100}
'''

#3. update a dictionary  
d = {'pradeep': 90, 'kumar': 30, 'yaramala': 100}
d['pradeep']=100
d['nani']=10
print(d)

#4. Delete elements from dictionary
d = {'pradeep': 100, 'kumar': 30, 'yaramala': 100, 'nani': 10}
del d['nani']
print(d)

'''
{'pradeep': 100, 'kumar': 30, 'yaramala': 100} 
'''

#5. Remove all entries from dictionary
d = {'pradeep': 100, 'kumar': 30, 'yaramala': 100, 'nani': 10}
d.clear()
print(d)  #{}

# 6.Delete total dictionary
d = {'pradeep': 100, 'kumar': 30, 'yaramala': 100, 'nani': 10}
del d
print(d) #NameError

# 7. To create a dictionary
d=dict()
print(type(d))  #<class 'dict'>

#8. get the number of items in a dictionary
d = {'pradeep': 100, 'yaramala': 100, 'nani': 10} 
print(len(d))  #3

#9.To get the value associated with the key
d = {'pradeep': 100, 'yaramala': 100, 'nani': 10} 
val = d.get('pradeep',0)
val1 = d.get('teacher',0)
print(val,val1) #100 0

#10. remove the entry associated with key and returns the corresponding value
d = {'pradeep': 100, 'yaramala': 100, 'nani': 10} 
val = d.pop('pradeep')
print(val) #100

#11.Remove the arbitary item and returns value
d = {'pradeep': 100, 'yaramala': 100, 'nani': 10} 
val = d.popitem()
print(val) # ('nani', 10)

#12. Get all the keys from dictionary
d ={'pradeep': 100, 'yaramala': 100, 'nani': 10} 
print(d.keys())  #dict_keys(['pradeep', 'yaramala', 'nani'])

#13.Get values associated with dictionary
d ={'pradeep': 100, 'yaramala': 100, 'nani': 10} 
print(d.values()) #dict_values([100, 100, 10])

#14.get the list of tuples key-value pair
d ={'pradeep': 300, 'yaramala': 100, 'nani': 10} 
print(d.items()) # dict_items([('pradeep', 300), ('yaramala', 100), ('nani', 10)])

#15. To create duplicate dictionary
d ={'pradeep': 300, 'yaramala': 100, 'nani': 10} 
d1 = d.copy()
print(d1) # d ={'pradeep': 300, 'yaramala': 100, 'nani': 10} 

#16. get the value from dictionay if not create
d ={'pradeep': 300, 'yaramala': 100, 'nani': 10} 
print(d.setdefault('pradeep',10))
print(d)
print(d.setdefault('city','Vijayawada'))
print(d)

#17.Merge two dictionaries
d = {'pradeep': 300, 'yaramala': 100, 'nani': 10} 
d1 ={'city': 300, 'yaramala': 20, 'nani': 10} 

d.update(d1) 
print(d)   #{'pradeep': 300, 'yaramala': 20, 'nani': 10, 'city': 300}

#18. Take a dictionary from keyboard and print sum of values
d = eval(input("Enter Dictionary: "))
sum=sum(d.values())
print("Sum: ",sum)

#19. Find the occurence of each letter present in the given string
s = input("Enter String: ")
d = {}
for i in s:
    d[i]=d.get(i,0)+1
for key,val in d.items():
    print(f"{key} occured {val} times")


'''
Enter String: mississippi
m occured 1 times
i occured 4 times
s occured 4 times
p occured 2 times
'''

"""20. Write a progam to accept student name and marks from 
the keyboard and creates a dictionary.Also dispaly student marks by taking student name"""

n = int(input("enter number of students: "))
d = {}
for i in range(n):
    name = input("Name: ")
    marks= int(input("Marks: "))
    d[name] = marks
while True:
    name = input("Enter name: ")
    marks = d.get(name,-1)
    if marks == -1:
        print("Not found")
    else:
        print("Marks: ",marks)
    option = input("Do you want to find another student[YES|NO]")
    if option.upper()=='NO':
        break
# 21 Dictionary comprehension
squares = {x:x*x for x in range(10)}
print(squares)
doubles = {x:x**3 for x in range(10)}
print(doubles)

'''
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
'''