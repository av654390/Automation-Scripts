def filter(session):
    try:
        #filter
        import time
        session.findById("wnd[0]/usr/lbl[13,8]").setFocus()
        session.findById("wnd[0]/usr/lbl[13,8]").caretPosition = 0
        session.findById("wnd[0]").sendVKey( 2)
        session.findById("wnd[0]/mbar/menu[1]/menu[3]").select()
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = "@5W\QShow agent...@"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").caretPosition = 19
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/usr/lbl[19,8]").setFocus()
        session.findById("wnd[0]/usr/lbl[19,8]").caretPosition = 1
        session.findById("wnd[0]").sendVKey( 2)
        session.findById("wnd[0]/mbar/menu[1]/menu[3]").select()
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").text = "@CS\QReady@"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").text = "@CU\QIn Process@"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").setFocus()
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").caretPosition = 11
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        time.sleep(2)
        session.findById("wnd[0]").HardCopy(f"{path}/before {nfid}.png", 1)
        #filter
        session.findById("wnd[0]/usr/lbl[13,11]").setFocus()
        session.findById("wnd[0]/usr/lbl[13,11]").caretPosition = 0
        session.findById("wnd[0]").sendVKey (2)
        session.findById("wnd[1]/usr/btnB1").press()
    except Exception as e:
        print({"Error while filtering agents",e})

def nf(session,path,stamp,nfid,uuser):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/niqs3"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtRIWO00-QMNUM").text = nfid 
        session.findById("wnd[0]/usr/ctxtRIWO00-QMNUM").caretPosition = 9
        session.findById("wnd[0]").sendVKey (0)
    
        message1=session.findById("wnd[0]/sbar").text  #it will read the last line of SAP page
        if message1 == f'Notification {nfid} does not exist':
            import time
            time.sleep(2)
            errorss='Error_nfid.png'
            session.findById("wnd[0]").HardCopy(path+errorss, 1)
            print(message1)
            return {"error":4,"message":message1,"ttype":"Notificationnumber"}

        session.findById("wnd[0]/titl/shellcont/shell").pressContextButton ("%GOS_TOOLBOX") #click workflow overview and workflow logs and set the status filter
        # session.findById("wnd[1]/usr/tblSAPLSWUGOBJECT_CONTROL").getAbsoluteRow(0).selected = True
        # session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/titl/shellcont/shell").selectContextMenuItem ("%GOS_WF_OVERVIEW")
        #filter
        session.findById("wnd[1]/usr/cntlCONTAINER/shellcont/shell/shellcont[0]/shell").setCurrentCell (-1,"STATUSTEXT")
        session.findById("wnd[1]/usr/cntlCONTAINER/shellcont/shell/shellcont[0]/shell").selectColumn ("STATUSTEXT")
        session.findById("wnd[1]/usr/cntlCONTAINER/shellcont/shell/shellcont[0]/shell").selectedRows = ""
        session.findById("wnd[1]/usr/cntlCONTAINER/shellcont/shell/shellcont[0]/shell").contextMenu()
        session.findById("wnd[1]/usr/cntlCONTAINER/shellcont/shell/shellcont[0]/shell").selectContextMenuItem ("&FILTER")
        session.findById("wnd[2]").sendVKey (4)
        session.findById("wnd[3]/usr/lbl[1,3]").caretPosition = 7
        session.findById("wnd[3]/tbar[0]/btn[0]").press()
        session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = "In Process"
        session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").caretPosition = 10
        session.findById("wnd[2]/tbar[0]/btn[0]").press()
        #excel
        session.findById("wnd[1]/usr/cntlCONTAINER/shellcont/shell/shellcont[0]/shell").contextMenu()
        session.findById("wnd[1]/usr/cntlCONTAINER/shellcont/shell/shellcont[0]/shell").selectContextMenuItem ("&XXL")
        session.findById("wnd[2]/tbar[0]/btn[0]").press()
        session.findById("wnd[2]/usr/ctxtDY_PATH").text = path
        session.findById("wnd[2]/usr/ctxtDY_FILENAME").text = "nf.xlsx"
        session.findById("wnd[2]/usr/ctxtDY_FILENAME").caretPosition = 7
        session.findById("wnd[2]/tbar[0]/btn[11]").press()
        import os
        import time
        name = f'nf_{stamp}.xlsx'
        os.rename(os.path.join(path, "nf.xlsx"), os.path.join(path,name))
        import pandas as pd
        f = pd.read_excel(path+name, engine='openpyxl')
        n=len(f.index)
        if n==0:
            return {"error":4,"message":"No id found with status In Process Ready","ttype":"DP"}
        for i in range(n):
            session.findById("wnd[1]/usr/cntlCONTAINER/shellcont/shell/shellcont[0]/shell").currentCellRow = i
            session.findById("wnd[1]/usr/cntlCONTAINER/shellcont/shell/shellcont[0]/shell").selectedRows = str(i)
            session.findById("wnd[1]/usr/cntlCONTAINER/shellcont/shell/shellcont[0]/shell").currentCellMoved()
            session.findById("wnd[1]/usr/cntlCONTAINER/shellcont/shell/shellcont[0]/shell").pressToolbarButton ("WIFI")

            filter(session)

            bfname=f"Before_{stamp}.png"
            session.findById("wnd[1]").HardCopy(path+bfname, 1)
            session.findById("wnd[1]").close()
            
            session.findById("wnd[0]/usr/lbl[22,11]").setFocus()
            session.findById("wnd[0]/usr/lbl[22,11]").caretPosition = 6
            session.findById("wnd[0]").sendVKey (2)
            session.findById("wnd[0]/mbar/menu[1]/menu[0]").select()
            session.findById("wnd[0]/shellcont/shell").selectItem ("0016","Column2")
            session.findById("wnd[0]/shellcont/shell").ensureVisibleHorizontalItem ("0016","Column2")
            session.findById("wnd[0]/shellcont/shell").pressButton ("0016","Column2")
            
            try:
                session.findById("wnd[1]/usr/ctxtPCHDY-SEARK").text = uuser
                session.findById("wnd[1]/tbar[0]/btn[0]").press()
                time.sleep(2)
                session.findById("wnd[0]").HardCopy(f"{path}/action {nfid}.png", 1) #Function Executed
                bar = "Function executed" in session.findById("wnd[0]/sbar").text
                print(bar)
                message2=session.findById("wnd[0]/sbar").text
                print(message2)
                if message2=='No values for this selection':
                    time.sleep(2)
                    errorss='Error_user.png'
                    session.findById("wnd[0]").HardCopy(path+errorss, 1)
                    return {"error":4,"message":"user not found","ttype":"user"}
            except Exception as e:
                print("User not found",e)
            session.findById("wnd[0]/tbar[0]/btn[3]").press()
           
            filter(session)
        
            afname=f"After_{stamp}.png"
            session.findById("wnd[1]").HardCopy(path+afname, 1)
            session.findById("wnd[1]").close()
            session.findById("wnd[0]/tbar[0]/btn[3]").press()#back
        session.findById("wnd[0]/tbar[0]/btn[3]").press()    
        return {"error":3,"message":f"{ bar} in Notification Forward"}
    except Exception as e:
        print({"Error while forwarding agents",e})
        return {"error":-1, "message":f"error in Notification Forwarding(nf) : {e}"}


   

if __name__ == '__main__':
    import logon
    #import cf
    rbq = "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    sid = {"RBQ":rbq}
    import os
    import datetime
    now = datetime.datetime.now()
    stamp = now.strftime("%Y-%m-%d-%H-%M-%S")
    curdir = os.getcwd()
    path = curdir+f'/excel_data/AutoSAP_{stamp}/'
    os.makedirs(os.path.dirname(path),exist_ok=True)
    nfid="100655144"#"201172430"#"201172427"#"99999999"#"201172332"#"201172360"#
    uuser ="el491900"#"kt75c0004"#"as58d4927" #"nc92j2918"
    session=logon.Autosap(rbq)
    print(nf(session,path,stamp,nfid,uuser))
    #print(logon.logof(session))