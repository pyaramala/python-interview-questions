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

count_vowels_and_consonants("Hello World")