import pandas as pd
import numpy as np
### AVG Mem ###
nf = pd.read_html("ST06 Mem new.html",header=0,decimal=',',thousands='.')[0]
latest_time=nf[(nf['Date']==nf.loc[0,'Date'])&(nf['Hour']==nf.loc[0,'Hour'])]
print("Used memory percentages:",latest_time['User\xa0Utilization[%]'].to_list())
unused_memory = 100 - latest_time['User\xa0Utilization[%]']
print(unused_memory)
# Check if the unused memory is in the range of 90 to 100 (this is equivalent to checking if the used memory is in the range 0-10)
threshold_exceeded = unused_memory.between(90, 100)
average_value = latest_time['User\xa0Utilization[%]'].mean()
# threshold_exceeded = latest_time['Percentage_Used[%]'].between(90, 100)

print("Average memory Value:", average_value)
average_memory_usage = round(average_value, 2)
# nf = pd.read_html(path+nfname,header=0,decimal=',',thousands='.')[0]
# a=[]
# for i in nf:
#     a.append(i)
# print(a)
# latest_time=nf[(nf['Date']==nf.loc[0,'Date'])&(nf['Hour']==nf.loc[0,'Hour'])]
# print("Used memory percentages:",latest_time['Percentage_Used[%]'].to_list())
# average_value = latest_time['Percentage_Used[%]'].mean()
# # threshold_exceeded = latest_time['Percentage_Used[%]'].between(90, 100)

# print("Average memory Value:", average_value)
# average_memory_usage = round(average_value, 2)

# f = pd.read_html('ST06 CPU.html', header=0)[0]
# try:
#     cpu_idle_value = pd.to_numeric(f.loc[(f['Category'] == 'CPU') & (f['Description'] == 'Idle'),'Value'], errors='coerce').values
#     cpu_used_value = 100 - cpu_idle_value
# except:
#     cpu_idle_value = pd.to_numeric(f.loc[(f['Monitoring\xa0Category'] == 'CPU') & (f['Description'] == 'Idle'),'Value'], errors='coerce').values
#     cpu_used_value = 100 - cpu_idle_value
        
# print(cpu_idle_value)
# print(cpu_used_value)
# threshold_exceeded = cpu_idle_value.between(85,100)
# if threshold_exceeded.any():
#     print(f["Application\xa0Server"])
# a={}
# if a is None:
#     print(True)
# f = pd.read_html("st06_new.html",header=0)[0]
# #print(f)
# '''
# application_server_id = df["Application\xa0Server"][0]
# print("ID",application_server_id)
# '''
# # for i in f:
# #     a.append(i)
# # print(a) #['Monitoring\xa0Category', 'Description', 'Value', 'Unit']

# for i in f.index:
#     a.append(f['Value'][i])
# print(a)

# Ensure the 'Value' column is numeric, coercing any errors to NaN (which will be ignored in the mean calculation)
# cpu_idle_value = pd.to_numeric(f.loc[(f['Monitoring\xa0Category'] == 'CPU') & (f['Description'] == 'Idle'),'Value'], errors='coerce').values
# print("CPU Idle Values:", cpu_idle_value)
# average_value = cpu_idle_value.mean()
# print("Average CPU Idle Value:", average_value)
# result = 100 - average_value
# print("100 - Average CPU Idle Value:", result)
# print(f['Description'][8:20])
# freememory_value = pd.to_numeric(f.loc[(f['Category'] == 'Memory') & (f['Description'] == 'Free\xa0memory\xa0percentage'),'Value'], errors='coerce').values
# print("FRee memory percentages:", freememory_value)
# average_value = freememory_value.mean()
# if average_value:
#     print(True)
# print("Average memory Value:", average_value)
# result = 100 - average_value
# print("100 - Average memory Value:", result)

# freememory_value = f.loc[(f['Monitoring\xa0Category'] == 'Memory') & (f['Description'] == 'Free\xa0memory\xa0percentage'), 'Value'].values[0]
# print(f"memory utilization: {freememory_value}")

# df = pd.read_html("al08.html",header=0)[0]
# #print(df)
# for i in df:
#     a.append(i)
# print(a)
# user_logons = df['User\xa0ID']
# print(f"User Logons: {user_logons}")

# nf = pd.read_html("st06new.html",header=0,decimal=',',thousands='.')[0]
# latest_time=nf[(nf['Date']==nf.loc[0,'Date'])&(nf['Hour']==nf.loc[0,'Hour'])]
# a=[]
# for i in nf:
#     a.append(i)

# print(a)
# print(latest_time['Percentage_Used[%]'].to_list())
# try:
#     cpu_used_all = latest_time['Percentage_Used[%]'].sum()
#     avg_cpu_used = cpu_used_all/len(latest_time)
#     print("CPU USED : ",avg_cpu_used)
#     if avg_cpu_used<6000:
#         avg_cpu_used_status='Green'
#     elif avg_cpu_used>=6000 and avg_cpu_used<7000:
#         avg_cpu_used_status='Amber'
#     elif avg_cpu_used>=7000:
#         avg_cpu_used_status='Red'
#     print(avg_cpu_used_status)
# except:
#     print(0)
# import re
# df=pd.read_csv("al08.txt",header=None)
# #print(df)
# # for i in df[0]:
# #     a.append(i)
# # print(a)
# userlogon = df.iloc[-1,0] # Get the last row, first column
# print("User Logon Line:", userlogon)
# first_number = re.search(r'\d+', userlogon).group()
# print(first_number) 





# df2 = pd.read_html("db02.html",header=0)[0]
# # for i in df2:
# #     a.append(i)
# #print(a)
# #['Active', 'Host', 'Port', 'Service', 'Process\xa0ID', 'Detail', 'SQL\xa0Port', 'Start\xa0Time', 'Process\xa0CPU\xa0(%)', 'Total\xa0CPU\xa0(%)', 'Process\xa0Memory\xa0(GB)', 'Total\xa0Memory\xa0(GB)', 'Available\xa0Memory', 'Physical\xa0Memory\xa0(GB)', 'Process\xa0Physical\xa0Memory\xa0(GB)', 'Total\xa0Memory\xa0Used\xa0Size\xa0(GB)', 'Effective\xa0Allocation\xa0Limit\xa0(GB)', 'Heap\xa0Memory\xa0Used\xa0Size', 'Shared\xa0Memory\xa0Used\xa0Size']
# # for i in df2.index:
# #     a.append(df2['Total\xa0CPU\xa0(%)'][i])
# # print(a) #['1-', '0', '0', '0', '0', '0', nan]
# cpu_column = df2['Total\xa0CPU\xa0(%)']
# cpu_column_cleaned = (
#     cpu_column.str.replace("-", "", regex=False)  # Remove dashes
#     .replace("", np.nan)  # Replace empty strings with NaN
#     .astype(float)  # Convert to float
# )
# average_cpu = round(cpu_column_cleaned.mean(),2)

# print("Average Total CPU (%):", average_cpu)