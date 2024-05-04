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
     



