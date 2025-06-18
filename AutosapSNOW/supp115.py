# print("""#######################################################################
                                              #
# #######################################################################""")
def filter(session,fil):
    try:
        # session.findById("wnd[0]/usr/lbl[13,7]").setFocus()
        session.findById("wnd[0]/usr/sub/1[0,0]/sub/1/3[0,6]/lbl[10,7]").setFocus()
        session.findById("wnd[0]/usr/sub/1[0,0]/sub/1/3[0,6]/lbl[10,7]").caretPosition = 1
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
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").text =fil # "@CU\QIn Process@"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").caretPosition = 16
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
    
    except Exception as e:
        print({"Error while filtering Agents":e})


def sup(session,path,stamp,supid,uuser):
    try:
        import time
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nse16"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtDATABROWSE-TABLENAME").text = "zslm_req_track"
        session.findById("wnd[0]/usr/ctxtDATABROWSE-TABLENAME").caretPosition = 14
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/txtI1-LOW").text = supid#"SUP000000024252"
        session.findById("wnd[0]/usr/txtI1-LOW").caretPosition = 15
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        # session.findById("wnd[1]/tbar[0]/btn[0]").press()
        message1=session.findById("wnd[0]/sbar").text
        print(message1)
        if message1=="No table entries found for specified key":
            time.sleep(2)
            errorss='Error_suppl_id.png'
            session.findById("wnd[0]").HardCopy(path+errorss, 1)
            return {"error":4,"message":message1,"ttype":"DP"}
        session.findById("wnd[0]/mbar/menu[6]/menu[5]/menu[2]/menu[2]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path #"C:\Users\el9fq8580\Documents\SAP\SAP GUI\"
        name1=f"supp1_{stamp}.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1#"sup1.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        # session.findById("wnd[0]/tbar[1]/btn[45]").press()
        # session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        # session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        # session.findById("wnd[1]/tbar[0]/btn[0]").press()
        # session.findById("wnd[1]/usr/ctxtDY_PATH").text = path #"C:\Users\el9fq8580\Documents\SAP\SAP GUI\"
        # name1=f"supp1_{stamp}.html"
        # session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1 #"supl1.html"
        # session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 10
        # session.findById("wnd[1]/tbar[0]/btn[11]").press()

        #Read Data
        import pandas as pd
        f=pd.read_html(path+name1,header=0)[0]
        try:
            try:
                ids=f['Wokflow\xa0ID\xa0of\xa0Top-Level\xa0Instance.1'][0]
                print('IDs',ids)
            except:
                ids=f['TOP_WI_ID'][0]
                print('IDs',ids)
        except Exception as e:
            print({"No IDs found":e})
            time.sleep(2)
            errorss='Error_IDs.png'
            session.findById("wnd[0]").HardCopy(path+errorss, 1)
            return {"error":4,"message":e,"ttype":"DP"}

        session.findById("wnd[0]/tbar[0]/okcd").text = "/nswia"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/txtID-LOW").text =str(ids) #"1988351"
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
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path #"C:\Users\el9fq8580\Documents\SAP\SAP GUI\"
        name2=f"supp2_{stamp}.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name2 #"supl2.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 10
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        g=pd.read_html(path+name2,header=0)[0] 
        st="started ready selected waiting"   
        status=g['Status'][0]
        print("Workflow Status:",status)
        if status.lower() in st:
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
            session.findById("wnd[0]/usr/sub/1[0,0]/sub/1/3[0,6]/sub/1/3/4[0,10]/lbl[19,10]").caretPosition = 8
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
            try:
                session.findById("wnd[1]/usr/btnSPOP-VAROPTION2").press()
            except:
                pass
            bar = "Function executed" in session.findById("wnd[0]/sbar").text
            print(bar)
            message3=session.findById("wnd[0]/sbar").text
            print(message3)
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
        print({'Error in sup':e})
        return {"error":-1,"message":f"Error in gmm forwarding: {e}"}


if __name__ == '__main__':
    import logon
    #import cf
    rbq = "2.3 -  [CH] - ECC/R3 QA / Test"
    slq= "2.8 -  [CH] - SAP SLM BUY QA / Test"
    sid = {"SLQ":slq}
    import os
    import sys
    import datetime
    now = datetime.datetime.now()
    stamp = now.strftime("%Y-%m-%d-%H-%M-%S")
    curdir = os.getcwd()
    path = curdir+f'/excel_data/AutoSAP_{stamp}/'
    os.makedirs(os.path.dirname(path),exist_ok=True)
    sys.stdout = open(path+"LOG"+stamp+".txt", "w")

    # cfid ="1100021150"
    # uuser ="nc92j2918" #"el9fq8580"
    supid='SUP000000024252'#'RCH000000189679'#'RCH000000189673'#"SUP000000024252"
    uuser="as58d4927"#'xas'#"el9fq8580"
    session=logon.Autosap(slq)
    # print(cf(session,path,stamp,cfid,uuser))
    print(sup(session,path,stamp,supid,uuser))
    # print(logon.logof(session))
