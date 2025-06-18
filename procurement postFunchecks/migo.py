# ****************************************************************************
#  Program Description : Script to read&capture material document dispaly    *
#  Program Name:  Procurement Post-Fun Checks\migo.py                        *
#          Date:  02/06/2025                                                 *
#       version:  1.0.0                                                      *
#        Author:  Akoju Sharanya                                             *
#  Return Codes:                                                             *
#                 1 - Success                                                *
#                 0 - Error check log file                                   *
# ****************************************************************************
#  AutoSAP Automation                                                        *
#  --------------------                                                      *
#  Sr.         Role           Member          Email                          *
#  ---------   ----------     --------------  -------------------------------*
#  1           Developer      Akoju Sharanya    akoju.x.sharanya@gsk.com     *  
#                                                                            *
# ****************************************************************************
def migo(no,session,path,stamp,sd,system):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nse16n"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtGD-TAB").text = "EKBE"
        session.findById("wnd[0]/usr/ctxtGD-TAB").caretPosition = 4
        session.findById("wnd[0]").sendVKey (0)
        #session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = "100"
        if system.lower() == "rbp":
            session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,1]").text = "66*"
        elif system.lower() == "sbp":
            session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,1]").text = "445*"
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,6]").setFocus()
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,6]").caretPosition = 0
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC").verticalScrollbar.position = 2
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC").verticalScrollbar.position = 4
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC").verticalScrollbar.position = 5
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,4]").text = "101"
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,5]").text = sd #"04.04.2025"
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,5]").setFocus()
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,5]").caretPosition = 10
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        try:
            import time
            message1=session.findById("wnd[0]/sbar").text
            print(message1)
            if message1=="No values found":
                time.sleep(2)
                errorss=f'{path}/Error[{system}]_MIGO.png'
                session.findById("wnd[0]").HardCopy(errorss, 1)
                #return {"status" : 0, "error" : "No values found in EKBE table for MIGO"}
        except Exception as e:
            print(f"EKBE document id found")

        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem ("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path #"C:\Users\as776099\OneDrive - GSK\Documents\SAP\SAP GUI\"
        name = f'{no}_EKBE_{stamp}.html'
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        #session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").currentCellColumn = "BELNR"
        import os
        import pandas as pd
        file_path = os.path.join(path, name)
        g = pd.read_html(file_path, header=0)[0]
        migo_id = g.loc[0,'Mat.\xa0Doc.']
        migo_id = int(migo_id)
        print({"MIGO_ID" : migo_id})
        
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nmigo"
        session.findById("wnd[0]").sendVKey (0)
        #session.findById("wnd[0]/shellcont/shell/shellcont[1]/shell[1]").topNode = ("          1")
        session.findById("wnd[0]/usr/ssubSUB_MAIN_CARRIER:SAPLMIGO:0003/subSUB_FIRSTLINE:SAPLMIGO:0010/subSUB_FIRSTLINE_REFDOC:SAPLMIGO:2010/txtGODYNPRO-MAT_DOC").text =  migo_id #"5015445430"
        session.findById("wnd[0]/usr/ssubSUB_MAIN_CARRIER:SAPLMIGO:0003/subSUB_FIRSTLINE:SAPLMIGO:0010/subSUB_FIRSTLINE_REFDOC:SAPLMIGO:2010/txtGODYNPRO-MAT_DOC").caretPosition = 10
        session.findById("wnd[0]").sendVKey (0)
        #session.findById("wnd[0]/usr/ssubSUB_MAIN_CARRIER:SAPLMIGO:0003/subSUB_ITEMDETAIL:SAPLMIGO:0301/subSUB_DETAIL:SAPLMIGO:0300/tabsTS_GOITEM/tabpOK_GOITEM_PO_DATA").select()
        ss_migo = f"{path}/{no} [{system}].MIGO - Good Receipt.png"
        session.findById("wnd[0]").HardCopy(ss_migo, 1)
        try:
            session.findById("wnd[0]/mbar/menu[2]/menu[11]").select()
            sname=f'{path}/{no} [{system}].MIGO - Good Receipt_Status.png'
            session.findById("wnd[1]").HardCopy(sname, 1)
            session.findById("wnd[1]").close()
            print(f"Taken Status screenshot of MIGO")
        except Exception as e:
            print("Unable to take Status screenshot of MIGO :",e)
            return {"status" : 0, "error" : "Unable to take Status screenshot of MIGO"}
        return {"status" : 1} 
    except Exception as e:
        print("error while capturing MIGO - Good Receipt : ",e)
        error_ss = f"{path}/Error [{system}].MIGO - Good Receipt.png"
        time.sleep(2)
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error while capturing MIGO - Good Receipt"}

if __name__ == "__main__":
    import os
    import logon
    import sender
    import datetime
    no = 1
    #RBQ = "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    SBP = "0.1 - R/3 Production"
    RBP = "1.1 - RBP - SAP ERP 6.0(R/3) System"
    session = logon.Autosap(RBP)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)
    migo(no, session, path, stamp, sd="26.05.2025", system="rbp")
