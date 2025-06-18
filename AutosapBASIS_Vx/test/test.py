# # session.findById("wnd[0]/usr/cntlCL_GRID/shellcont/shell").selectedRows = "0"
# # variablename=session.findById("wnd[0]/usr/cntlCL_GRID/shellcont/shell").GetCellValue(row number,"column name")
# from datetime import timedelta
# import datetime,pytz
 
# # tz=pytz.timezone('Asia/Kolkata')
# tz=pytz.timezone('UTC')
# tz=pytz.timezone('CET')
# tm=datetime.datetime.now(tz=tz) - timedelta(hours=11)
# sd= tm.strftime("%d.%m.%Y")
# et= datetime.datetime.now(tz=tz).strftime("%H:%M:%S")
# st= tm.strftime("%H:%M:%S")
# ed= datetime.datetime.now(tz=tz).strftime("%d.%m.%Y")
# print("SD:",sd)
# print("ET:",et)
# print("ST:",st)
# print("ED:",ed)
# import pandas as pd
# df=pd.read_html('ST22all.html',header=0)[0]
# a=[]
# print('###ST22')
# for i in df:
#     a.append(i)
# print(a)
# dumps_count=len(df.index)
# print(dumps_count)
# n=df[df['Runtime\xa0Error']=="TIME_OUT"]
# print(len(n))
# dumps_count=200
# if dumps_count <200:
#     status='Green' 
# elif dumps_count>=200 and dumps_count<340:
#     status='Amber' 
# else:
#     status='Red'
# # print(status)

# print('###ST07')
# df1=pd.read_html('ST07.html',header=1)[1]
# # print(df1)
# cols=[]
# for i in df1:
#     cols.append(i)
# print(cols) #['Unnamed: 0', 'LoggedOn', 'Active', 'In\xa0WP', 'User', 'Server']
# row=df1[df1['Unnamed: 0']=='Total'].index
# print(row[0])
# act_users=df1.loc[row[0],'Active']
# wp=df1.loc[row[0],'In\xa0WP']
# # print('WP-',wp)
# # print('act-',act_users)
# # print(df1.Total==22)

# print('### DB02 ###')
# df2=pd.read_html('db02.html',header=0)[0]
# print(df2)
# c=[]
# for i in df2:
#     c.append(i)
# #Columns=['Tablespace\xa0name', 'Size(MB)', 'Free(MB)', 'Used(%)', 'Autoextend', 'Total\xa0size(MB)', 'Total\xa0free\xa0space(MB)', 'Total\xa0used\xa0(%)', '#Files', '#Segments', '#Extents', 'Status', 'Contents', 'Compression', 'Compress\xa0for', 'Encrypted', 'Encrypt\xa0algorithm']
# print(c)
# req=['PSAPR3I','PSAPUNDO','PSAPR3I750','PSAPR3IINDEX','PSAPSOFFCONT1']
# db02_dict={}
# for k in req:
#     db02_dict[k]=df2.loc[df2['Tablespace\xa0name']==k,'Used(%)'].values[0]
# # db02_dict['PSAPR3I']=df2.loc[df2['Tablespace\xa0name']=='PSAPR3I','Used(%)'].values[0]
# # db02_dict['PSAPUNDO']=df2.loc[df2['Tablespace\xa0name']=='PSAPUNDO','Used(%)'].values[0]
# # db02_dict['PSAPR3I750']=df2.loc[df2['Tablespace\xa0name']=='PSAPR3I750','Used(%)'].values[0]
# # db02_dict['PSAPR3IINDEX']=df2.loc[df2['Tablespace\xa0name']=='PSAPR3IINDEX','Used(%)'].values[0]
# # db02_dict['PSAPSOFFCONT1']=df2.loc[df2['Tablespace\xa0name']=='PSAPSOFFCONT1','Used(%)'].values[0]
# print(db02_dict)


# print("####STAMP###")
# from datetime import datetime
# # import 
# now=datetime.now()
# stamp=now.strftime("%Y-%m-%d-%H-%M-%S")
# print(stamp)
# print(stamp[:10])
# print(stamp[11:])


# f()
sm59_list=["SEAL-CONNC","SEAL-CONVUTIL","SEAL-CONVUTIL-1","SEAL-CONVUTIL-2","SEAL-CONVUTIL-3","SEAL-VIEW-CKL-CONV00","SEAL-VIEW-CKL-CONV01","SEAL-VIEW-CKL-CONV02","SEAL-VIEW-CKL-CONV03","SEAL-VIEW-CKL-CONV04","SEAL-VIEW00","SEAL-VIEW01","SEAL-VIEW02","SEAL-VIEW03","SEAL-VIEW04","SEAL-VIEW05","SEAL-VIEW06","SEAL-VIEW07","SEAL-VIEW08","SEAL-VIEW09","SEAL-VIEW10","SEAL-VIEW11","SEAL-VIEW12","SEAL-VIEW13","SEAL-VIEW14","SEAL-VIEW15","TREX_TRP"]
print("Length=",len(sm59_list))
# print("######")
# print("\n ####")
# print("\n###")
# final_values={'db02_dict':db02_dict}
# for i in final_values['db02_dict']:
#     print(final_values['db02_dict'][i])

# st=pd.read_html('rcpu.html',header=0,decimal=',',thousands='.')[0]
# #['Process\xa0ID', 'User', 'Process\xa0Name', 'Utilizatn', 'CPU\xa0Time', 'ResidentSz', 'Priority']
# val=st.loc[st['Process\xa0Name'].str.contains('ragent'),'Utilizatn'].values[0]
# print(val/100)
# if 1.705>1.5:
#     print(True)
# if val<1.5:
#     status='Green'
# elif val>=1.5 and val<2:
#     status='Amber'
# elif val>=2:
#     status='Red'

# print(st['Process\xa0Name'].to_list())

# print("###SE38###")
# nf=pd.read_html('sbvse38.html',header=0,thousands='.')[0]
# # #['Time', 'AS\xa0Instance', 'Act.\xa0WPs', 'Dia.WPs', 'RFC\xa0Normal', 'CPU\xa0Usr', 'CPU\xa0Sys', 'CPU\xa0Idle', 'Paging\xa0in', 'Paging\xa0out', 'Free\xa0Mem.', 'EM\xa0alloc.', 'EM\xa0attach.', 'Em\xa0global', 'Heap\xa0Memor', 'Pri.', 'Paging\xa0Mem', 'Dia.', 'Upd.', 'Enq.', 'Logins', 'Sessions']
# val=nf['Time']
# latest_time=nf[nf['Time']==nf.loc[0,'Time']]
# print("LLLATEST",latest_time)
# sum_login=latest_time['Logins'].sum()
# sum_sessions=latest_time['Sessions'].sum()
# wp_priv=latest_time['Pri.'].sum()
# print(sum_sessions,sum_login)

# cpu_idle=latest_time.loc[nf['AS\xa0Instance']=='rixsap2v_SBV_09','CPU\xa0Idle'].values[0]
# cpu_u=100-cpu_idle
# print((cpu_idle,cpu_u))
# nn=pd.read_html('abc.html',header=0)[0]

# # print(len(nn))
# # all_status=['Green','Green','Green']
# # if 'Red' in all_status:
# #     overall_status='Red'
# # elif 'Amber' in all_status:
# #     overall_status='Amber'
# # elif all(ele == 'Green' for ele in all_status):
# #     overall_status='Green'

# # print("OVER ALL STATUS",overall_status)
# # # print(round(2223.18828,2))


# # print("########ST06 CPU######")
# # df1=pd.read_html('st06cpu.html',header=0)[0]
# # print(df1)
# # dict1=df1.set_index('App.Server')['Value'].to_dict()
# # print(dict1)

# # df2=pd.read_html('st06fm.html',header=0)[0]
# # # ['App.Server', 'Category', 'Descript.', 'Value', 'Unit']
# # dict2=df2.set_index('App.Server')['Value'].to_dict()
# # print(dict2)

# # combined_dict={k:[round(100-dict1[k],2),dict2[k]] for k in dict1}

# # print(combined_dict)



# # x="abc.png"
# # if x.endswith(".xlsx" or '.png'):
# #     print("XXXX",x)
# # else:
# #     print("YYYYY")


# import pandas as pd 
# nf=pd.read_html("se38test.html",header=0,thousands='.',decimal=',')[0]
# print(nf)
# latest_time=nf[nf['Time']==nf.loc[0,'Time']]

# ##Logins Data##
# logins=latest_time['Logins'].sum()
# print(logins)
# if logins<6000:
#     logins_status='Green'
# elif logins>=6000 and logins<7000:
#     logins_status='Amber'
# elif logins>=7000:
#     logins_status='Red'

# ##Sessions Data##
# sessions=latest_time['Sessions'].sum()
# if sessions<9500:
#     sessions_status='Green'
# elif sessions>=9500 and sessions<10000:
#     sessions_status='Amber'
# elif sessions>=10000:
#     sessions_status='Red'

# ##WPs Priv Mode Data##
# wps=latest_time['Pri.'].sum()
# if wps<150:
#     wps_status='Green'
# elif wps>=150 and wps<200:
#     wps_status='Amber'
# elif wps>200:
#     wps_status='Red'
# print(wps,"WPS")
# ##CPU Utilization% Data##
# try:
#     cpu_idle=latest_time.loc[nf['AS\xa0Instance']=='rixsasp1_SBP_00' or nf['AS\xa0Instance']=='rixsasap001_SBT_01','CPU\xa0Idle'].values[0]
# except:
#     cpu_idle=latest_time.loc[nf['AS\xa0Instance']=='rixsasap001_SBT_01','CPU\xa0Idle'].values[0]

# cpu=100-cpu_idle
# if cpu<80:
#     cpu_status='Green'
# elif cpu>=80 and cpu<90:
#     cpu_status='Amber'
# elif cpu>=90:
#     cpu_status='Red'   

# print(cpu)


# print(isinstance('abc',str))
# import json
# f=open('sys.txt','r')
# sys=f.read()
# sid=json.loads(sys)
# print(sid,type(sid))
# print(sid['SBV'])
# f.close()

# with open('sys.txt', 'r') as file:
#     data = file.read()
#     sid = json.loads(data)

# s1="Daily Monitoring 23.09.2024 "
# s2="Daily Monitoring"
# s3="Not Monitoring"
# import re
# pattern="Daily Monitoring \d{2}.\d{2}.\d{4}$"
# for i in [s1,s2,s3]:
#     print(bool(re.match(pattern,i)))