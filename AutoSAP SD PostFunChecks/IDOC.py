def idoc(no,session, path, stamp):
    try:
        import time
        session.findById("wnd[0]/tbar[0]/okcd").text = "/NWE02"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/tabsTABSTRIP_IDOCTABBL/tabpSOS_TAB/ssub%_SUBSCREEN_IDOCTABBL:RSEIDOC2:1100/btn%_IDOCTP_%_APP_%-VALU_PUSH").press()
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,0]").text = "ORDERS05"
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,1]").text = "ORDERRSP"
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").text = "INVOIC"
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").setFocus()
        session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").caretPosition = 6
        session.findById("wnd[1]/tbar[0]/btn[8]").press()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        time.sleep(2)
        ss_idoc = f"{path}/{no} IDOC FailureChecks.png"
        session.findById("wnd[0]").HardCopy(ss_idoc, 1)
        session.findById("wnd[0]/mbar/menu[3]/menu[11]").select()
        try:
            session.findById("wnd[0]/mbar/menu[3]/menu[11]").select()
            ss_idoc_status = f"{path}/{no} IDOC FailureChecks_Status.png"
            session.findById("wnd[1]").HardCopy(ss_idoc_status, 1)
            session.findById("wnd[1]").close()
            print("Taken Status screenshot of IDOC")
        except Exception as e:
            print("Unable to take Status screenshot of IDOC : ",e)
            return {"status" : 0, "error" : "Unable to take Status screenshot of IDOC"}
        return {"status" : 1}
    except Exception as e:
        print("error while capturing IDOC failure checks : ",e)
        error_ss = f"{path}/Error IDOC failure checks.png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error while capturing IDOC failure checks" }

        # import pyautogui
        # import time

    #print("Move your mouse to the desired position. You have 5 seconds...")
    # time.sleep(5)

    # # x, y = pyautogui.position()
    # # print(f"Mouse is at: ({x}, {y})")
    # pyautogui.moveTo(1117, 710)
    # pyautogui.click()


    # time.sleep(2)  # Wait for SAP to be in focus
    # sap_window = pyautogui.getWindowsWithTitle("SAP")  # Adjust the window title as needed

    # if sap_window:
    #     x, y, w, h = sap_window[0].left, sap_window[0].top, sap_window[0].width, sap_window[0].height
    #     print("Xx=",x)
    #     print("Yy=",y)
    #     print("Ww=",w)
    #     print("Hh=",h)
    #     x, y, w, h = 0,0 ,1350,800
    #     pyautogui.screenshot(f"{path}/IDOC_List.png", region=(x, y, w, h))



if __name__ == "__main__":
    import os
    import logon
    import datetime
    RBP = "1.1 - RBP - SAP ERP 6.0(R/3) System"
    session = logon.Autosap(RBP)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)
    idoc(no=1,session=session,path=path,stamp=stamp) 