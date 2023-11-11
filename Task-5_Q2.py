# Number of rows in pyramid
num_rows = 5
# Initialize starting number
start_number = 1
# Loop to print the pyramid
for i in range(1, num_rows + 1):
# Print leading spaces
    for j in range(num_rows - i):
        print("  ", end="")
# Print numbers in increasing order
    for j in range(1, i + 2):
        print(start_number, end=" ")
        start_number += 1
# Move to next line after completing a row
    print()
