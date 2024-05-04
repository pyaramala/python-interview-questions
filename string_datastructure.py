#1. Check if a string is a palindrome
s = input("Enter String: ")
if s == s[::-1]:
    print(" Palindrome")
else:
    print("No it is not palindrome")

'''
Enter String: malayalam
Palindrome
'''

# 2. Reverse a string
s = input("Enter string")
print("Reverse: ",s[::-1])

'''
Enter string pradeep
Reverse:  peedarp
'''

# 3.Count the occurrence of a character in a string

s = input("Enter String: ")
char = input("Enter character to count: ")
count = s.count(char)
print("Count",count)


'''
Enter String: welcome
Enter character to count: e
Count 2
'''

# 4. check if two strings are anagrams

def are_anagrams(str1,str2):
    str1 = str1.lower().replace(" ","")
    str2 = str2.lower().replace(" ","")
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
    

print(are_anagrams("silent","listen")) #True
print(are_anagrams("hello","world"))   #False
print(are_anagrams("school master","The classrom")) #True
     

# 5.Remove duplicate characters from a string

s = input("Enter String: ")
result = '' 
for char in s:
    if char not in result:
        result+=char

print(result) #

'''
Enter String: hello world
helo wrd
'''

# 6. Find the first non-repeating character in a string

s = input("Enter String")
char_count_dict = {}
for char in s:
    char_count_dict[char]=char_count_dict.get(char,0)+1
for char in s:
    if char_count_dict[char]==1:
        print(char)
        break

'''
Enter String pradeep
r
'''


# 7. Check if a string contain only digits

s = input("Enter String: ")
if s.isdigit():
    print("String contain only digits")
else:
    print("NO")


'''
Enter String: 1234
String contain only digits
PS C:\Users\new\python_interview_questions\python-interview-questions> python test.py
Enter String: p123
NO
'''

# 8. Check if a string contains onlyy alphanumeric characters

s = input("Enter String: ")
if s.isalnum():
    print("YES")
else:
    print("No")

''' 
PS C:\Users\new\python_interview_questions\python-interview-questions> python test.py
Enter String: abc123
YES
PS C:\Users\new\python_interview_questions\python-interview-questions> python test.py
Enter String: 123
YES
PS C:\Users\new\python_interview_questions\python-interview-questions> python test.py
Enter String: 123!
No
PS C:\Users\new\python_interview_questions\python-interview-questions> 

'''

# 9.Remove all white spaces from a string