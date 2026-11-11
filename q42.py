# Given a string, count the number of vowels and consonants.

s = "programming"
vowel = 0
consonant = 0

for i in s:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel +=1
    else:
        consonant += 1

print(f"Vowel : {vowel}\nConsonant : {consonant}")