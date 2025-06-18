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
        sm59_dict={}
        if sid.lower()=='sbt':
            s=99
        elif sid.lower()=='sbv':
            s=117
        elif sid.lower()=='sbp':
            s=132
        for i in range(s,s+31):
            if i<100:
                session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").selectItem(f"         {i}","&Hierarchy")
                session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").ensureVisibleHorizontalItem(f"         {i}","&Hierarchy")
                session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").doubleClickItem(f"         {i}","&Hierarchy")
                
            elif i in [s+26,s+27,s+28,s+29]:
                continue
            else:
                session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").selectItem(f"        {i}","&Hierarchy")
                session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").ensureVisibleHorizontalItem(f"        {i}","&Hierarchy")
                session.findById("wnd[0]/usr/cntlSM59CNTL_AREA/shellcont/shell/shellcont[1]/shell[1]").doubleClickItem(f"        {i}","&Hierarchy")
                
            session.findById("wnd[0]/tbar[1]/btn[27]").press()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellRow = 0
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectedRows = "0"
            variablename=session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").GetCellValue("0","RESULT")
            print(f"V{i}: {variablename}")
            sm59_dict[i]=variablename if 'Error' in variablename else 'Ok'
            session.findById("wnd[0]/tbar[0]/btn[3]").press()
            session.findById("wnd[0]/tbar[0]/btn[3]").press()
        print("SM59_dict : ",sm59_dict)
        return sm59_dict
    except Exception as e:
        print({'Error in SM59':e})
        return {0:'Check Manually'}

if __name__ =="__main__":
    # sid={'sbt':"1.2 - R/3 Acceptance [Informal Testing]"}
    sid={'sbv':"1.1 - R/3 Validation [Formal Testing]"}
    import os
    import logon
    from datetime import datetime
    session=logon.Autosap(sid['sbv'])
    nos=0
    now=datetime.now()
    stamp=now.strftime("%Y-%m-%d-%H-%M-%S")
    cd=os.getcwd()
    path = cd + f'/excel data/AutoSAP_{stamp}/'
    sm59_dict=sm59(nos=0,session=session,path=path,stamp=stamp,sid='sbv')
    print(sm59_dict)
    # print(sm59_dict[100])
    # logon.logof(session)
