# import pandas as pd 
# df=pd.read_html('sbtsm.html',header=0,encoding='utf-8')[1]

# df=df[df['Status']=]
# print(df['Status'])
# print(df)
# a=[]
# for i in df:
#     a.append(i)

# print(a)
#['Unnamed: 0', 'Cl.', 'Queue\xa0Name', 'Entries']

# print(any([0,0]))
# queues=df['Queue\xa0Name'].to_dict()
# print(queues)

# imp=['CSRIXSBPI','CSAMPLE-BIDR','DL','ZRO','WMTH0','WMD','EWMMEWMGOODSMVT','ZECC_FINDINGS','ZMNF','POFS']
# vimp=['EWMMEWMGOODSMVT','DL']

# fil_q={}
# for q in queues:
#     for i in imp:
#         if queues[q].startswith(i):
#             print("QUEUE",q,queues[q])
#             fil_q[q]=queues[q]
# print("FILTER",fil_q)
            
# print("LEN",len(fil_q)) 


# print("QQQ",26//25)



# if 'i' in []:
#     print(True)
# else:
#     print(False)

# d={0:'A',1:'B',2:'C',3:'D'}

# for i in d:
#     if i==1:
#         del d[i]

# print(d)

# d={}
# print(len(d))

import pandas as pd 
df=pd.read_html('sbtsm.html',header=0)[1]

print(df)
