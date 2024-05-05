# 13. Find all substrngs of a string
s = 'abcd'
sub_string_list = []
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub_string_list.append(s[i:j])
print(sub_string_list)

'''
['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
'''

# 14. Check if a string is a rotation of another string

def is_rotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    concatenated_string = s1+s1

    if s2 in concatenated_string:
        return True
    else:
        return False
    
s1 = "waterbottle"
s2 = "erbottlewat"
print(is_rotation(s1,s2))

s1 = "hello"
s2 = "world"
print(is_rotation(s1,s2))

'''
waterbottlewaterbottle
True
hellohello
False
'''

# 15. Count the number of vowels and consonents in a string

def count_vowels_and_consonants(input_string):
    vowels = set("aeiouAEIOU")
    vowels_count = 0
    consonent_count = 0
    for char in input_string:
        if char in vowels:
            vowels_count+=1
        elif char.isalpha():
            consonent_count += 1
    print(vowels_count,consonent_count)

count_vowels_and_consonants("Hello World")  #3 7


# 16. Check if a string contains palindrome substring of length greater than or equal to k

s = input("Enter String: ")
n = len(s)
k=4
sub_string_list = []
for i in range(len(s)):
    for j in range(i+1,n+1):
        sub_string_list.append(s[i:j])
new_list = [substr for substr in sub_string_list if len(substr)==k and substr==substr[::-1]]
print(new_list)

'''
Enter String: abccba
['bccb']
'''

# 17.Find the first repeated character in a string

s = input("Enter String: ")
word_count_dict = {}
for char in s:
    if char  in word_count_dict:
        print(char)
        break
    else:
        word_count_dict[char]=1

'''
Enter String: abcdefghija
a
'''

# 18.Find the index of the first occurence of substring in a string
s = input("Enter Main string: ")
sub_s = input("Enter sub string: ")
print(s.find(sub_s))

'''
Enter Main string: hello world
Enter sub string: world
6
'''

#19.check if a string is valid palindrome after removing k characters
 
# 20.Replace all occurence of a substring in a string with another substring

s = input("Enter Main string: ")
sub_string = input("Sub string: ")
new_substring = input("New substring: ")
result = s.replace(sub_string,new_substring)
print(result)

'''
Enter Main string: Hello World
Sub string: Hello
New substring: Python
Python World

'''

