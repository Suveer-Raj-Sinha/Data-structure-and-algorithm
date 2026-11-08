# Given a list of words, find the longest word.

words = ["apple", "banana", "watermelon", "kiwi", "pineapple"]
largest = ""
count = 0

for i in words:
    string = i
    lCount = 0
    for j in range(len(string)):
        lCount += 1
    if lCount > count:
        count = lCount
        largest = i

# for i in words:
#     if len(i) > len(largest):
#         largest = i

print(largest)