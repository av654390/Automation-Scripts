# ****************************************************************************
#  Program Description : Script Performs SM59 T-Code Action in SAP           *
#  Program Name:  AutosapBASIS\sm59.py                                       *
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

def sm59(nos=0,session=0,path=0,stamp=0,sid=0):
    try:
        print("\n##### SM59 #####")
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsm59"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").expandNode("          6")
        session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").topNode = "          1"
        sm59_list=["SEAL-CONNC","SEAL-CONVUTIL","SEAL-CONVUTIL-1","SEAL-CONVUTIL-2","SEAL-CONVUTIL-3","SEAL-VIEW-CKL-CONV00","SEAL-VIEW-CKL-CONV01","SEAL-VIEW-CKL-CONV02","SEAL-VIEW-CKL-CONV03","SEAL-VIEW-CKL-CONV04","SEAL-VIEW00","SEAL-VIEW01","SEAL-VIEW02","SEAL-VIEW03","SEAL-VIEW04","SEAL-VIEW05","SEAL-VIEW06","SEAL-VIEW07","SEAL-VIEW08","SEAL-VIEW09","SEAL-VIEW10","SEAL-VIEW11","SEAL-VIEW12","SEAL-VIEW13","SEAL-VIEW14","SEAL-VIEW15","TREX_TRP"]
        print("Length=",len(sm59_list))
        sm59_dict={}
        for seal in sm59_list:
            session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[0]").pressButton("SEARCH")
            session.findById("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[0,24]").text = seal
            session.findById("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[0,24]").caretPosition = 10
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[1]/usr/lbl[6,3]").setFocus()
            session.findById("wnd[1]/usr/lbl[6,3]").caretPosition = 18
            session.findById("wnd[1]").sendVKey(2)
            session.findById("wnd[0]/tbar[1]/btn[27]").press()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 0
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "0"
            variablename=session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").GetCellValue("0","RESULT")
            print(f"{seal}: {variablename}")
            sm59_dict[seal]=variablename if 'Error' in variablename else 'Ok'
            session.findById("wnd[0]/tbar[0]/btn[3]").press()
            session.findById("wnd[0]/tbar[0]/btn[3]").press()
        print("SM59_dict : ",sm59_dict)
        return sm59_dict
    except Exception as e:
        print({'Error in SM59':e})
        return {0:'Check Manually'}

if __name__ =="__main__":
    # sid={'sbt':"1.2 - R/3 Acceptance [Informal Testing]"}
    # sid={'sbv':"1.1 - R/3 Validation [Formal Testing]"}
    sid = {"SBP":"0.1 - R/3 Production"}
    import os
    import logon
    from datetime import datetime
    session=logon.Autosap(sid['SBP'])
    nos=0
    now=datetime.now()
    stamp=now.strftime("%Y-%m-%d-%H-%M-%S")
    cd=os.getcwd()
    path = cd + f'/excel data/AutoSAP_{stamp}/'
    sm59_dict=sm59(nos=0,session=session,path=path,stamp=stamp,sid='sbv')
    print(sm59_dict)
    # print(sm59_dict[100])
    # logon.logof(session)
