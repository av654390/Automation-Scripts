# ****************************************************************************
#  Program Description : Script for smlg tcode                               *
#  Program Name:  \smlg.py                                                *
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
def smlg(nos=2,session=0,stamp=0,path=0,sid=0):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsmlg"
        session.findById("wnd[0]").sendVKey (0)
        try :
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
        except Exception as e :
            print(e,"table not locked in smlg")
        session.findById("wnd[0]/tbar[1]/btn[5]").press()
        if sid.lower() in 'sbp or aup':
            session.findById("wnd[0]/mbar/menu[4]/menu[5]/menu[2]/menu[1]").select()
        elif sid.lower() in 'ttp':
            session.findById("wnd[0]/mbar/menu[4]/menu[5]/menu[2]/menu[2]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = f"{nos} [{sid}] smlg {stamp}.html"
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        import pandas as pd
        a=path+f"{nos} [{sid}] smlg {stamp}.html"
        df=pd.read_html(a,header=0,na_values=0,decimal=",",thousands=".")
        df=df[0].fillna(0)
        max_response_time = df["Resp.time(ms)"].max()
        return {"Max responsetime":max_response_time}
    except Exception as e:
        return {"error":0,"message":f"in smlg {e}"}

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
                print(smlg(nos=nos, session=session, sid=system_id, stamp=stamp, path=path))
                print(logon.logof(session))
                nos += 1
        except Exception as e:
            print(f"Error during file download: {e}")

    except Exception as e:
        print(f"General error: {e}")

