## Filtering function ##
def filter(session,fil):
    try:
        session.findById("wnd[0]/usr/sub/1[0,0]/sub/1/3[0,6]/lbl[10,7]").setFocus()
        session.findById("wnd[0]/usr/sub/1[0,0]/sub/1/3[0,6]/lbl[10,7]").caretPosition = 0
        session.findById("wnd[0]").sendVKey(2)
        session.findById("wnd[0]/mbar/menu[1]/menu[3]").select()
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = "@5W\QSHOW AGENT...@"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").caretPosition = 19
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/usr/sub/1[0,0]/sub/1/3[0,6]/lbl[16,7]").setFocus()
        session.findById("wnd[0]/usr/sub/1[0,0]/sub/1/3[0,6]/lbl[16,7]").caretPosition = 1
        session.findById("wnd[0]").sendVKey (2)
        session.findById("wnd[0]/mbar/menu[1]/menu[3]").select()
        
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").text = "@CS\QReady@"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").setFocus()
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").caretPosition = 0
        # session.findById("wnd[1]").sendVKey (4)
        # session.findById("wnd[2]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").text =fil# "@CU\QIn Process@"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").caretPosition = 16
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
    
    except Exception as e:
        print({"Error while filtering Agents":e})

#### Main function ####
def gmm(session,path,stamp,gmmid,uuser):
    try:
        import time
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nse16"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtDATABROWSE-TABLENAME").text = "ZGM_REQUEST"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtI1-LOW").text = gmmid
        session.findById("wnd[0]/usr/ctxtI2-LOW").setFocus()
        session.findById("wnd[0]/usr/ctxtI2-LOW").caretPosition = 0
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        message1=session.findById("wnd[0]/sbar").text
        print(message1)
        if message1=="No table entries found for specified key":
            time.sleep(2)
            errorss='Error_GMMid.png'
            session.findById("wnd[0]").HardCopy(path+errorss, 1)
            return {"error":4,"message":message1,"ttype":"DP"}

        session.findById("wnd[0]/tbar[1]/btn[45]").press()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        name1=f"gmm1_{stamp}.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 8
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        ## Read HTML for ID ##
        import pandas as pd
        f=pd.read_html(path+name1,header=0)[0]
        # print(f)
        #['Cl.', 'Material\xa0Request\xa0Number', 'Material\xa0Request\xa0Number.1', 'Material\xa0Request\xa0Number.2', 'Material', 'MTyp', 'Scenario', 'Wokflow\xa0ID\xa0of\xa0Top-Level\xa0Instance', 'Wokflow\xa0ID\xa0of\xa0Top-Level\xa0Instance.1',
        
        a=[]
        for i in f.index:
            a.append(f['Wokflow\xa0ID\xa0of\xa0Top-Level\xa0Instance'][i])
        try:
            ids=a[1]
            # ids='187892881'
            print(ids)
        except Exception as e:
            print({"No IDs found":e})
            time.sleep(2)
            errorss='Error_IDs.png'
            session.findById("wnd[0]").HardCopy(path+errorss, 1)
            return {"error":4,"message":e,"ttype":"DP"}
        
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nswia"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/txtID-LOW").text = ids
        session.findById("wnd[0]/usr/txtID-LOW").caretPosition = 3
        session.findById("wnd[0]/tbar[1]/btn[8]").press()

        message2=session.findById("wnd[0]/sbar").text   
        print(message2)
        if message2=="No work items exist":
            time.sleep(2)
            errorss='Error_WorkItem.png'
            session.findById("wnd[0]").HardCopy(path+errorss, 1)
            return {"error":4,"message":message1,"ttype":"DP"}

        session.findById("wnd[0]/tbar[1]/btn[44]").press()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text =path # "C:\Users\el9fq8580\Documents\SAP\SAP GUI\"
        name2=f"gmm2_{stamp}.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name2
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 12
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        st="started ready selected waiting"
        nf=pd.read_html(path+name2,header=0)[0]
        #['ID', 'Status', 'Workflow', 'WI\xa0Type', 'Task', 'CreateDate', 'CreateTime', 'Work\xa0item\xa0text', 'Confirm', 'Back', 'Priority', 'DeadlStat', 'Duration', 'Attachm.', 'Persistence\xa0Profile', 'After\xa0Condition', 'Agent', 'Agent.1', 'Administrator', 'Creator', 'EventCompl', 'Workflow.1', 'Attachmnts', 'Forwarded', 'Deadline', 'ActEndTime', 'Done\xa0On', 'Task\xa0text', 'Language']
        status=nf['Status'][0]
        print("Status",status)
        if status.lower() in st:        
            #selecting row
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").currentCellColumn = ""
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectedRows = "0"
            session.findById("wnd[0]/tbar[1]/btn[20]").press()
            if status.lower()=='selected':
                fil="@CT\QReserved@"
            elif status.lower()=='waiting':
                fil="@CW\QWaiting@"
            else:
                fil="@CU\QIn Process@"
            filter(session,fil)
            print("Taking before SS")
            session.findById("wnd[0]/usr/sub/1[0,0]/sub/1/3[0,6]/sub/1/3/4[0,10]/lbl[10,10]").setFocus()
            session.findById("wnd[0]/usr/sub/1[0,0]/sub/1/3[0,6]/sub/1/3/4[0,10]/lbl[10,10]").caretPosition = 0
            session.findById("wnd[0]").sendVKey(2)
            session.findById("wnd[1]/usr/btnB1").press()
            ## Take before screenshot ##
            bfname=f"Before_{stamp}.png"
            session.findById("wnd[1]").HardCopy(path+bfname, 1)
            
            print("Taken before SS")

            session.findById("wnd[1]/tbar[0]/btn[12]").press()
            session.findById("wnd[0]/usr/sub/1[0,0]/sub/1/3[0,6]/sub/1/3/4[0,10]/lbl[19,10]").setFocus()
            session.findById("wnd[0]/usr/sub/1[0,0]/sub/1/3[0,6]/sub/1/3/4[0,10]/lbl[19,10]").caretPosition = 6
            session.findById("wnd[0]").sendVKey(2)
            session.findById("wnd[0]/mbar/menu[1]/menu[0]").select()
            session.findById("wnd[0]/shellcont").dockerPixelSize = 370
            if status.lower()=='waiting':
                session.findById("wnd[0]/shellcont/shell").selectItem("0001","Column2")
                session.findById("wnd[0]/shellcont/shell").ensureVisibleHorizontalItem("0001","Column2")
                session.findById("wnd[0]/shellcont/shell").pressButton("0001","Column2")
            session.findById("wnd[0]/shellcont/shell").selectItem ("0016","Column2")
            session.findById("wnd[0]/shellcont/shell").ensureVisibleHorizontalItem ("0016","Column2")
            session.findById("wnd[0]/shellcont/shell").pressButton ("0016","Column2")
            session.findById("wnd[1]/usr/ctxtPCHDY-SEARK").text = uuser
            session.findById("wnd[1]/usr/ctxtPCHDY-SEARK").caretPosition = 9
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            bar = "Function executed" in session.findById("wnd[0]/sbar").text
            print(bar)
            message3=session.findById("wnd[0]/sbar").text
            if message3=='No values for this selection':
                errorss='Error_user.png'
                session.findById("wnd[0]").HardCopy(path+errorss, 1)
                return {"error":4,"message":"user not found","ttype":"user"}
            
            session.findById("wnd[0]/tbar[0]/btn[3]").press()
            filter(session,fil)
            print("Taking after SS")
            session.findById("wnd[0]/usr/sub/1[0,0]/sub/1/3[0,6]/sub/1/3/4[0,10]/lbl[10,10]").setFocus()
            session.findById("wnd[0]/usr/sub/1[0,0]/sub/1/3[0,6]/sub/1/3/4[0,10]/lbl[10,10]").caretPosition = 0
            session.findById("wnd[0]").sendVKey(2)
            session.findById("wnd[1]/usr/btnB1").press() #after screenshot
            ## Take After screenshot ##

            afname=f"After_{stamp}.png"
            session.findById("wnd[1]").HardCopy(path+afname, 1)
            print("Taken after SS")
            session.findById("wnd[1]/tbar[0]/btn[12]").press()
            session.findById("wnd[0]/tbar[0]/btn[3]").press()#back

        else:
            time.sleep(1)
            errorss='Error_Status.png'
            session.findById("wnd[0]").HardCopy(path+errorss, 1)
            return {"error":4,"message":"Status is not 'Ready'/'Selected'/'Started'","ttype":"DPSTATUS"}
        session.findById("wnd[0]/tbar[0]/btn[3]").press()
        return {"error":3,"message":f"{ bar} in Notification Forward"}

    except Exception as e:
        print({"Error in forwarding":e})
        return {"error":-1,"message":f"Error in gmm forwarding: {e}"}
    

if __name__ == '__main__':
    import logon
    #import cf
    rbq = "2.3 -  [CH] - ECC/R3 QA / Test"
    sid = {"RBQ":rbq}
    import os
    import sys
    import datetime
    now = datetime.datetime.now()
    stamp = now.strftime("%Y-%m-%d-%H-%M-%S")
    curdir = os.getcwd()
    path = curdir+f'/excel_data/AutoSAP_{stamp}/'
    os.makedirs(os.path.dirname(path),exist_ok=True)
    sys.stdout = open(path+"LOG"+stamp+".txt", "w")
    print("""#######################################################################
                                        #
#######################################################################""")

    gmmid='1102200'#"1608901"
    uuser="as58d4927"#'xas'#"el9fq8580"
    session=logon.Autosap(rbq)
    print(gmm(session,path,stamp,gmmid,uuser))
    print(logon.logof(session))
