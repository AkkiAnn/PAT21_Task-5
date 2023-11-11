def unq_characters(input_string):
 # set to store unique characters
    uniq_chars = set()
 # Iterate character in input string
    for char in input_string:
 # Add character to set
        uniq_chars.add(char)    
# Return number of unique characters
    return len(uniq_chars)
# Example:
input_string = "hello, world!"
result = unq_characters(input_string)
# This will print 10 for given example ("hello, world!")
print(result)  

