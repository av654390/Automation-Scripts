import win32com.client as win32
from dateutil.relativedelta import *
import datetime
import os

def ccmail(fpath,key_list): ##Summary+Screenshots
    try:
        now=datetime.datetime.now()
        today=now.strftime("%d.%m.%Y")
        n=now+relativedelta(months=+1) ##
        current_month=now.strftime("%m.%Y")
        next_month=n.strftime("%m.%Y")
        # nn=n+relativedelta(months=+1)
        outlook=win32.Dispatch("Outlook.Application")
        mail_item=outlook.CreateItem(0)
        # mail_item.To='erry.x.lavakumar@haleon.com'
        mail_item.To="akoju.x.sharanya@gsk.com"#'CH_EP&T_BASIS_SUPPORT@haleon.com'#'nikhil.x.chalikwar@haleon.com'#'akoju.x.sharanya@haleon.com'#'kanakakishore.8.telu@haleon.com'#'erry.x.lavakumar@haleon.com'#
        mail_item.CC=';erry.8.lavakumar@gsk.com'#nikhil.x.chalikwar@gsk.com
        mail_item.Subject=f"Certificate checks || Production Environment {now.strftime('%d-%m-%Y')}"

        f = open("bscm.html","r").read()  ## Html that contains screenshots
        bdy= open("bm.html","r").read() ## Html that contains Hello team
        sum=open(fpath+'Autosaphtml_sheet-'+today+'.html','r').read()
        
        f = f.replace("{current_month}",now.strftime("%B %Y"))
        f = f.replace("{next_month}",n.strftime("%B %Y"))
        bdy = bdy.replace("{current_month}",now.strftime("%B %Y"))
        bdy = bdy.replace("{next_month}",n.strftime("%B %Y"))
        j=0
        #print(path_list)
        for i in key_list:
            path=fpath+i
            ss=os.listdir(path)
            # print("SSSSS",ss)
            for s in ss:
                # print(s,i+current_month+'.png')
                if s==i+current_month+'.png':
                    cm=path.replace('/','\\')+"\\"+str(s)
                    # print(cm)
                    attachment = mail_item.Attachments.Add(cm)
                    attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F",f"{i}1")
                elif s==i+next_month+'.png':
                    nm=path.replace('/','\\')+"\\"+str(s)
                    print(nm)
                    attachment = mail_item.Attachments.Add(nm)
                    attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F",f"{i}2")
                else:
                    cm=path.replace('/','\\')+"\\"+str(s)
                    # print(cm)
                    attachment = mail_item.Attachments.Add(cm)
                    attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F",f"{i}1")

        # for i in path_list:
        #     if i is not None:
        #         ss=os.listdir(i) ##
        #         cm=i.replace('/','\\')+"\\"+str(ss[1])
        #         nm=i.replace('/','\\')+"\\"+str(ss[2])
        #         attachment = mail_item.Attachments.Add(cm)
        #         attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F","cm"+str(j))
        #         attachment = mail_item.Attachments.Add(nm)
        #         attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F","nm"+str(j))
                
        #         # print(cm)
        #         # print(nm)
        #         j+=1
        #     else:
        #         f = f.replace(f"cm{str(j)}","No Certificates Expiring")
        #         f = f.replace(f"nm{str(j)}","No Certificates Expiring")
        #         j+=1
        #path="C:\\Users\\el9fq8580\\Desktop\\VSCode\\CertificatesCheck\\text_report\\"
        # path=os.getcwd()+"\\text_report\\"
        # report_list=os.listdir(path)
        # for i in report_list:
        #     mail_item.Attachments.Add(path+i)
        mail_item.HTMLBody = bdy+sum+f
        mail_item.Send()
        # print(path_list)
        return "mail sent!"
    except Exception as e:
        print(e)
        return "Error in Sending Mail"


if __name__ == "__main__":
    pass