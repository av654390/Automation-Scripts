# ****************************************************************************
#  Program Description : downloads the dumps report from st22T-code           *
#  Program Name:  AutosapRBP&RWP/st22.py                                      *
#          Date:  08/05/2024                                                  *
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
#  1           Developer      Nikhil Chalikwar  nikhil.x.chalikwar@gsk.com     *
#  2           Developer      Erry Lavakumar    erry.8.lavakumar@gsk.com       *  
#  3           Developer      Akoju Sharanya    akoju.x.sharanya@gsk.com       *  
# ****************************************************************************

def st22(nos=0, session=0, stamp=0, path=0, sid=0):
    try:
        import datetime
        import os
        import pytz
        from datetime import timedelta
        if not os.path.exists(path):
            os.makedirs(path)
        tz = pytz.timezone('GMT')
        current_time = datetime.datetime.now(tz=tz)
        one_hour_ago_hours_ago = current_time - timedelta(hours=1)

        # Format dates and times
        start_date = one_hour_ago_hours_ago.strftime("%d.%m.%Y")
        end_date = current_time.strftime("%d.%m.%Y")
        start_time = one_hour_ago_hours_ago.strftime("%H:%M:%S")
        end_time = current_time.strftime("%H:%M:%S")

        print(f"Start Date: {start_date}, Start Time: {start_time}")
        print(f"End Date: {end_date}, End Time: {end_time}")

        session.findById("wnd[0]/tbar[0]/okcd").text = "/nst22"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtS_DATUM-LOW").text = start_date
        session.findById("wnd[0]/usr/ctxtS_DATUM-HIGH").text = end_date
        session.findById("wnd[0]/usr/ctxtS_UZEIT-LOW").text = start_time
        session.findById("wnd[0]/usr/ctxtS_UZEIT-HIGH").text = end_time
        session.findById("wnd[0]/usr/txtS_UNAME-LOW").text = "*"
        session.findById("wnd[0]/usr/txtS_UNAME-LOW").setFocus()
        session.findById("wnd[0]/usr/txtS_UNAME-LOW").caretPosition = 1
        session.findById("wnd[0]/usr/btnSTARTSEL").press()
        message1=session.findById("wnd[0]/sbar").text
        print(message1)
        import time
        if message1=="No short dumps match the selection criteria":
            time.sleep(2)
            name=f'{path}/{nos} [{sid}] Dumps {stamp}.png'
            session.findById("wnd[0]").HardCopy(name, 1)
            return {'Sum':0,'status':'Green'}
        session.findById("wnd[0]/usr/cntlRSSHOWRABAX_ALV_100/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
        session.findById("wnd[0]/usr/cntlRSSHOWRABAX_ALV_100/shellcont/shell").selectContextMenuItem ("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        name1 = f"{nos} [{sid}] st22dumps {stamp}.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        import pandas as pd
        df=pd.read_html(path+name1,header=0)[0]
        dumps_count=len(df.index)
        return{"Sum" : dumps_count, "message": f"Success in system {sid}"}
    except Exception as e:
        return {"error": 0, "message": f"An error occurred in : {e}"}


# def st22(nos=0,session=0,stamp=0,path=0,sid=0):
#     try:
#         import datetime
#         import os
#         # Get today's date
#         today_date = datetime.datetime.now().strftime("%d.%m.%Y")
#         # Calculate the time range for the last 3 hours
#         current_time = datetime.datetime.now()
#         low_time = (current_time - datetime.timedelta(hours=1)).strftime("%H:%M:%S")
#         print(low_time)
#         high_time = current_time.strftime("%H:%M:%S")
#         print(high_time)
#         session.findById("wnd[0]/tbar[0]/okcd").text = "/nst22"
#         session.findById("wnd[0]").sendVKey (0)
#         session.findById("wnd[0]/mbar/menu[2]/menu[1]").select()
#         session.findById("wnd[0]/usr/ctxtS_DATUM-LOW").text = today_date
#         #session.findById("wnd[0]/usr/ctxtS_DATUM-HIGH").text = today_date
#         # session.findById("wnd[0]/usr/ctxtS_UZEIT-LOW").text = low_time
#         # session.findById("wnd[0]/usr/ctxtS_UZEIT-HIGH").text = high_time
#         session.findById("wnd[0]/usr/ctxtS_UZEIT-HIGH").setFocus()
#         session.findById("wnd[0]/tbar[1]/btn[8]").press()
#         session.findById("wnd[0]/mbar/menu[3]/menu[5]/menu[2]/menu[2]").select()
#         #session.findById("wnd[0]/mbar/menu[3]/menu[5]/menu[2]/menu[1]").select()
#         session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
#         session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
#         session.findById("wnd[1]/tbar[0]/btn[0]").press()
#         session.findById("wnd[1]/usr/ctxtDY_PATH").text = path 
#         session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = f"{nos} [{sid}] st22dumps {stamp}.html"
#         session.findById("wnd[1]/tbar[0]/btn[11]").press()
    #     import pandas as pd
    #     f= pd.read_html(f"{path}/{nos} [{sid}] st22dumps {stamp}.html",header=1)[0]
    #     a=[]
    #     for i in f['Runtime\xa0Errors Number']: 
    #         j = str(i).split()
    #         #print(j)
    #         if j[-1].isdigit(): 
    #             a.append(int(j[-1]))  # Convert it to an integer and append to the list
    #     total_sum = sum(a)
    #     #print("Extracted Numbers:", a)
    #     #return("Sum of Numbers:", total_sum)
    #     #return {"error": 0, "message": f"Success in system {system_id}", "Sum": total_sum}
    #     return {"Sum": total_sum, "message": f"Success in system {sid}"}
    # except Exception as e:
    #     return {"error": 0, "message": f"An error occurred in : {e}"}

if __name__ == "__main__":
    try:
        import os
        import datetime
        import logon
        import sender

        stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        sid = {
            "rbp": "1.1 - RBP - SAP ERP 6.0(R/3) System"
            # "RBQ": "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System",
            # "RWQ": "4.5 - RWQ - SAP BW Informal System",
            # "RAQ": "4.6 - RAQ - SAP SCM(APO) Informal System",
            # "BIT": "2.2 - BW Test [Informal Testing]"

        }

        nos = 1
        path = os.getcwd() + f"\excel data\\autosap {stamp}\\"
        
        # File download section
        try:
            for system_id in sid:
                session = logon.Autosap(sid[system_id])
                print(st22(nos=nos, session=session, sid=system_id, stamp=stamp, path=path))
                print(logon.logof(session))
                nos += 1
        except Exception as e:
            print(f"Error during file download: {e}")

            
    except Exception as e:
        print(f"General error: {e}")
  