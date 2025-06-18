def ZSD_SOBOOK(no,session,path,stamp,sd,ed):
    try:
        
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nZSD_SOBOOK"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtS_VKORG-LOW").setFocus()
        session.findById("wnd[0]/usr/ctxtS_VKORG-LOW").caretPosition = 0
        session.findById("wnd[0]").sendVKey (4)
        session.findById("wnd[1]/usr/lbl[1,4]").setFocus()
        session.findById("wnd[1]/usr/lbl[1,4]").caretPosition = 3
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/usr/ctxtS_AUDAT-LOW").text = sd #"01.03.2025"
        session.findById("wnd[0]/usr/ctxtS_AUDAT-HIGH").text = ed #"07.03.2025"
        session.findById("wnd[0]/usr/ctxtS_AUDAT-HIGH").setFocus()
        session.findById("wnd[0]/usr/ctxtS_AUDAT-HIGH").caretPosition = 10
        session.findById("wnd[0]/tbar[1]/btn[8]").press() #ss
        ss_zsdso = f"{path}/{no} ZSD_SOBOOK.png"
        session.findById("wnd[0]").HardCopy(ss_zsdso, 1)

        try:
            session.findById("wnd[0]/mbar/menu[5]/menu[11]").select()
            ss_zsdso_status = f"{path}/{no} ZSD_SOBOOK_Status.png"
            session.findById("wnd[1]").HardCopy(ss_zsdso_status, 1)
            session.findById("wnd[1]").close()
            print(f"Taken Status screenshot of ZSD_SOBOOK")
        except Exception as e:
            print("Unable to take Status screenshot of ZSD_SOBOOK :",e)
            return {"status" : 0, "error" : "Unable to take Status screenshot of ZSD_SOBOOK " }

        return {"status" : 1}
    except Exception as e:
        print("Error while capturing ZSD_SOBOOK : ",e)
        error_ss = f"{path}/Error ZSD_SOBOOK.png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error while capturing ZSD_SOBOOK " }

if __name__ == "__main__":
    import os
    import logon
    import datetime
    RBQ = "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    session = logon.Autosap(RBQ)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)
    ZSD_SOBOOK(no=1,session=session,path=path,stamp=stamp,sd ="01.03.2025",ed="20.03.2025")  