# Given a string, count the number of vowels and consonants.

s = "programming"
vowel = 0
consonant = 0

for i in s.lower():
    if i in "aeiou":
        vowel +=1
    elif s.isalpha():
        consonant += 1

print(f"Vowel : {vowel}\nConsonant : {consonant}")