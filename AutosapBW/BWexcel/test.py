 # #column2_data = df2['Result]   #access by its column name
# # #column2_data = df2.iloc[:,1]   #accesses it by index
# # #df2["Result"].str.replace(r'\D+', '').str.replace(',', '.')  #.str is used to convert data in column2 into string and then applying string function like the regular expression pattern r'\D+' to replace all non-digit characters (\D+) with an empty string ('')
#f=pd.read_html(path+fname,decimal=",",thousands=".",header=0)[1]

import re

data = [
    '0 CFU/10ml',
    '<0,25 EU/ml',
    '0,9 µS/cm',
    '0 CFU/200ml',
    '15 particles/m³',
    '25,9 °C',
    '392,9 ppb',
    '0 CFU/CP',
    '9 ppb',
    '-25,9 ppb'
]

def extract_numeric_value(s):
    # Find all sequences of digits (including decimals and negative signs)
    numeric_values = re.findall(r'-?\d+\.*\d*', s)

    # Return only the first numeric value found (ignoring units and extra characters)
    if numeric_values:
        return float(numeric_values[0])
    else:
        return None

for item in data:
    numeric_value = extract_numeric_value(item)
    if numeric_value is not None:
        print(numeric_value)

print(bool(re.fullmatch(r'[a-z,A-Z]+', 'Ba')))
# Perform VLOOKUP equivalent for 'Not in ECC' column and 'Not in BW'
#concatenated_file['Not in ECC'] = concatenated_file['Inspection Lot'].apply(lambda x: x if x not in df2['Insp.  Lot'].values else 'NA')
#concatenated_file['Not in BW'] = concatenated_file['Insp.  Lot'].apply(lambda x: x if x not in df1['Inspection Lot'].values else 'NA')

# Sort both DataFrames by the relevant columns
# df1 = df1.sort_values(by='Inspection Lot').reset_index(drop=True)
# df2 = df2.sort_values(by='Insp.  lot').reset_index(drop=True)
# 1.40009E+11	PASS	
# 1.40009E+11	PASS	
# 1.40009E+11	LE	