def is_anagram(str1, str2):
# Remove spaces convert to lowercase 
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
# Check sorted characters
    return sorted(str1) == sorted(str2)
# Example:
string1 = "listen"
string2 = "silent"
result = is_anagram(string1, string2)
 # This will print True for the given example
print(result) 
