# Check Whether Two Strings Are Anagrams - Two strings are anagrams if they contain exactly the same characters with the same frequencies, but in a different order.

s1 = "listen"
s2 = "silent"
Anagram = True

if len(s1) != len(s2):
    print("Not Anagram")
else:
    for i in s1:
        if i not in s2:
            Anagram = False
        else:
            Anagram = True

print("Anagram" if Anagram else "Not Anagram")