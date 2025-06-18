def vf03(no,session,path,stamp,sd,ed):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nse16n"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtGD-TAB").text = "NAST"
        session.findById("wnd[0]/usr/ctxtGD-TAB").setFocus()
        session.findById("wnd[0]/usr/ctxtGD-TAB").caretPosition = 4
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = "500"
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,1]").text = "V3"
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,3]").text = "ZRD0"
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,7]").text = sd #"07.03.2025"
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-HIGH[3,7]").text = ed #"12.03.2025"
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-HIGH[3,7]").setFocus()
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-HIGH[3,7]").caretPosition = 10
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem ("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path #"C:\Users\as776099\OneDrive - GSK\Documents\SAP\SAP GUI\"
        name = f'{no}_NAST_{stamp}.html'
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        import os
        import pandas as pd
        file_path = os.path.join(path, name)
        g = pd.read_html(file_path, header=0)[0]
        invoice_id = g.loc[0,'Object\xa0key']
        print({"Invoice_ID" : invoice_id})

        try:
            import time
            message1=session.findById("wnd[0]/sbar").text
            print(message1)
            if message1=="No values found":
                time.sleep(2)
                errorss=f'{path}/Error_NAST.png'
                session.findById("wnd[0]").HardCopy(path+errorss, 1)
                return {"error":"Error while capturing Billing Document ID",'status':0}
        except Exception as e:
            print({"NAST document id found",e})

        # session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").currentCellColumn = "OBJKY"
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nvf03"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtVBRK-VBELN").text = invoice_id #"4203008235"
        session.findById("wnd[0]/usr/ctxtVBRK-VBELN").caretPosition = 10
        session.findById("wnd[0]").sendVKey (0)
        ss_vf03 = f"{path}/{no}. VF03-Billing Document.png"
        session.findById("wnd[0]").HardCopy(ss_vf03, 1)
        try:
            session.findById("wnd[0]/mbar/menu[4]/menu[11]").select()
            ss_vf03_status = f"{path}/{no}. VF03-Billing Document_Status.png"
            session.findById("wnd[1]").HardCopy(ss_vf03_status, 1)
            session.findById("wnd[1]").close()
            print("Taken Status screenshot of VF03-Billing")
        except:
            print("Unable to take Status screenshot of VF03-Billing")
        session.findById("wnd[0]/tbar[0]/btn[3]").press()
        session.findById("wnd[0]/mbar/menu[0]/menu[11]").select()
        no +=1
        ss_invoice = f"{path}/{no}. Invoice Layout.png"
        session.findById("wnd[1]").HardCopy(ss_invoice, 1)
        session.findById("wnd[1]/usr/tblSAPLVMSGTABCONTROL").getAbsoluteRow(0).selected = True
        session.findById("wnd[1]/tbar[0]/btn[37]").press()
        time.sleep(3)
        #session.findById("wnd[0]/mbar/menu[2]/menu[2]").select()
        no +=1
        ss_pp = f"{path}/{no}. print_preview.png"
        session.findById("wnd[0]").HardCopy(ss_pp, 1)
        try:
            session.findById("wnd[0]/mbar/menu[4]/menu[11]").select()
            ss_pp_status = f"{path}/{no}. print_preview_status.png"
            session.findById("wnd[1]").HardCopy(ss_pp_status, 1)
            session.findById("wnd[1]").close()
            print("Taken Status screenshot of VF03-PrintPreview")
        except:
            print("Unable to take Status screenshot of VF03-PrintPreview")
        return {"status" : 1}
    except Exception as e:
        print("error while capturing invoice : ",e)
        error_ss = f"{path}/Error VF03-Invoice.png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error while capturing VF03-Invoice"}
if __name__ == "__main__":
    import os
    import logon
    import sender
    import datetime
    no = 1
    #RBQ = "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    RBP = "1.1 - RBP - SAP ERP 6.0(R/3) System"
    session = logon.Autosap(RBP)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)
    vf03(no,session,path,stamp,sd="17.03.2025",ed="24.03.2025")  
