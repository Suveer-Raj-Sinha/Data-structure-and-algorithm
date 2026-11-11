# Given a string, find the character that appears most frequently.

s = "programming"
max = s[0]
count = 0

for i in range(len(s)):
    sub_count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            sub_count += 1
    if sub_count > count:
        count = sub_count
        max = s[i]

print(max)