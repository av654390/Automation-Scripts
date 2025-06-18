import pandas as pd

# Read the HTML file
f = pd.read_html("dumps.html", header=1)[0]

# Get the number of rows (dumps)
dumps = len(f.index)
print(dumps)

# Initialize a list to store extracted numbers
extracted_numbers = []

# Print the column names for debugging
print("Columns in DataFrame:", f.columns)

# Check for 'Runtime Errors Number' column and clean it
if 'Runtime\xa0Errors Number' in f.columns:
    for i in f['Runtime\xa0Errors Number']:
        j = str(i).split()
        print("Split result:", j)  # Debugging output
        if j and j[-1].isdigit():
            extracted_numbers.append(int(j[-1]))  # Append only integers
else:
    print("Column 'Runtime Errors Number' not found.")

# Ensure that all items in list 'extracted_numbers' are integers
# Debug output for extracted numbers
print("Extracted Numbers before summing:", extracted_numbers)

# Sum the numbers in the list
total_sum = sum(extracted_numbers)

# Print the extracted numbers and their sum
print("Extracted Numbers:", extracted_numbers)
print("Sum of Numbers:", total_sum)
