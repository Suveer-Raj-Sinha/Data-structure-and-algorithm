# Given a string, reverse it without using slicing ([::-1]) or built-in reverse functions.

s = "programming"
chars = list(s)
j = len(chars)-1

for i in range(len(chars)):
    if i < j:
        chars[i], chars[j] = chars[j], chars[i]
        j -= 1

s = "".join(chars)
print(s)