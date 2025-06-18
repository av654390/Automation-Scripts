import pandas as pd
import re
import os
import datetime

# Generate timestamp
stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
name1 = "result_BW.xlsx"
name2 = "result_SBT.xlsx"
path = os.path.join(os.getcwd(), "excel data", f"autosap_{stamp}")
os.makedirs(path, exist_ok=True)
output_file1_path = os.path.join(path, f"result_BW_{stamp}.xlsx")
output_file2_path = os.path.join(path, f"result_SBT_{stamp}.xlsx")
df1 = pd.read_excel(name1, engine='openpyxl')
df2 = pd.read_excel(name2, engine='openpyxl')
#print(df2)
#Function to extract numeric value 
def extract_numeric_value(s):
    numeric_values = re.findall(r'-?\d+(?:[\.,]\d+)?', str(s))
    if numeric_values:
        return float(numeric_values[0].replace(',', '.'))
    else:
        return None

# Function to check if a string contains only uppercase alphabetic characters
def contains_only_uppercase(s):
    return bool(re.fullmatch(r'[a-z,A-Z]+', s.strip()))

# Filter out rows where 'Result' contains only uppercase alphabetic characters
df2 = df2[~df2['Result'].apply(contains_only_uppercase)]

# Apply function to 'Result' column and create a new column 'Sum of results(ECC)'
df2['Sum of results(ECC)'] = df2['Result'].apply(extract_numeric_value)

# Select necessary columns from df2 to concatenate with df1
df2_subset = df2[['Insp.  Lot', 'Sum of results(ECC)']].reset_index(drop=True)

# Concatenate df1 and df2_subset horizontally (along columns)
concatenated_file = pd.concat([df1, df2_subset], axis=1)

# Perform VLOOKUP equivalent for 'Not in ECC' & 'Not in BW' column
concatenated_file['Not in ECC'] = concatenated_file['Inspection Lot'].apply(lambda x: x if x not in df2['Insp.  Lot'].values else 'NA')
concatenated_file['Not in BW'] = concatenated_file['Insp.  Lot'].apply(lambda x: x if x not in df1['Inspection Lot'].values else 'NA')

# Create 'Comments' column
def generate_comments(row):
    comments = []
    # if row['Not in ECC'] == 'NA':
    #     comments.append('not in ECC because the timestamp is after 10:30,expected in next delta running')
    if row['Not in BW'] != 'NA':
        comments.append('not in BW because the timestamp is after 10:30,expected in next delta running')
    return ', '.join(comments)

concatenated_file['Comments'] = concatenated_file.apply(generate_comments, axis=1)

df2.to_excel(output_file2_path, index=False, engine='openpyxl')         # Save df2 with new column
concatenated_file.to_excel(output_file1_path, index=False, engine='openpyxl')    # Save concatenated file

print("Files saved successfully.")










#print(df2)            #[Insp.  lot    Result  Numeric_Value]
# Regular expression to find numeric values (including decimals and negative signs)
 # Return the first numeric value found as float, or None if no numeric value is found
  # Replace commas with dots for consistency and convert to float
