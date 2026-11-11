# Given two strings, check whether the second string exists inside the first string

s = "programming"
sub = "gram"
found = True

for i in range(len(s)):
    j = 0
    while j < len(sub):
        if i + j >= len(s) or s[i+j] != sub[j]:
            break
        j += 1
    if j == len(sub):
        found = True
        break

print("Found" if found else "Not Found")