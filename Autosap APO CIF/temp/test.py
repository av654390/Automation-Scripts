def test():
    import pandas as pd
    g=pd.read_html('canceled.html',header=0)[0]
    l=[]
    can= g[g['Status'] == 'Canceled']
    fin=g[g['Status'] == 'Finished']
    cj=can['JobName'].tolist()
    fj=fin['JobName'].tolist()
    for i in cj:
        if i in fj:
            print(i)
    # for i in g[g['Status']=='Canceled']:
    #     print(i)
        # l.append(i)

    # print(l)

    # ['JobName', 'Spool', 'Job\xa0CreatedB', 'Status', 'Sched.\xa0start\xa0date', 'Sched.\xa0start\xa0time', 'Duration(sec.)', 'Start\xa0date', 'Start\xa0Time', 'Delay\xa0(sec.)']

# test()
def test1():
    import pandas as pd
    g=pd.read_html('canceled.html',header=0)[0]
    l=[]
    j=g['JobName'].tolist()
    # print(j)
    # ['ALL_CF_CIF_REGENERATE', 'ALL_CF_CIF_REGENERATE_AP', 'ALL_CF_CIF_REGENERATE_MEA', 'ALL_CF_CIF_REGENERATE_NA', 'ALL_CF_CIF_REGENERATE_NA', 'BIREQU_AB4H4ZT844AORSF794CIFSTP6', 'Z_CIF_PIR_DELTA', '*Summary']
    d={'ALL_CF_CIF_REGENERATE':'Released','ALL_CF_CIF_REGENERATE_AP':'Released', 'ALL_CF_CIF_REGENERATE_MEA':'Released', 'ALL_CF_CIF_REGENERATE_NA':'Released','Z_CIF_PIR_DELTA':'Released'}

    for i in range(len(g.index)-1):
        if g['Status'][i]=='Canceled':
            d[g['JobName'][i]]='Canceled'
        else:
            d[g['JobName'][i]]=g['Status'][i]

    # d['ALL_CF_CIF_REGENERATE_NA']='Finished'

    if all(i=='Finished' for i in d.values()):
        # print(True)
        print(True)

    data=[]
    if not data:
        print("NOOOOTT")
    print(d)

# test1()


def test3():
    import pandas as pd
    g=pd.read_html('CIF20.html',header=0)[0]
    # Convert the 'Date' and 'Time' columns to datetime
    g=g[g['JobName']!='*Summary']
    g['Datetime']=pd.to_datetime(g['Sched.\xa0start\xa0date']+' '+g['Sched.\xa0start\xa0time'])

    #Sort the dataframe by 'Datetime' and 'Status' in descending order
    g.sort_values(by=['Datetime','Status'],ascending=[False,False], inplace=True)

    #Drop the 'Date', 'Time', and 'Datetime' Columns
    g.drop(['Sched.\xa0start\xa0date','Sched.\xa0start\xa0time','Datetime'],axis=1,inplace=True)

    #Drop duplicate rows based on 'Job Name' and keep the first occurence (Latest status)
    latest_status=g.drop_duplicates(subset='JobName', keep='first')

    #Convert the result to a dictionary in key-value format

    d=latest_status.set_index('JobName')['Status'].to_dict()
    print(d)

# test3()
def v():
    c=0
    import time
    # while True:
    #     print(c)
    #     c=c+1
    #     if c==3:
    #         exit()
    #     time.sleep(5)
    d={'BIREQU_1CCCIFK98ZAGTJTO2DA58QV6F': 'NA', 'ALL_CF_CIF_REGENERATE_NA': 'Finished', 'Z_CIF_PIR_DELTA': 'Finished', 'ALL_CF_CIF_REGENERATE': 'Finished', 'ALL_CF_CIF_REGENERATE_MEA': 'Finished', 'ALL_CF_CIF_REGENERATE_AP': 'Finished', 'BIREQU_0TRZKIZVE4K1F8WPSG6QDWCIF': 'Finished'}
    a1=open('a1.txt','r').read()
    # a2=open('a2.txt','r').read()
    print(a1)
    # print(a2)
    if a1==str(d):
        print("EQUAL")
    else:
        new_status=open('a1.txt','w')
        new_status.write(str(d))
    
# v()

def test2():
    import os
    import time
    import datetime,pytz
    tz=pytz.timezone('UTC')
    now=datetime.datetime.now(tz=tz)
    curtime=now.time()
    today4pm=now.replace(hour=16, minute=0, second=0, microsecond=0)
    date=now.strftime("%d.%m.%Y")
    # today = datetime.date.today(tz=tz)
    yesterday = now - datetime.timedelta(days=1)
    yesterday_str = yesterday.strftime("%d.%m.%Y")
    if now<today4pm:
        print("Yet to reach",curtime)
    else:
        print("4PPMM",today4pm)

    print(tz)
    print("Now",now)
    print("Yes",yesterday)
# test2()



import win32com.client as win32
import os
# import logon
def mail():
    f= open('cifmail.html',"r").read()
    data="Abc"
    date="11/11/11"
    f=f.replace('{data}',str(data))
    f=f.replace('{date}',date)
    body = f
    outlook = win32.gencache.EnsureDispatch('Outlook.Application')
    mail = outlook.CreateItem(0)
    # mail._oleobj_.Invoke(*(64209,0,8,To))
    mail.Subject="Testing"
    mail.To = "erry.x.lavakumar@haleon.com"#"CH_EP&T_APO_L2@haleon.com;CH_EP&T_APO_L3@haleon.com;shivaraju.x.mk@haleon.com"#
    mail.CC='akoju.x.sharanya@haleon.com'#;nikhil.x.chalikwar@haleon.com'
    # mail.HTMLBody = body
    path=os.getcwd()+'\\testing\\'

    for i in os.listdir(path):
        print(path+i)
        if i.lower().endswith(".html"):
            sum=open(path+i,'r').read()
            # attachment = mail.Attachments.Add(path+i)
            # attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F","screenshot")
            # print(i)
    mail.HTMLBody = body+sum
        
    # mail.Display()
    mail.Send()
    return "mail sent"

mail()