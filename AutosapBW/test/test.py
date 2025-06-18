# import pandas as pd 

# df=pd.read_csv('newfile.csv',header=20,sep='|',)

# print(df['Functional Location '])
#Column Names - ['Unnamed: 0', 'Functional Location ', 'Basic Start Date', 'Notification Nb', 'Short Text For Characteristic           ', 'Organism Text', 'Insp.  lot  ', 'Operation Short Text                ', 'Result             ', 'Sort.Field', 'Unnamed: 10']


# df=pd.read_html('0 source SBT 2024-06-24-15-58-43.html',header=0)[1]
# print(df)
# a=[]
# for x in df:
#     a.append(x)
# print(a)
# df2=pd.read_html('YANALYSIS_PATTERN_II.xls',header=0)[1]
# print(df2)py test.py

# from datetime import datetime, timedelta
# ftoday=datetime.today().replace(day=1)
# fyesterday=ftoday-timedelta(days=1)
# ffirstday_of_month=fyesterday.replace(day=1)
# today=ftoday.strftime('%d.%m.%Y')
# yesterday=fyesterday.strftime('%d.%m.%Y')
# firstday_of_month=ffirstday_of_month.strftime('%d.%m.%Y')

# print("T:",today)
# print("Y:",yesterday)
# print('F:',firstday_of_month)


# df=pd.read_html('QASR.html',header=0)[0]
# a=[]
# for x in df:
#     a.append(x)

# print(a)
# ['MANDANT', 'PRUEFLOS', 'VORGLFNR', 'MERKNR', 'PROBENR', 'SATZSTATUS', 'ATTRIBUT', 'QERGDATH', 'ERSTELLER', 'ERSTELLDAT', 'AENDERER', 'AENDERDAT', 'MBEWERTG', 'DBEWERTG', 'PRUEFER', 'PRUEFDATUV', 'PRUEFDATUB', 'PRUEFZEITV', 'PRUEFZEITB', 'PRUEFBEMKT', 'PRLTEXTKZ', 'LTEXTSPR', 'ISTSTPUMF', 'ANZFEHLEH', 'ANTEILNI', 'ANTEIL', 'ANZFEHLER', 'ANZWERTO', 'ANZWERTU', 'ANZWERTG', 'MAXWERTNI', 'MEDIANNI', 'MINWERTNI', 'MITTELWNI', 'VARIANZNI', 'MOMENT3NI', 'MOMENT4NI', 'ANTEILONI', 'ANTEILUNI', 'MAXWERT', 'MEDIANWERT', 'MINWERT', 'MITTELWERT', 'VARIANZ', 'MOMENT3', 'MOMENT4', 'ANTEILO', 'ANTEILU', 'KATALGART1', 'GRUPPE1', 'CODE1', 'VERSION1', 'KATALGART2', 'GRUPPE2', 'CODE2', 'VERSION2', 'KATALGART3', 'GRUPPE3', 'CODE3', 'VERSION3', 'KATALGART4', 'GRUPPE4', 'CODE4', 'VERSION4', 'KATALGART5', 'GRUPPE5', 'CODE5', 'VERSION5', 'FEHLKLAS', 'SENDEFLAG', 'MASCHINE', 'POSITION', 'AENDBELEG', 'KZBEWERTG', 'ZEITERSTL', 'ZEITAEND', 'ORIGINAL_INPUT', 'DIFF_DEC_PLACES', 'INPPROC_READY', 'SIGN_ID', 'SIGN_STATE']
# AENDERDAT, ZEITERSTL 
# from datetime import datetime, timedelta
# df['datetime']=pd.to_datetime(df['AENDERDAT'] +' '+df['ZEITERSTL'])
# yd=datetime.now()-timedelta(days=1)

# threshold=yd.replace(hour=22,minute=30,second=0,microsecond=0)

# lots_after_1030=df[df['datetime'] > threshold]
# lots_before_1030=df[df['datetime'] < threshold]

# print("Lots After 10 30",lots_after_1030[['PRUEFLOS','AENDERDAT','ZEITERSTL']])
# print("Lots Before 10 30",lots_before_1030[['PRUEFLOS','AENDERDAT','ZEITERSTL']])

# aft=lots_after_1030['PRUEFLOS'].tolist()
# bef=lots_before_1030['PRUEFLOS'].tolist()

# if 140007970546 in bef:
#     print("TTTT")

# if 140007970546 in aft:
    # print("T")

# li=[140007955554,140007955552,140007955553,140007955554,140007955554,140007955553,140007955554,140007955554,140007955554,140007955554]
# string='\n'.join(map(str,li))

# import pyperclip
# cop=pyperclip.copy(string)

# print(string)

# import pandas as pd 
# df=pd.read_html('0 Missing Lots 2024-06-24-18-38-35.html',header=0)[0]
# # ['MANDANT', 'PRUEFLOS', 'VORGLFNR', 'MERKNR', 'PROBENR', 'SATZSTATUS', 'ATTRIBUT', 'QERGDATH', 'ERSTELLER', 'ERSTELLDAT', 'AENDERER', 'AENDERDAT', 'MBEWERTG', 'DBEWERTG', 'PRUEFER', 'PRUEFDATUV', 'PRUEFDATUB', 'PRUEFZEITV', 'PRUEFZEITB', 'PRUEFBEMKT', 'PRLTEXTKZ', 'LTEXTSPR', 'ISTSTPUMF', 'ANZFEHLEH', 'ANTEILNI', 'ANTEIL', 'ANZFEHLER', 'ANZWERTO', 'ANZWERTU', 'ANZWERTG', 'MAXWERTNI', 'MEDIANNI', 'MINWERTNI', 'MITTELWNI', 'VARIANZNI', 'MOMENT3NI', 'MOMENT4NI', 'ANTEILONI', 'ANTEILUNI', 'MAXWERT', 'MEDIANWERT', 'MINWERT', 'MITTELWERT', 'VARIANZ', 'MOMENT3', 'MOMENT4', 'ANTEILO', 'ANTEILU', 'KATALGART1', 'GRUPPE1', 'CODE1', 'VERSION1', 'KATALGART2', 'GRUPPE2', 'CODE2', 'VERSION2', 'KATALGART3', 'GRUPPE3', 'CODE3', 'VERSION3', 'KATALGART4', 'GRUPPE4', 'CODE4', 'VERSION4', 'KATALGART5', 'GRUPPE5', 'CODE5', 'VERSION5', 'FEHLKLAS', 'SENDEFLAG', 'MASCHINE', 'POSITION', 'AENDBELEG', 'KZBEWERTG', 'ZEITERSTL', 'ZEITAEND', 'ORIGINAL_INPUT', 'DIFF_DEC_PLACES', 'INPPROC_READY', 'SIGN_ID', 'SIGN_STATE']
# # AENDERDAT, ZEITERSTL 
# print("DF Read")
# from datetime import datetime, timedelta
# df['date']=pd.to_datetime(df['AENDERDAT'], format='%d.%m.%Y')
# df['datetime']=pd.to_datetime(df['date'].dt.strftime("%Y-%m-%d") +' '+df['ZEITERSTL'])
# yd=datetime.now()-timedelta(days=1)
# threshold=yd.replace(hour=22,minute=30,second=0,microsecond=0)
# print("THR:",threshold)
# print("After Threshold")
# lots_after_1030=df[df['datetime'] > threshold]
# lots_before_1030=df[df['datetime'] < threshold]

# print("YESTRDAY",yd)
# print("Lots After 10 30",lots_after_1030[['PRUEFLOS','AENDERDAT','ZEITERSTL']])
# print("Lots Before 10 30",lots_before_1030[['PRUEFLOS','AENDERDAT','ZEITERSTL']])
# bef=lots_before_1030['PRUEFLOS'].tolist()
# aft=lots_after_1030['PRUEFLOS'].tolist()

# print("BEF",bef)
# print("AFT",aft)

# [7,15,22,29]
# n=7
# scroll=7
''' for first 8 --> 0-7
        Next 7 --> 1-7
        Next 7 --> 1-7
        (i-1)%7==0'''
# for i in range(30):
#     if i<=7:
#         print(i, True)
#     elif (i-1)%7==0:
#         print(i, 7 if i==8 else i) 

import pandas as pd

df=pd.read_html("sbt.html",header=0)[1]

print(df.shape)