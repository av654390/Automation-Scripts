# ****************************************************************************
#  Program Description : Script for smlg tcode                               *
#  Program Name:  RBP\smlg.py                                                *
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
#  1           Developer      erry lavakumar    erry.8.lavakumar@gsk.com     *  
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
        session.findById("wnd[0]/mbar/menu[4]/menu[5]/menu[2]/menu[2]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path#"C:\Users\as776099\OneDrive - GSK\Documents\SAP\SAP GUI\"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = f"{nos} [{sid}] smlg {stamp}.html"#smlg.html"
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
    import os
    import logon
    import datetime
    rbq= "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    #rbp= "1.1 - RBP - SAP ERP 6.0(R/3) System"
    #rwp= "1.2 - RWP-SAP BW  System"
    session=logon.Autosap(rbq)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    path=os.getcwd()+f"\excel data\\autosap {stamp}\\"
    nos=2
    print(smlg(nos,session,stamp,path))
    #print(logon.logof(session))
