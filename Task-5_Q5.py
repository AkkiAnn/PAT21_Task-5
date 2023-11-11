# function which return reverse of a string
def isPalindrome(s):
 return s == s[::-1]
s = "malayalam"
ans = isPalindrome(s)
if ans:
 print("True")
else:
 print("False")