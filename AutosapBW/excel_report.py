# ****************************************************************************
#  Program Description : Script Generates Excel Report                       *
#  Program Name:  AutosapBW\excel_report.py                                  *
#          Date:  21/06/2024                                                 *
#       version:  1.0.0                                                      *
#        Author:  Erry Lavakumar                                             *
#  Return Codes:                                                             *
#                 0 - Success                                                *
#                 1 - Error check log file                                   *
# ****************************************************************************
#  AutoSAP Automation                                                        *
#  --------------------                                                      *
#  Sr.         Role           Member          Email                          *
#  ---------   ----------     --------------  -------------------------------*
#  1           Developer      NIKHIL CHALIKWAR  nikhil.x.chalikwar@gsk.com   *
#  2           Developer      Erry Lavakumar    erry.8.lavakumar@gsk.com     *  
#  2           Developer      Akoju Sharanya    akoju.x.sharanya@gsk.com     *  
#                                                                            *
# ****************************************************************************

# Function to Generate Analyzed Excel Report #
def gen(nos=0,session=0,path=0,stamp=0,sbt_file=0):

    import pandas as pd
    import re
    import os
    import datetime

    # Generate timestamp
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    name1 = "YANALYSIS_PATTERN_II.xlsx"
    # path = os.path.join(os.getcwd(), "excel data", f"autosap_{stamp}")
    os.makedirs(path, exist_ok=True)
    output_file1_path = os.path.join(path, f"Final_Report_{stamp}.xlsx")
    output_file2_path = os.path.join(path, f"SBT_Analysed_{stamp}.xlsx")
    df1 = pd.read_html(path+'YANALYSIS_PATTERN_II.xls',header=0)[1]
    df2 = pd.read_html(path+sbt_file,header=0)[1]
    # ['Functional\xa0Location', 'Basic\xa0Start\xa0Date', 'Notification\xa0Nb', 'Short\xa0Text\xa0For\xa0Characteristic', 'Organism\xa0Text', 'Insp. lot', 'Operation\xa0Short\xa0Text', 'Result', 'Sort.Field']
    
    #Function to extract numeric value 
    def extract_numeric_value(s):
        numeric_values = re.findall(r'-?\d+(?:[\.,]\d+)?', str(s))
        if numeric_values:
            return float(numeric_values[0].replace(',', '.'))
        else:
            return None

    # Function to check if a string contains only uppercase alphabetic characters
    def contains_only_uppercase(s):
        return bool(re.fullmatch(r'[a-z,A-Z]+', str(s).strip()))

    # Filter out rows where 'Result' contains only uppercase alphabetic characters
    df2 = df2[~df2['Result'].apply(contains_only_uppercase)]

    # Apply function to 'Result' column and create a new column 'Sum of results(ECC)'
    df2['Sum of results(ECC)'] = df2['Result'].apply(extract_numeric_value)

    # Select necessary columns from df2 to concatenate with df1
    df2_subset = df2[['Insp. lot', 'Sum of results(ECC)']].reset_index(drop=True)

    # Pivoting the ECC Inspection Lots
    df2_group =df2_subset.groupby('Insp. lot',as_index=False)['Sum of results(ECC)'].sum()
    # Concatenate df1 and df2_subset horizontally (along columns)
    concatenated_file = pd.concat([df1, df2_group], axis=1)
    # Making sure that the Lots Column is in Integer type
    concatenated_file['Inspection Lot']=concatenated_file['Inspection Lot'].fillna(0)
    concatenated_file['Inspection Lot']=concatenated_file['Inspection Lot'].astype('int64')
    concatenated_file['Insp. lot']=concatenated_file['Insp. lot'].fillna(0)
    concatenated_file['Insp. lot']=concatenated_file['Insp. lot'].astype('int64')
    print(concatenated_file['Inspection Lot'])
    print(concatenated_file['Insp. lot'])

    # Perform VLOOKUP equivalent for 'Not in ECC' & 'Not in BW' column
    concatenated_file['Not in ECC'] = concatenated_file['Inspection Lot'].apply(lambda x: x if x not in df2['Insp. lot'].values else 'NA')
    concatenated_file['Not in BW'] = concatenated_file['Insp. lot'].apply(lambda x: x if x not in df1['Inspection Lot'].values else 'NA')
    # concatenated_file.to_excel(output_file1_path, index=False, engine='openpyxl') 
    print("No Issues Till Report Analysis!")
    nonzerodf=concatenated_file[(concatenated_file['Not in BW']!=0) & (concatenated_file['Not in BW']!='NA')]
    not_in_bw=nonzerodf['Not in BW'].reset_index(drop=True)
    df_not_in_bw=not_in_bw.to_dict()
    # Create 'Comments' column
    import source
    lots_missing=source.se16(nos=0,session=session,path=path,stamp=stamp,reason='reason',dict1=df_not_in_bw)
    print("DICT:",df_not_in_bw)
    print("Lots Missing:",lots_missing)
    global before_list,after_list

    before_list=lots_missing['Before']
    print("Missing Lots Which Ran Before 10:30 PM Yesterday:",before_list)
    after_list=lots_missing['After']
    print("Missing Lots Which Ran After 10:30 PM Yesterday:",after_list)

    def generate_comments(row):
        comments = []
        if row['Not in BW'] != 'NA' and int(row['Not in BW']) in after_list:
            comments.append('not in BW because the timestamp is after 10:30,expected in next delta running')
        elif row['Not in BW'] != 'NA' and int(row['Not in BW']) in before_list:
            comments.append('Lot Missing')
        return ', '.join(comments)

    concatenated_file['Comments'] = concatenated_file.apply(generate_comments, axis=1)
    print("Comments Column Added Successfully!")
    df2.to_excel(output_file2_path, index=False, engine='openpyxl')         # Save df2 with new column
    concatenated_file.to_excel(output_file1_path, index=False, engine='openpyxl')    # Save concatenated file

    print("Excel Files saved successfully!")

    return concatenated_file[concatenated_file['Insp. lot']!=0]['Insp. lot'].to_dict()

