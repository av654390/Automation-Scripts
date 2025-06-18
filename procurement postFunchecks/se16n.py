# ****************************************************************************
#  Program Description : Script to read&capture se16n view table             *
#  Program Name:  Procurement Post-Fun Checks\se16n.py                       *
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
def se16n(no,session,path,stamp,system):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nse16n"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtGD-TAB").text = "BUT000"
        session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = ""
        session.findById("wnd[0]/usr/txtGD-MAX_LINES").setFocus()
        session.findById("wnd[0]/usr/txtGD-MAX_LINES").caretPosition = 0
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").currentCellRow = -1
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectColumn ("PARTNER")
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarButton ("&SORT_DSC")
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").setColumnWidth ("PARTNER",17)
        ss_se16n = f"{path}/{no} [{system}].SE16N - View Table.png"
        session.findById("wnd[0]").HardCopy(ss_se16n, 1)
        try:
            session.findById("wnd[0]/mbar/menu[3]/menu[11]").select()
            sname=f'{path}/{no} [{system}].SE16N - View Table_Status.png'
            session.findById("wnd[1]").HardCopy(sname, 1)
            session.findById("wnd[1]").close()
            print(f"Taken Status screenshot of SE16N")
        except Exception as e:
            print("Unable to take Status screenshot of SE16N :",e)
        return {"status" : 1}
    except Exception as e:
        print("error while capturing SE16N - View Table : ",e)
        error_ss = f"{path}/Error [{system}].SE16N - View Table.png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error while capturing SE16N - View Table"}

if __name__ == "__main__":
    import os
    import logon
    import sender
    import datetime
    no = 1
    SBP = "0.1 - R/3 Production"
    #SBP = "Z.0.1 - SBP SYSTEM Restricted - for SAP Basis only"
    RBP = "1.1 - RBP - SAP ERP 6.0(R/3) System"
    session = logon.Autosap(RBP)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)
    se16n(no,session,path,stamp,system="rbp")