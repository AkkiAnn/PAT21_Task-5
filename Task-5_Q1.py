# Input string
input_string = "Guvi Geeks Network Private Limited"
# Convert input string to lowercase 
input_string = input_string.lower()
# Initialize variables to store counts
total_vowels = 0
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
# Iterate each character in input string
for char in input_string:
    if char in "aeiou":
        total_vowels += 1
        if char == "a":
            count_a += 1
        elif char == "e":
            count_e += 1
        elif char == "i":
            count_i += 1
        elif char == "o":
            count_o += 1
        elif char == "u":
            count_u += 1
# Print results
print("Total number of vowels:", total_vowels)
print("Count of 'A':", count_a)
print("Count of 'E':", count_e)
print("Count of 'I':", count_i)
print("Count of 'O':", count_o)
print("Count of 'U':", count_u)
