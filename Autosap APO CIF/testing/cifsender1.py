
import win32com.client as win32
import os
# import logon
def sender(path,data,sub,date):
    # total=[]    
    try:
        # sub= f"Autosap hourly monitoring RBQ {stamp } GMT"
        if not data:
            data=None 
        f= open('cifmail.html',"r").read()
        f=f.replace('{data}',str(data))
        f=f.replace('{date}',date)
        # print(os.getcwd())
        body = f
        outlook = win32.gencache.EnsureDispatch('Outlook.Application')
        mail = outlook.CreateItem(0)
        # mail._oleobj_.Invoke(*(64209,0,8,To))
        mail.Subject=sub
        mail.To = "erry.x.lavakumar@haleon.com"#"CH_EP&T_APO_L2@haleon.com;CH_EP&T_APO_L3@haleon.com;shivaraju.x.mk@haleon.com"#
        mail.CC='akoju.x.sharanya@haleon.com;nikhil.x.chalikwar@haleon.com'
        
        for i in os.listdir(path):
            if i.lower().endswith(".html"):
                summ=open(path+i,'r').read()
                # attachment = mail.Attachments.Add(path+i)
                # attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F","screenshot")
                # print(i)
            
        # mail.Display()
        mail.HTMLBody = body+summ
        mail.Send()
        return "mail sent"

    except Exception as e:
        return {"error":0,"message":f"error in sender {e}"}
    # finally:
    #     pass
        # f"smq2 redo {stamp}.html"
if __name__ == "__main__":
    # import datetime,pytz
    # #tz=pytz.timezone('Europe/London')
    # To = 'CH_EP&T_APO_L3@haleon.com'
    # stamp=datetime.datetime.now(tz=tz).strftime("%Y-%m-%d-%H-%M-%S")
    # path= os.getcwd()+r"\\excel_data\Autosap_cancelled_1689326934.7433019\\"
    # sub= f"Autosap CIF job monitoring {stamp }"
    # #ht=path + r"Autosapexcel_sheet-2022-12-01-14-22-19.html"
    # print(sender(path,output,sub,date))
    pass