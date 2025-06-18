# ****************************************************************************
#  Program Description : Script for sm58 tcode                               *
#  Program Name:  RBP\sm58.py                                                *
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
def sm58(nos=3,session=0,stamp=0,path=0,queue="RBP_AAE",sid=0):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsm58"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/txtBENUTZER-LOW").text = "*"
        session.findById("wnd[0]/usr/ctxtDEST-LOW").text = queue
        session.findById("wnd[0]/usr/ctxtDEST-LOW").setFocus()
        session.findById("wnd[0]/usr/ctxtDEST-LOW").caretPosition = 8
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/mbar/menu[4]/menu[5]/menu[2]/menu[2]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path#"C:\Users\as776099\OneDrive - GSK\Documents\SAP\SAP GUI\"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text =f"{nos} [{sid}] sm58 {stamp}.html" # "sm58.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        import pandas as pd 
        a=path+f"{nos} [{sid}] sm58 {stamp}.html"
        table=pd.read_html(a)[0]
        d=table.to_dict()
        #entries=d[0][0]
        value=int(list(d[0].keys())[0])
        return {"Entries":value,"message":"in sm58"}
    except Exception as e:
        return {"error":0,"message":f"in sm58 {e}"}

if __name__ == "__main__":
    import os
    import logon
    import datetime
    rbq = "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    session=logon.Autosap(rbq)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    nos=3
    path=os.getcwd()+f"\excel data\\autosap {stamp}\\"
    print(sm58(nos,session,stamp,path))
    print(logon.logof(session))