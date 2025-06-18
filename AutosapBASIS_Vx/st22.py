# ****************************************************************************
#  Program Description : Script Performs ST22 T-Code Action in SAP           *
#  Program Name:  AutosapBASIS\st22.py                                       *
#          Date:  21/06/2024                                                 *
#       version:  1.0.0                                                      *
#        Author:  Erry Lavakumar                                             *
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

def st22(nos=0,session=0,path=0,stamp=0):
    try:
        print("\n##### ST22 #####")
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nst22"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/btnTODAY").press()
        message1=session.findById("wnd[0]/sbar").text
        print(message1)
        import time
        if message1=="No short dumps match the selection criteria":
            time.sleep(2)
            name=f'{path}/{nos} ST22 {stamp}.png'
            session.findById("wnd[0]").HardCopy(name, 1)
            print("ST22 : File/Screenshot Saved Successfully!!")
            return {'value':0,'status':'Green'}
        session.findById("wnd[0]/usr/cntlRSSHOWRABAX_ALV_100/shellcont/shell").setCurrentCell(-1,"ERRORID")
        session.findById("wnd[0]/usr/cntlRSSHOWRABAX_ALV_100/shellcont/shell").selectColumn("ERRORID")
        session.findById("wnd[0]/usr/cntlRSSHOWRABAX_ALV_100/shellcont/shell").pressToolbarContextButton("&MB_FILTER")
        session.findById("wnd[0]/usr/cntlRSSHOWRABAX_ALV_100/shellcont/shell").selectContextMenuItem("&FILTER")
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = "TIME_OUT"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").caretPosition = 8
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/usr/cntlRSSHOWRABAX_ALV_100/shellcont/shell").pressToolbarContextButton("&MB_EXPORT")
        session.findById("wnd[0]/usr/cntlRSSHOWRABAX_ALV_100/shellcont/shell").selectContextMenuItem("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        name1=f"{nos} ST22_TimeOut Dumps.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 12
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        import pandas as pd
        df=pd.read_html(path+name1,header=0)[0]
        dumps_count=len(df.index)
        print("Dumps Count :", dumps_count)
        if dumps_count <200:
            status='Green' 
        elif dumps_count>=200 and dumps_count<=340:
            status='Amber' 
        else:
            status='Red'
        return {'value':dumps_count,'status':status}
    
    except Exception as e:
        print({'Error in ST22':e})
        return {'value':'Nan','status':'Check Manually'}

if __name__ =="__main__":
    # sid={"SBP":"0.1 - R/3 Production"}
    sid = {"SBT":"1.2 - R/3 Acceptance [Informal Testing]"}
    import os
    import logon
    from datetime import datetime
    session=logon.Autosap(sid['SBT'])
    nos=0
    now=datetime.now()
    stamp=now.strftime("%Y-%m-%d-%H-%M-%S")
    cd=os.getcwd()
    path = cd + f'/excel data/AutoSAP_{stamp}/'
    print(st22(nos=0,session=session,path=path,stamp=stamp))
    # print(st06(nos=0,session=session,path=path,stamp=stamp,sid='SBP'))