#Check Whether a String Is a Palindrome - Given a string, check whether it reads the same forward and backward.

s = "madam"
left = 0
right = len(s)- 1
is_palindrome = True

while right > left:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left +=  1
    right -= 1

print("Palindrome" if is_palindrome else "Not Palindrome")