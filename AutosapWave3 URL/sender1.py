import win32com.client as win32
# import sys
# import time
# import datetime
# from dateutil.relativedelta import relativedelta
# import calendar
# import pandas as pd
# import mail_excel_data         
# import os
import os
# import logon
def sender(path,To,sub,ht):
    # total=[]    
    try:
        # sub= f"Autosap hourly monitoring RBQ {stamp } GMT"        
        f= open(ht,"r").read()
        # print(os.getcwd())
        body = "hi hello"
        outlook = win32.gencache.EnsureDispatch('Outlook.Application')
        mail = outlook.CreateItem(0)
        # mail._oleobj_.Invoke(*(64209,0,8,To))
        mail.Subject=sub
        mail.To = To
        mail.HTMLBody = "Hi Team .<br> Please find the below status of JAVA monitoring ."+body
        # for i in os.listdir(path):
        #     if i.lower().endswith(".html"):
        #         # print(i)
        #         mail.Attachments.Add(Source=path+i)
        # mail.Display()
        mail.Send()
        return "mail sent"

    except Exception as e:
        return {"error":0,"message":f"error in sender {e}"}
    # finally:
    #     pass
        # f"smq2 redo {stamp}.html"
if __name__ == "__main__":
    import datetime,pytz
    tz=pytz.timezone('Europe/London')
    To = 'nikhil.x.chalikwar@gsk.com'
    stamp=datetime.datetime.now(tz=tz).strftime("%Y-%m-%d-%H-%M-%S")
    path= os.getcwd()+r"\\excel data\autosap 2022-12-01-14-22-19\\"
    sub= f"Autosap hourly monitoring RBQ {stamp } GMT"
    ht=r"C:\Users\nc843765\OneDrive - GSK\NKISLIVE\thecode\CIF\cif_c.html"
    print(sender(path,To,sub,ht))


    # "//*[@id="sys_readonly.sys_user.user_name"]
    # /html/body/div[2]/div[6]/div[3]/form/div/span/span/div[4]/div[1]/div[1]/div[1]/div[2]/input[1]"