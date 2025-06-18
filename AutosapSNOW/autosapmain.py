## Pre-Requisites ##
# pip install pytz
# pip install pandas
# pip install python-docx
# pip install python-dateutil

## Import All required files #Custom Modules

import os
import sys
import datetime
import logon
import read
import dp115, cus115, not115
import sender
import generatedoc

RBQ= "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"

# uuser = "mg992450"
now = datetime.datetime.now()
stamp = now.strftime("%Y-%m-%d-%H-%M-%S")
today = now.strftime("%d-%M-%y")
# tempdir= f"autosap {stamp}"
cd = os.getcwd()
path = cd + f'\excel data\AutoSAP_{stamp}\\'
os.makedirs(os.path.dirname(path),exist_ok=True)
org = os.path.join(cd ,'Data Change Form.docx')
sys.stdout = open(path+"LOG"+stamp+".txt", "w")
print("Files will be stored in the path-",path)

tickets = read.tickets()
cat_113 = tickets['cat_113']
cat_114 = tickets['cat_114']
cat_115 = tickets['cat_115']
cat_116 = tickets['cat_116']
session=logon.Autosap(RBQ)
send_from = "noreply-autosapautomation@gsk.com"
send_cc = ["erry.8.lavakumar@gsk.com"]
send_bcc = ["erry.8.lavakumar@gsk.com"]


def perform115(task):
    print('_'*100)
    print("SC Task :",task)
    request_item = cat_115[task]['request_item']
    print("Request Item:",request_item)
    docid = cat_115[task]['docid']
    print('docid:',docid)
    uuser = cat_115[task]['uuser']
    print("UUser:",uuser)
    opened_by = cat_115[task]['opened_by']
    opened_by_email = cat_115[task]['opened_by_email']
    print(opened_by, opened_by_email)
    send_to = []
    npath = os.path.join(path,f"{task}_{request_item}")
    subject = f"Update on your request - {task}"
    if len(docid) >12 or len(docid)<3:
        print("Inavlid DP number:",docid)
    else:
        result = dp115.dpforward(session,npath,stamp,docid,uuser)
        print(result)
        try:
            
            if result['error'] == 1:
                print("After Success")
                tar = os.path.join(npath,f'DCF {request_item}.docx')
                print(tar)
                print(cat_115[task])
                d = generatedoc.gen(org,tar,npath,today,data=cat_115[task])
                print("Doc Generated ")
            elif result['error'] == 4:
                pass
            else:
                print(result['message'])
        except Exception as e:
            print("Final :",e)
        # if isinstance(result,dict):
        #     if result['error'] ==1:
        #         html = 'mail_positive.html'
        #     dtype = result[dtype]
        #     html = ''
        #     sender.send_mail(send_from, send_to, send_cc, send_bcc, subject, text='test', files=npath,html=html,data = cat_115,task = task)
    # break
for task in cat_115:
    perform115(task)
print(logon.logof(session))