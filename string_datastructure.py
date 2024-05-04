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