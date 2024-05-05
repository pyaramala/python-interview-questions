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

