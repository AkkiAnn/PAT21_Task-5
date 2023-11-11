def remove_vowels(input_string):
# Initialize empty string to store result
    result = ""
# Iterate each character in input string
    for char in input_string:
# Check character is not a vowel 
        if char.lower() not in "aeiou":
            result += char
    return result
# Example:
input_string = "Hello, World!"
result_string = remove_vowels(input_string)
print(result_string)
