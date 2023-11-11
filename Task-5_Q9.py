def count_words(input_string):
# Split input string into words using whitespace 
    words = input_string.split()
# Return number of words in list
    return len(words)
# Example:
input_string = "PAT twenty one Task five"
result = count_words(input_string)
print("Number of words:", result)

