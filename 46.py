# Given a list of strings, find the longest prefix shared by all strings.

words = ["flower", "flow", "flight"]
prefix = ""

for i in range(len(words[0])):
    match = True

    for word in words:
        if i >= len(word) or word[i] != words[0][i]:
            match = False
            break

    if match:
        prefix += words[0][i]
    else:
        break

print(prefix)