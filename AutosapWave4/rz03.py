# ****************************************************************************
#  Program Description : Script for rz03 tcode                               *
#  Program Name:  \rz03.py                                                *
#          Date:  08/05/2024                                                 *
#       version:  1.0.0                                                      *
#        Author:  Sharanya Akoju                                             *
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

def rz03(nos=1,session=0,stamp=0,path=0,sid=0):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nrz03"
        session.findById("wnd[0]").sendVKey (0)
        try :
            session.findById("wnd[1]").close()
        except Exception as e :
            print(f"{e} causion window did not came in RZ03")
        if sid.lower() in 'sbp or aup': # for SBP and AUP
            #session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[0]/mbar/menu[5]/menu[5]/menu[2]/menu[1]").select()
        elif sid.lower() in 'ttp':
            session.findById("wnd[0]/mbar/menu[5]/menu[5]/menu[2]/menu[2]").select()
            # session.findById("wnd[0]/mbar/menu[5]/menu[5]/menu[2]/menu[2]").select()
        
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path#"C:\Users\as776099\OneDrive - GSK\Documents\SAP\SAP GUI\"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = f"{nos} [{sid}] rz03 {stamp}.html"#"rz03.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        import pandas as pd
        a=path+ f"//{nos} [{sid}] rz03 {stamp}.html"
        df=pd.read_html(a,header=2)[0]
        AS= df[df["Status"]=="Active"]  # Filter the DataFrame to select rows where the status is "Active"
        num_AS=AS.shape[0]   # Count the number of active servers
        #return num_AS
        return {"ActiveServers": num_AS}
    except Exception as e:
        return {"error": 0, "message": f"An error occurred in rz03: {e}"}


if __name__ == "__main__":
    try:
        import os
        import datetime
        import logon

        stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        sid = {
            "WMV": "A.1 - eWM Validation [Formal Testing]",
            "BIV": "2.1 - BW Validation [Formal Testing]",
            #"HRV": "7.1 - HR Validation [Formal Testing]"
            
        }


        nos = 1
        path = os.getcwd() + f"\excel data\\autosap {stamp}\\"

        # File download section
        try:
            for system_id in sid:
                session = logon.Autosap(sid[system_id])
                print(rz03(nos=nos, session=session, sid=system_id, stamp=stamp, path=path))
                print(logon.logof(session))
                nos += 1
        except Exception as e:
            print(f"Error during file download: {e}")

    except Exception as e:
        print(f"General error: {e}")


