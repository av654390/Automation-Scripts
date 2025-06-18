# ****************************************************************************
#  Program Description : downloads the dumps report from st22T-code           *
#  Program Name:  AutoSAPABAPdumps/st22.py                                    *
#          Date:  30/04/2025                                                  *
#       Version:  1.0.0                                                       *
#        Author:  Sharanya Akoju                                              *
#  Return Codes:                                                              *
#                 0 - Success                                                 *
#                 1 - Error check log file                                    *
# ****************************************************************************
#  AutoSAP Automation                                                         *
#  --------------------                                                       *
#  Sr.         Role           Member           Email                          *
#  ---------   ----------     --------------   ------------------------------ *
#  1           Developer      Erry Lavakumar    erry.8.lavakumar@gsk.com       *  
#  2           Developer      Akoju Sharanya    akoju.x.sharanya@gsk.com       *  
# ****************************************************************************

def st22(nos=0,session=0,system_id=0,stamp=0,path=0):
    try:
        import datetime
        yesterday_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        print("Yesterday's date :", yesterday_date)
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nst22"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/mbar/menu[2]/menu[1]").select()
        session.findById("wnd[0]/usr/ctxtS_DATUM-LOW").text = yesterday_date#"11.08.2024"
        session.findById("wnd[0]/usr/ctxtS_UZEIT-HIGH").setFocus()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        try:
            session.findById("wnd[0]/usr/ctxtS_DATUM-LOW").text = yesterday_date
            session.findById("wnd[0]/usr/ctxtS_DATUM-LOW").caretPosition = 10
            session.findById("wnd[0]/usr/btnSTARTSEL").press()
            message1=session.findById("wnd[0]/sbar").text
            print(message1)
            import time
            if message1=="No short dumps match the selection criteria":
                time.sleep(2)
                name=f'{path}/{nos} [{system_id}] EWAdumps {stamp}.png'
                #name=f'{path}/{nos} [{sid}] Dumps {stamp}.png'
                session.findById("wnd[0]").HardCopy(name, 1)
                return {'Dumps_count':0}
        except:
            # if system_id.lower() == "hrd":
            #     session.findById("wnd[0]/mbar/menu[3]/menu[5]/menu[2]/menu[2]").select()
            # else:
            session.findById("wnd[0]/mbar/menu[3]/menu[5]/menu[2]/menu[1]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[1]/usr/ctxtDY_PATH").text = path 
            name1 = f"{nos} [{system_id}] EWAdumps {stamp}.html"
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1
            session.findById("wnd[1]/tbar[0]/btn[11]").press()
            import pandas as pd
            df = pd.read_html(path+name1,header=1)[0]
            #print(df)
            a=[]
            for i in df['Runtime\xa0Errors Number']: 
                j = str(i).split()
                #print(j)
                if j[-1].isdigit(): 
                    a.append(int(j[-1]))
            total_sum = sum(a)
            #print("Extracted Numbers:", a)
            return {'Dumps_count': total_sum}
            print("Sum of Numbers:", total_sum)
    except Exception as e:
        return {"error": 0, "message": f"An error occurred in : {e}"}

if __name__ == "__main__":
    try:
        import os
        import datetime
        import logon
        import sender

        stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        system_ids = {
            "RBQ": "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System",
            "RWQ": "4.5 - RWQ - SAP BW Informal System",
            "RAQ": "4.6 - RAQ - SAP SCM(APO) Informal System",
            "BIT": "2.2 - BW Test [Informal Testing]"

        }

        nos = 1
        path = os.getcwd() + f"\excel data\\autosap {stamp}\\"
        
        # File download section
        try:
            for system_id in system_ids:
                session = logon.Autosap(system_ids[system_id])
                print(st22(nos=nos, session=session, system_id=system_id, stamp=stamp, path=path))
                print(logon.logof(session))
                nos += 1
        except Exception as e:
            print(f"Error during file download: {e}")

        # Email sending section
        try:
            frm = "noreply-autosapautomation@gsk.com"
            #To = ["akoju.x.sharanya@gsk.com"]
            Cc = ["akoju.x.sharanya@gsk.com"]
            To = ["erry.8.lavakumar@gsk.com","akoju.x.sharanya@gsk.com"]
            sub = f" Autosap EWA Dumps report {stamp} "
            file_path = path 
            html = "bdy.html"
            send_result = sender.send_mail(send_from=frm, send_to=To, send_cc=Cc, subject=sub, text=None, path=file_path, html=html)
            print(send_result)
        except Exception as e:
            print(f"Error during email sending: {e}")
            # Optionally, you can use sys.exit(1) to stop the execution if email sending is critical
            # sys.exit(1)
            
    except Exception as e:
        print(f"General error: {e}")
  