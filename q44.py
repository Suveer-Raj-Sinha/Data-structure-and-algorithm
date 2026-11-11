# Given a string, remove repeated characters while preserving their original order.

s = "programming"
new_s = ""

for i in range(len(s)):
    if s[i] not in new_s:
        new_s += s[i]

print(new_s)