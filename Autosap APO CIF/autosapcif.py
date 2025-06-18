# ****************************************************************************
#  Program Description : Script checks cif jobs                              *
#  Program Name:  CIF\autosapcif.py                                      *
#          Date:  08/05/2024                                                 *
#       version:  1.0.0                                                      *
#        Author:  Nikhil Chalikwar                                           *
#  Return Codes:                                                             *
#                 0 - Success                                                *
#                 1 - Error check log file                                   *
# ****************************************************************************
#  AutoSAP Automation                                                        *
#  --------------------                                                      *
#  Sr.         Role           Member          Email                          *
#  ---------   ----------     --------------  -------------------------------*
#  1           Developer      NIKHIL CHALIKWAR  nikhil.x.chalikwar@gsk.com   *
#  2           Developer      erry lavakumar    erry.8.lavakumar@gsk.com     *  
#  2           Developer      akoju sharanya    akoju.x.sharanya@gsk.com     *  
#                                                                            *
# ****************************************************************************
#Step 1 (function 'cif' in 'cif.py' file): Checks the CIF jobs and downloads the report
#Step 2 (function 'fins' in 'cif.py' file):Captures if all the jobs have 'Finished' Status
#Step 3 (function 'cans' in 'cif.py' file): Captures if any job has 'Cancelled' Status
#Step 4 (function 'sender' in 'cifsender1.py' file):Sends the Alert mail to APO team 
## This loop will execute until and unless all the jobs status is equal to 'Finished' ##

import os
import time
import datetime,pytz
import sys

 
# tz=pytz.timezone('Asia/Kolkata')
# tz=pytz.timezone('UTC')
tz=pytz.timezone('CET')
now=datetime.datetime.now(tz=tz)
stamp=now.strftime("%Y-%m-%d-%H-%M-%S")
SBP = "0.1 - R/3 Production"
stamp=now.strftime("%Y-%m-%d")#stamp = str(time.time())
path = os.getcwd() + f'\excel_data\\AutoSAP_{stamp}\\'
# os.mkdir(path)
os.makedirs(os.path.dirname(path), exist_ok=True)
sys.stdout = open(path+"LOG"+stamp+".txt", "w")
print("""#######################################################################

#######################################################################""")

import cif
import logon
import sender
stamp = datetime.datetime.now(tz=tz).strftime("%Y-%m-%d-%H-%M-%S")

job = "z_*_APO_D_CIF_DELTA"
users="*"
# job = "ARFC:0A6D03206676663B53D400F7"
# users="MM043578"
# todayjob= now.strftime("%d.%m.%Y")
# today4pm=now.replace(hour=18, minute=0, second=0, microsecond=0)
session = logon.Autosap(SBP)
today=now.strftime("%d.%m.%Y")#"06.09.2024"
# temp =cif.cif(session,path,stamp,fd=today,td=today,job=job,users=users)
# print(temp)
frm =  "noreply-autosapautomation@gsk.com"
to= ["TCS_GLOBAL_ERP_APO_L2@gsk.com","GLOBALERP_APO_L3@gsk.com","aswin.x.johncherian@gsk.com","saimanjusha.x.sajja@gsk.com","harishankarramakanth.x.pallam@gsk.com","arvind.x.suganathan@gsk.com","chandi.x.venkatesh@gsk.com","saugata.x.bhatnagar@gsk.com","nikhita.x.adari@gsk.com","penchalaiah.x.velagacherla@gsk.com","sachin.x.gurushantanavar@gsk.com"]
cc =  ["preetham.x.aranha@gsk.com","hareesh.x.s@gsk.com","akoju.x.sharanya@gsk.com","erry.8.lavakumar@gsk.com"]
subject=f"[FYI] AutoSAP CIF job monitoring {stamp} CET"
bdy="test mail"
flag0=1
# if all(i=='Schedule' or i=='Released' for i in temp["value"]):
#     # print(fins(session,path,name1))
#     print(temp["value"])
#     sender.send_mail(send_from=frm, send_to=to, send_cc=cc, subject=subject, text=bdy, files=path,html=r"cif_s.html")
# if any(i=='Canceled' for i in temp["value"]):
#     # print(fins(session,path,name1))
#     print(temp["value"])
#     subject="[RED] AutoSAP CIF job monitoring"
#     html=r"cif_c.html"
#     sender.send_mail(send_from=frm, send_to=to, send_cc=cc, subject=subject, text=bdy, files=path,html=html)
# if all(i=="Finished" for i in temp["value"]):
#     subject="[GREEN] AutoSAP CIF job monitoring"
#     # print(fins(session,path,name1))
#     print(temp["value"])
#     sender.send_mail(send_from=frm, send_to=to, send_cc=cc, subject=subject, text=bdy, files=path,html=r"cif_f.html")
# # # if temp["status"]=="Schedule":
#     # pass
try:
    while 1:
        if "<class 'win32com.client.CDispatch'>"!=str(type(session)):
            session = logon.Autosap(SBP)
        print("----------------------------------------------------------------------")
        temp =cif.cif(session,path,stamp,fd=today,td=today,job=job,users=users)
        print(temp)
        print("----------------------------------------------------------------------")
        if temp['status']=="nojob" :
                subject=f"[Attention no job found] AutoSAP CIF job monitoring {stamp} CET"
                # if flag0 ==0 : print(temp["value"])
                sender.send_mail(send_from=frm, send_to=to, send_cc=cc, subject=subject, text=bdy, files=path,html=r"cif_s.html")
                break
        if flag0 and temp['status']=="ScheduleorReleased" :
                # if flag0 ==0 : print(temp["value"])
                sender.send_mail(send_from=frm, send_to=to, send_cc=cc, subject=subject, text=bdy, files=path,html=r"cif_s.html")
                flag0=0
        if temp['status']=="Active":
            pass
        if temp['status']=="Canceled":
            print(temp["value"])
            subject=f"[RED] AutoSAP CIF job monitoring {stamp} CET"
            html=r"cif_c.html"
            sender.send_mail(send_from=frm, send_to=to, send_cc=cc, subject=subject, text=bdy, files=path,html=html)
        if temp['status']=="Finished":
            print(temp["value"])
            subject=f"[GREEN] AutoSAP CIF job monitoring {stamp} CET"
            html=r"cif_f.html"
            sender.send_mail(send_from=frm, send_to=to, send_cc=cc, subject=subject, text=bdy, files=path,html=html)
            break
        if temp['status']=="other":
            print(temp["value"])
            subject=f"[RED CRITICAL] AutoSAP CIF job monitoring automation error {stamp} CET"
            html=r"cif_er.html"
            sender.send_mail(send_from=frm, send_to=to, send_cc=cc, subject=subject, text=bdy, files=path,html=html)
        time.sleep(1200) #20 mins

    print(logon.logof(session))
    print("finished !!!")

except Exception as e:
    print({'Error in Automation (while loop)':e})

finally :
    sys.stdout.close() 
# if output['Status']=='Green':
#     sub=f'Green:AutoSAP CIF job monitoring {stamp }'
# else:
#     sub=f'Red:AutoSAP CIF job monitoring {stamp }'
# print(cifsender.sender(path,output,sub,today))

#['No.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#['No.', 'Program\xa0name/command', 'Prog.\xa0type', 'Spool\xa0list', 'Parameters', 'User', 'Lang.', 'Start\xa0date', 'Start\xa0At', 'End\xa0date', 'End\xa0time', 'Status', 'Duration(sec.)']
# ['Program\xa0name/command', 'RIMODGEN', 'RIMODAC2', 'RIMODGEN', 'RIMODAC2', 'RIMODGEN', 'RIMODAC2', 'RIMODGEN', 'RIMODAC2', 'RIMODGEN', 'RIMODAC2', 
# 'RIMODGEN', 'RIMODAC2', 'RIMODGEN', 'RIMODAC2', 'RIMODGEN', 'RIMODAC2', 'CUSLNTRTO_CIF_REPORT', 'CUSLNTRTO_CIF_REPORT', 'RIMODGEN', 'RIMODAC2', 'RIMODGEN', 'RIMODAC2', 'RIMODGEN', 'RIMODAC2', 'RIMODGEN', 'RIMODAC2', 'RIMODGEN', 'RIMODAC2', 'RIMODGEN', 'RIMODAC2', 'RIMODGEN', 'RIMODAC2', 'RIMODGEN', 'RIMODAC2', 'RCPTRAN4', 'RIMODDEL']
#   cancelled_jobs = g[g['Status'] == 'Canceled']
        # cancelled_job_names = cancelled_jobs['JobName']

        # for job_name in cancelled_job_names:
        #     print("The JobName is:", job_name)



        # df="df"


        # d={}

        # for in df :
        #     if i[]=="cancellted":
        #         d[]="cancelled"

        # if cancelled in d:
    # if text!=str(output):
    #     new_status=open(filename,'w')
    #     new_status.write(str(output))
    #     if 'Canceled' in output.values():
    #         for k,v in output.items():
    #             if v=='Canceled':
    #                 data.append(k)
    #         nstamp=now.strftime("%Y-%m-%d-%H-%M-%S")#stamp = str(time.time())
    #         sub=f'RED: AutoSAP CIF job monitoring {nstamp} UTC'
    #         print(f"'Canceled' Status found for job-{data} at {nstamp} UTC")
    #         print(cifsender1.sender(path,data,sub,today))
            
    #     elif all(i=='Finished' for i in output.values()):
    #         nstamp=now.strftime("%Y-%m-%d-%H-%M-%S")#stamp = str(time.time())
    #         sub=f'Green:AutoSAP CIF job monitoring {nstamp} UTC'
    #         print(f"Status of all Jobs are 'Finished' at {nstamp} UTC")
    #         print(cifsender1.sender(path,data,sub,today))
    #         exit()
    # else:
    #     nstamp=now.strftime("%Y-%m-%d-%H-%M-%S")#stamp = str(time.time())
    #     print(f"The status is same at {nstamp} UTC")