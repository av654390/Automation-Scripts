# ****************************************************************************
#  Program Description : script to get idoc status                           *
#  Program Name:  Procurement Post-Fun Checks\idoc.py                        *
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
def idoc(no,session, path, stamp, system):
    try:
        session.findById("wnd[0]/tbar[0]/okcd").text = "/NWE02"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/tabsTABSTRIP_IDOCTABBL/tabpSOS_TAB/ssub%_SUBSCREEN_IDOCTABBL:RSEIDOC2:1100/btn%_IDOCTP_%_APP_%-VALU_PUSH").press()
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,0]").text = "ORDERS05"
        # session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,1]").text = "ORDERRSP"
       # session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").text = "INVOIC"
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").setFocus()
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").caretPosition = 6
        session.findById("wnd[1]/tbar[0]/btn[8]").press()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        ss_idoc = f"{path}/{no} [{system}].WE02 - Idoc Status.png"
        session.findById("wnd[0]").HardCopy(ss_idoc, 1)
        try:
            session.findById("wnd[0]/mbar/menu[3]/menu[11]").select()
            ss_idoc_status = f"{path}/{no} [{system}].IDOCStatus_Status.png"
            session.findById("wnd[1]").HardCopy(ss_idoc_status, 1)
            session.findById("wnd[1]").close()
            print("Taken Status screenshot of IDOC")
        except Exception as e:
            print("Unable to take Status screenshot of IDOC : ",e)
            return {"status" : 0, "error" : "Unable to take Status screenshot of IDOC"}
        return {"status" : 1}
    except Exception as e:
        print("error while capturing IDOC Status : ",e)
        error_ss = f"{path}/Error [{system}].IDOC Status.png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error while capturing IDOC Status" }

if __name__ == "__main__":
    import os
    import logon
    import datetime
    SBP = "0.1 - R/3 Production"
    #SBP = "0.1b - R/3 Production - International Sites"
    RBP = "1.1 - RBP - SAP ERP 6.0(R/3) System"
    #RBQ = "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    session = logon.Autosap(RBP)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)
    idoc(no=1,session=session,path=path,stamp=stamp,system="rbp") 