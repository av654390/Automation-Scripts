
def lc10(nos = 0,session = 0,stamp = 0,path= 0,sid = 0):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nLC10"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtCON_NAME").text = "LCA"
        session.findById("wnd[0]/usr/ctxtCON_NAME").caretPosition = 3
        session.findById("wnd[0]/tbar[1]/btn[37]").press()
        try:
            session.findById("wnd[0]/usr/txtOVERVIEW-LABEL_STATE").setFocus()
            # status1 = session.findById("wnd[0]/usr/txtOVERVIEW-LABEL_STATE").text
            # print("Status1:",status1)
            session.findById("wnd[0]/usr/txtOVERVIEW-STATE_ICON").setFocus()
            session.findById("wnd[0]/usr/txtOVERVIEW-STATE_ICON").caretPosition = 0
            status = session.findById("wnd[0]/usr/txtOVERVIEW-STATE_ICON").IconName
            print("Operational State Status:",status)
            if status == "S_TL_G":
                operational_status = "Green"
            else:
                operational_status = "Red"
        except:
            print("Error while checking Operational State Status")
        try:
            session.findById("wnd[0]/usr/txtOVERVIEW-LABEL_AUTOLOG").setFocus()
            session.findById("wnd[0]/usr/txtOVERVIEW-LABEL_AUTOLOG").caretPosition = 16
            # on1 = session.findById("wnd[0]/usr/txtOVERVIEW-LABEL_AUTOLOG").text
            # print("ON?1:",on1)
            # session.findById("wnd[0]").sendVKey(2)
            session.findById("wnd[0]/usr/txtOVERVIEW-STATE_AUTOLOG").setFocus()
            session.findById("wnd[0]/usr/txtOVERVIEW-STATE_AUTOLOG").caretPosition = 1
            auto_backup = session.findById("wnd[0]/usr/txtOVERVIEW-STATE_AUTOLOG").text
            print("Automatic Log Backup:",auto_backup)
            # session.findById("wnd[0]").sendVKey(2)
        except:
            print("Error while Automatic Log Backup")
        session.findById("wnd[0]/usr/txtOVERVIEW-LABEL_GRAPH_DATA").setFocus()
        session.findById("wnd[0]/usr/txtOVERVIEW-LABEL_GRAPH_DATA").caretPosition = 2
        session.findById("wnd[0]").sendVKey(2)
        session.findById("wnd[0]/usr/btnAREADATA-TEXT_BUTTON_DETAILS").press()
        session.findById("wnd[0]/usr/subSUB_DETAILS:SAPLSSDBCCMS:0102/cntlCONT_DETAILS/shellcont/shell").setCurrentCell(1,"SIZE_PCT")
        used_data = session.findById("wnd[0]/usr/subSUB_DETAILS:SAPLSSDBCCMS:0102/cntlCONT_DETAILS/shellcont/shell").GetCellValue(1,"SIZE_PCT")
        print("Used Area Data:",used_data)
        session.findById("wnd[0]/usr/subSUB_DETAILS:SAPLSSDBCCMS:0102/cntlCONT_DETAILS/shellcont/shell").selectedRows = "1"
        session.findById("wnd[0]/tbar[0]/btn[3]").press()
        session.findById("wnd[0]/usr/txtOVERVIEW-LABEL_GRAPH_LOG").setFocus()
        session.findById("wnd[0]/usr/txtOVERVIEW-LABEL_GRAPH_LOG").caretPosition = 1
        session.findById("wnd[0]").sendVKey(2)
        session.findById("wnd[0]/usr/txtAREALOG-USED-SIZE_PCT").setFocus()
        session.findById("wnd[0]/usr/txtAREALOG-USED-SIZE_PCT").caretPosition = 6
        used_log = session.findById("wnd[0]/usr/txtAREALOG-USED-SIZE_PCT").text
        print("Used Area Log:",used_log)
        return {"operational_status": operational_status,"Automatic Log Backup":auto_backup,"Used Area Data":used_data,"Used Area Log":used_log}
    except Exception as e:
        return {"error": 0, "message": f"An error occurred in rz03: {e}"}


if __name__ == "__main__":
    try:
        import os
        import datetime
        import logon
        stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        sid = {"AUP": "0.3 - APO Production"}
        nos = 1
        path = os.getcwd() + f"\excel data\\autosap {stamp}\\"
        # File download section
        try:
            for system_id in sid:
                session = logon.Autosap(sid[system_id])
                print(lc10(nos=nos, session=session, stamp=stamp, path=path, sid = system_id))
                # print(logon.logof(session))
                nos += 1
        except Exception as e:
            print(f"Error during file download: {e}")
    except Exception as e:
        print(f"General error: {e}")
