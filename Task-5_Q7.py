def frequent_character(input_string):
# Initialize dictionary to store character freq
    char_frequency = {}
# Iterate character 
    for char in input_string:
# Consider alphabetic 
        if char.isalpha():  
            char = char.lower()  
# Convert lowercase 
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
# Find character maximum freq
    frequent_char = max(char_frequency, key=char_frequency.get)
    return frequent_char
# Example:
input_string = "Hello, World!"
result = frequent_character(input_string)
print("Most frequent character:", result)
