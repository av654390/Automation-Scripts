#Step 1 (function 'sap_logon' in 'autosapcheck.py' file): Logs into SAP and creates a session
#Step 2 (function 'tcode' in 'autosapcheck.py' file): Performs SM37 T codes, takes screenshots of Expiring certificates and returns the path of screenshots saved
#Step 3 (function 'report' in 'report.py' file): Returns the report of expiring certificates in the format {Sysytem:{'overdue': 0, 'week0': 0, 'week1': 0, 'week2': 0, 'week3': 0, 'week4': 0, 'week5': 0, 'week6': 0, 'recent':'NA', 'certname':'NA}}
#Step 4 (function 'rex' in 'report.py' file): Creates a summary/report based on the above generated data
#Step 5 (function 'ccmail' in 'cc_mail.py' file): Sends mail to BASIS Team with the above created summary
#Step 6 (function 'logof' in 'autosapcheck.py' file): Logsoff from SAP session

print("""#######################################################################
#                                                  #
#######################################################################""")

import os
import time
import datetime
import subprocess
#import pyscreenshot
import win32com.client
from dateutil.relativedelta import *

import cc_mail
import report

## 'cred.txt' should contain SAP Logon ID in first line and Password in Second line ##
fi= open("cred.txt",'r')
id= fi.readline().strip()
passs= fi.readline().strip()

start=time.time()
import json
f=open('sys.txt','r')
syst=f.read()
sid=json.loads(syst)
f.close()


## Function for all SAP actions ## 
def tcode(session=0,cf=0,folder=0):
   try:
      if type(session)!=int and type(cf)!=int and type(folder)!=int:
         now=datetime.datetime.now()
         n=now+relativedelta(months=+1)
         nn=n+relativedelta(months=+1)
         cm=now.strftime("%m.%Y")
         nm=n.strftime("%m.%Y")
         nnm=nn.strftime("%m.%Y")
         d=[now,n,nn]
         dt=[cm,nm,nnm]
         #stamp=time.time()
         # base_dir=os.getcwd()+"\\Systems_Certificates_Data\\" ##
         sub_dir = os.path.join(folder,cf)
         os.makedirs(sub_dir)
         print(f"Sub directory for {cf} is {sub_dir}")
         session.findById("wnd[0]").maximize()
         session.findById("wnd[0]/tbar[0]/okcd").text = "/nsm37" #/nex
         session.findById("wnd[0]").sendVKey(0)
         session.findById("wnd[0]/usr/chkBTCH2170-SCHEDUL").selected = False
         session.findById("wnd[0]/usr/chkBTCH2170-READY").selected = False
         session.findById("wnd[0]/usr/chkBTCH2170-RUNNING").selected = False
         session.findById("wnd[0]/usr/chkBTCH2170-ABORTED").selected = False
         session.findById("wnd[0]/usr/txtBTCH2170-JOBNAME").text = "SSF*"#"*cert*"
         session.findById("wnd[0]/usr/txtBTCH2170-USERNAME").text = "*"
         session.findById("wnd[0]/usr/ctxtBTCH2170-FROM_DATE").text = ""
         session.findById("wnd[0]/usr/ctxtBTCH2170-TO_DATE").text = ""
         session.findById("wnd[0]/tbar[1]/btn[8]").press()
         message1=session.findById("wnd[0]/sbar").text
         print(message1)
         if message1=="No job matches the selection criteria":
            time.sleep(2)
            session.findById("wnd[0]").HardCopy(f"{sub_dir}\{cf}_JobsError.png")
            return {"error":4,"message":message1,"ttype":"Jobs"}
         time.sleep(2)
         try:
            ### For LPP ###
            session.findById("wnd[0]/usr/lbl[59,10]").setFocus()
            session.findById("wnd[0]/usr/lbl[59,10]").caretPosition = 6
            session.findById("wnd[0]").sendVKey(2)
            session.findById("wnd[0]/tbar[1]/btn[40]").press()
            session.findById("wnd[0]/usr/lbl[53,12]").setFocus()
            session.findById("wnd[0]/usr/lbl[53,12]").caretPosition = 0
            session.findById("wnd[0]").sendVKey(2)
            message2=session.findById("wnd[0]/sbar").text
            print(message2)
            if message2=="No list exists":
               time.sleep(2)
               session.findById("wnd[0]").HardCopy(f"{sub_dir}\{cf}_SpoolError.png", 1)
               return {"error":4,"message":message2,"ttype":"Spool"}
         except:
            try:
               ### For All Systems except LPP and RBP ###
               session.findById("wnd[0]/usr/lbl[80,10]").setFocus()
               session.findById("wnd[0]/usr/lbl[80,10]").caretPosition = 5
               session.findById("wnd[0]").sendVKey(2)
            except:
               ### For RBP ###
               session.findById("wnd[0]/usr/lbl[72,10]").setFocus()
               session.findById("wnd[0]/usr/lbl[72,10]").caretPosition = 5
               session.findById("wnd[0]").sendVKey(2)
            session.findById("wnd[0]/tbar[1]/btn[40]").press()
            session.findById("wnd[0]/usr/lbl[37,12]").setFocus()
            session.findById("wnd[0]/usr/lbl[37,12]").caretPosition = 0
            session.findById("wnd[0]").sendVKey(2)
            message2=session.findById("wnd[0]/sbar").text
            print(message2)
            if message2=="No list exists":
               time.sleep(2)
               session.findById("wnd[0]").HardCopy(f"{sub_dir}\{cf}_SpoolError.png", 1)
               return {"error":4,"message":message2,"ttype":"Spool"}
         try:
            session.findById("wnd[0]/usr/lbl[14,3]").setFocus()
            session.findById("wnd[0]/usr/lbl[14,3]").caretPosition = 0
            session.findById("wnd[0]").sendVKey(2)            
            session.findById("wnd[0]").sendVKey(71)
            for j in dt:
               session.findById("wnd[1]/usr/txtRSYSF-STRING").text = j
               session.findById("wnd[1]").sendVKey(0)
               session.findById("wnd[2]").HardCopy(f"{sub_dir}\{cf+j}.png", 1)
               session.findById("wnd[2]").close()

            session.findById("wnd[1]").close()
            session.findById("wnd[0]/tbar[1]/btn[48]").press()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[1]/usr/ctxtDY_PATH").text = sub_dir#"C:\\Users\\el9fq8580\\Desktop\\VSCode\\CertificatesCheck\\text_report\\"
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = cf+".txt"
            session.findById("wnd[1]/tbar[0]/btn[11]").press()
            
         except Exception as e:
            message=f"Error in 'Graphical view of spool list' in {cf} System"
            print({message:e})
            session.findById("wnd[0]").HardCopy(f"{sub_dir}\{cf}_Error.png", 1)
            return {"error":4,"message":message,"ttype":"Spool"}
         
   except Exception as e:
      message=f"Error in 'Job Overview Layout' in {cf} System"
      print({message:e})
      session.findById("wnd[0]").HardCopy(f"{sub_dir}\{cf}_Error1.png", 1)
      return {"error":4,"message":message,"ttype":"Layout"}
   return {"error":1,"message":"Success","ttype":"NA"}

## Function for Logging off SAP Session ##
def logof(session):
   try: 
      session.findById("wnd[0]/tbar[0]/okcd").text = "/nex"
      session.findById("wnd[0]").sendVKey(0)
      #   session.findById("wnd[0]/tbar[0]/okcd").text = "/nex"
      #   session.findById("wnd[0]").sendVKey(0)
      print("Logged off")
      return 0
   except Exception as e:
      print({"LogOff Error":e})
      return "Error in LogOff"

if __name__ == "__main__":
   import os
   import sys
   stamp=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
   path=os.getcwd()+f"//excel_data//AutoSAP_{stamp}//"
   os.mkdir(path)
   sys.stdout = open(path+"LOG"+stamp+".txt", "w")
    ## Function to call all the required functions and process ##
   import logon
   #sid={"RBQ": "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
   # ,"RWQ": "4.5 - RWQ - SAP BW Informal System",}
   fi= open("cred.txt",'r')
   id= fi.readline().strip()
   passs= fi.readline().strip()

   start=time.time()
   import json
   f=open('sys.txt','r')
   syst=f.read()
   sid=json.loads(syst)
   f.close()
   output_dict={}
   for i in sid:
      session=logon.Autosap(sid[i])      
      try:
         output_dict[i]=tcode(session=session,cf=i,folder=path)
      except Exception as e:
         print({"Error in calling tcode function":e})
      print(logof(session))
   end=time.time()
   run_time=round(end-start)
   print("Output Dictionary :",output_dict)
   ht=report.report(path,list(sid.keys()),run_time,output_dict)
      # print(cc_mail.ccmail(fpath,list(sid.keys())))
   import sender
   frm =  "noreply-autosapautomation@gsk.com"
   subject=f"[Green] AutoSAP Certificates Check Monitoring {stamp} GMT"
   to= ["ITTCSESAT@gsk.com"]
   cc =  ["anil.x.reddy@gsk.com","preetham.x.aranha@gsk.com","hareesh.x.s@gsk.com","shiva.x.prasad@gsk.com","akash.2.verma@gsk.com","vishnuvardhan.x.kalicheti@gsk.com"]
   bdy="test mail"
   file_path=path
   html=ht
   sender.send_mail(send_from=frm, send_to=to, send_cc=cc, subject=subject, text='NA', path=path,html=ht)
            
               

      # connect(path,sid)
         