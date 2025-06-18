def filter(session):
    try:
        session.findById("wnd[0]/usr/lbl[13,7]").setFocus()
        session.findById("wnd[0]").sendVKey(2)
        #print("vvvvvvvvv")
        session.findById("wnd[0]/mbar/menu[1]/menu[3]").select()
        session.findById("wnd[1]").sendVKey (4)
        session.findById("wnd[2]/usr/lbl[1,5]").setFocus()
        session.findById("wnd[2]/usr/lbl[1,5]").caretPosition = 0
        session.findById("wnd[2]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = "@5W\QSHOW AGENT...@"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").caretPosition = 19
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        #print("iiiiiiii")
        session.findById("wnd[0]/usr/lbl[19,7]").setFocus()
        session.findById("wnd[0]/usr/lbl[19,7]").caretPosition = 0
        session.findById("wnd[0]").sendVKey (2)
        session.findById("wnd[0]/mbar/menu[1]/menu[3]").select()
        
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").text = "@CS\QReady@"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").setFocus()
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").caretPosition = 0
        session.findById("wnd[1]").sendVKey (4)
        session.findById("wnd[2]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").text = "@CU\QIn Process@"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").caretPosition = 16
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]").HardCopy(f"{path}/before {cfid}.png", 1)
        #filter
        session.findById("wnd[0]/usr/lbl[13,10]").setFocus()
        session.findById("wnd[0]/usr/lbl[13,10]").caretPosition = 0
        session.findById("wnd[0]").sendVKey (2)
        session.findById("wnd[1]/usr/btnB1").press()
    
    except Exception as e:
        print({"Error while flitering agents",e})


def cf(session,path,stamp,cfid,uuser):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nse16"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtDATABROWSE-TABLENAME").text = "ZKN_WF_CUSTOMER"
        session.findById("wnd[0]/usr/ctxtDATABROWSE-TABLENAME").caretPosition = 15
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtI1-LOW").text =  cfid
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        try:
            import time
            message1=session.findById("wnd[0]/sbar").text
            print(message1)
            if message1=="No table entries found for specified key":
                time.sleep(2)
                errorss='Error_cfid.png'
                session.findById("wnd[0]").HardCopy(path+errorss, 1)
                return {"error":4,"message":message1,"ttype":"DP"}
        except Exception as e:
            print("dp found",e) 
        
        #session.findById("wnd[0]/tbar[1]/btn[45]").press()
        session.findById("wnd[0]/mbar/menu[6]/menu[5]/menu[2]/menu[2]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        name1 = f'status_{stamp}.html'
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        #Read html for id# 
        st="STARTED READY SELECTED"
        import pandas as pd
        f=pd.read_html(path+name1,header=0)[0]
        ids=[]
        for i in f.index:
            if f['Status'][i] in st:  #Technical\xa0Status
                ids.append(f['ID'][i])
        print(ids)
        if len(ids)==0:
            #return "No id found with status STARTED READY SELECTED"
            return {"error":4,"message":"No id found with status STARTED READY SELECTED","ttype":"DP"}
    except Exception as e:
        print({'DP numbers not found',e})

    try:
        for id in ids:
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nswia"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/txtID-LOW").text = str(id) #"000511743942"
            session.findById("wnd[0]/tbar[1]/btn[8]").press()
            try:
                import time
                message2=session.findById("wnd[0]/sbar").text
                print(message2)
                if message2=="No work items exist":
                    time.sleep(2)
                    errorss='Error_WorkItem.png'
                    session.findById("wnd[0]").HardCopy(path+errorss, 1)
                    return {"error":4,"message":message2,"ttype":"DPSTATUS"}
            except Exception as e:
                print({"dp status is fine",e})

            session.findById("wnd[0]/tbar[1]/btn[44]").press()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
            name2 = f'cf2_{id}_{stamp}.html'
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name2
            session.findById("wnd[1]/tbar[0]/btn[11]").press()
            g = pd.read_html(path+name2,header=0)[0]
            n=len(g.index)
            print(n)
            d={}
            for k in g.index:
                status=g['Status'][k]
                d[k]=status
            print(d)
            for j in d:
                if d[j].lower() == 'cancelled':
                    return -1
                #elif
                else:
                    session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").currentCellRow = j #click on the currentrow
                    session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectedRows = str(j) #selecting that row
                    session.findById("wnd[0]/tbar[1]/btn[20]").press() #spoollist
                    filter(session)
                    print(j)
            
                    ## Take before screenshot ##
                    bfname=f"Before_{stamp}_{id}.png"
                    session.findById("wnd[1]").HardCopy(path+bfname, 1)
                    session.findById("wnd[1]").close()

                    session.findById("wnd[0]/usr/lbl[22,10]").setFocus()
                    session.findById("wnd[0]/usr/lbl[22,10]").caretPosition = 8
                    session.findById("wnd[0]").sendVKey (2)
                    session.findById("wnd[0]/mbar/menu[1]/menu[0]").select()
                    session.findById("wnd[0]/shellcont/shell").selectItem ("0016","Column2")
                    session.findById("wnd[0]/shellcont/shell").ensureVisibleHorizontalItem ("0016","Column2")
                    session.findById("wnd[0]/shellcont/shell").pressButton ("0016","Column2")
                    try:
                        session.findById("wnd[1]/usr/ctxtPCHDY-SEARK").text = uuser
                        session.findById("wnd[1]/usr/ctxtPCHDY-SEARK").caretPosition = 9
                        session.findById("wnd[1]/tbar[0]/btn[0]").press()
                        session.findById("wnd[0]").HardCopy(f"{path}/action {cfid}.png", 1) #Function Executed
                        bar = "Function executed" in session.findById("wnd[0]/sbar").text
                        print(bar)
                        message3=session.findById("wnd[0]/sbar").text
                        print(message3)
                        if message3==f'No values for this selection':
                            errorss='Error_user.png'
                            session.findById("wnd[0]").HardCopy(path+errorss, 1)
                            return {"error":4,"message":"user not found","ttype":"user"}
                    except Exception as e:
                        print("User not found",e)

                    session.findById("wnd[0]/tbar[0]/btn[3]").press()
                    filter(session)

                    ## Take After screenshot ##
                    afname=f"After_{stamp}_{id}.png"
                    session.findById("wnd[1]").HardCopy(path+afname, 1)
                    session.findById("wnd[1]").close()
                    session.findById("wnd[0]/tbar[0]/btn[3]").press()#back    
            session.findById("wnd[0]/tbar[0]/btn[3]").press()
            return {"error":3,"message":f"{ bar} in Customer Forward"}
    except Exception as e:
        print({"Error in forwarding",e})
        return {"error":-1, "message":f"error in Customer Forwarding(cf) : {e}"}
    return 'done'

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
    cfid ="1100000967"#1200079625"#1200079624"#"1100004909"#1100021150"#"99999999"#"1100004580"#
    uuser ="el491900"#"kt75c0004"#"as58d4927"#"nc92j2918" #"el9fq8580"
    session=logon.Autosap(rbq)
    print(cf(session,path,stamp,cfid,uuser))
    #print(logon.logof(session))