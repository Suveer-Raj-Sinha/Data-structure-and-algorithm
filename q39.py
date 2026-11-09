# Given a string, find the first character that appears exactly once.

s = "aabbcdeff"
i = 0

for i in range(len(s)):
    num = True
    for j in range(len(s)):
        if i == j:
            continue
        elif s[i] == s[j]:
            num = False
            break
    if num:
        print(s[i])
        break