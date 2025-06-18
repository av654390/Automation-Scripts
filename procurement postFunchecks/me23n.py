# ****************************************************************************
#  Program Description : Script to read&capture purchase document display    *
#  Program Name:  Procurement Post-Fun Checks\me23n.py                       *
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
def me23n(no,session,path,stamp,sd, system):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nse16n"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtGD-TAB").text = "EKKO"
        session.findById("wnd[0]/usr/ctxtGD-TAB").caretPosition = 4
        session.findById("wnd[0]").sendVKey (0)
        #session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = "100"
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,4]").text = "ZAPO"
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,4]").setFocus()
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,4]").caretPosition = 4
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC").verticalScrollbar.position = 1
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,7]").text = sd #"03.04.2025"
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,7]").setFocus()
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,7]").caretPosition = 10
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        try:
            import time
            message1=session.findById("wnd[0]/sbar").text
            print(message1)
            if message1=="No values found":
                time.sleep(2)
                errorss=f'{path}/Error[{system}]_ME23N.png'
                session.findById("wnd[0]").HardCopy(errorss, 1)
                #return {"status" : 0, "error" : "No values found in EKKO table for ME23n"}
        except Exception as e:
            print({"EKKO document id found",e})
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem ("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path #"C:\Users\as776099\OneDrive - GSK\Documents\SAP\SAP GUI\"
        name = f'{no}_EKKO_{stamp}.html'
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 10
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        import os
        import pandas as pd
        file_path = os.path.join(path, name)
        g = pd.read_html(file_path, header=0)[0]

        #PO_id = g.loc[0,'Pur.\xa0Doc.'] #RBP
        #PO_id=g.loc[0,'Purch.Doc.'] #SBP

        po_columns = ['Pur.\xa0Doc.', 'Purch.Doc.']
        for col in po_columns:
            if col in g.columns:
                PO_id = g.loc[0, col]
                break
        else:
            raise ValueError("Purchase Order column not found in the input data.")

        print({"PO_ID" : int(PO_id)})

        session.findById("wnd[0]/tbar[0]/okcd").text = "/nme23n"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/tbar[1]/btn[17]").press()
        session.findById("wnd[1]/usr/subSUB0:SAPLMEGUI:0003/ctxtMEPO_SELECT-EBELN").text = PO_id #"6601751148"
        session.findById("wnd[1]/usr/subSUB0:SAPLMEGUI:0003/radMEPO_SELECT-BSTYP_F").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        ss_me23n = f"{path}/{no} [{system}].ME23N - PO Display.png"
        session.findById("wnd[0]").HardCopy(ss_me23n, 1)

    ###extracting pr_id(Purchase_Request) for me53n tcode ####
        session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0019/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1212/cntlGRIDPO/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
        session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0019/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:1212/cntlGRIDPO/shellcont/shell").selectContextMenuItem ("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path #"C:\Users\as776099\OneDrive - GSK\Documents\SAP\SAP GUI\"
        name = f'{no}_me53n_{stamp}.html'
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        import os
        import pandas as pd
        file_path = os.path.join(path, name)
        f = pd.read_html(file_path, header=0)[0]
        PR_id = f.loc[0,'Purch.Req.']
        PR_id = int(PR_id)
        print({"PR_ID" : PR_id})

        try:
            session.findById("wnd[0]/mbar/menu[4]/menu[11]").select()
            sname=f'{path}/{no} [{system}].ME23N - PO Display_Status.png'
            session.findById("wnd[1]").HardCopy(sname, 1)
            session.findById("wnd[1]").close()
            print(f"Taken Status screenshot of ME23N")
        except Exception as e:
            print("Unable to take Status screenshot of ME23N :",e) 
        #return {"status" : 1}
        return{"Purchase_Request" : PR_id, "status" : 1}
    except Exception as e:
        print("error while capturing ME23N - PO Display : ",e)
        error_ss = f"{path}/Error [{system}].ME23N - PO Display .png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error while capturing ME23N - PO Display "}

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
    me23n(no,session,path,stamp,sd="26.05.2025",system="rbp")  