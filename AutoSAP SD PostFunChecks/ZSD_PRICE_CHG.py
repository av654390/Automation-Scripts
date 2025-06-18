def ZSD_PRICE_CHG(no, session,path,stamp):
    try:
        import datetime
        from dateutil.relativedelta import relativedelta
        today = datetime.date.today()
        # Generate dynamic sd and ed for last 3 months
        today = datetime.date.today()
        ed = today.strftime("%d.%m.%Y")
        sd = (today - relativedelta(months=3)).strftime("%d.%m.%Y")
        print("Start Date for ZSD_PRICE_CHG_REPORT :",sd)
        print("End Date for ZSD_PRICE_CHG_REPORT :",ed)
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nZSD_PRICE_CHG_REPORT"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtO_DATE-LOW").text = sd
        session.findById("wnd[0]/usr/ctxtO_DATE-HIGH").text = ed
        session.findById("wnd[0]/usr/ctxtO_KSCHL-LOW").text = "zpr0"
        session.findById("wnd[0]/usr/ctxtO_VKORG-LOW").setFocus()
        session.findById("wnd[0]/usr/ctxtO_VKORG-LOW").caretPosition = 3
        session.findById("wnd[0]").sendVKey (4)
        session.findById("wnd[1]/usr/lbl[1,4]").setFocus()
        session.findById("wnd[1]/usr/lbl[1,4]").caretPosition = 2
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        ss_zsdreport = f"{path}/{no} ZSD_PRICE_CHG_REPORT.png"
        session.findById("wnd[0]").HardCopy(ss_zsdreport, 1)
        try:
            session.findById("wnd[0]/mbar/menu[5]/menu[11]").select()
            ss_zsdreport_status = f"{path}/{no} ZSD_PRICE_CHG_REPORT_Status.png"
            session.findById("wnd[1]").HardCopy(ss_zsdreport_status, 1)
            session.findById("wnd[1]").close()
            print(f"Taken Status screenshot of ZSD_PRICE_CHG_REPORT")
        except Exception as e:
            print("Unable to take Status screenshot of ZSD_PRICE_CHG_REPORT :",e)
            return {"status" : 0, "error" : "Unable to take Status screenshot of ZSD_PRICE_CHG_REPORT"}
        return {"status" : 1}
    except Exception as e:
        print("error while capturing ZSD_PRICE_CHG Report : ",e)
        error_ss = f"{path}/Error ZSD_PRICE_CHG Report.png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error while capturing ZSD_PRICE_CHG Report" }

if __name__ == "__main__":
    import os
    import logon
    import datetime
    no = 1
    RBP= "1.1 - RBP - SAP ERP 6.0(R/3) System"
    RBQ = "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    session = logon.Autosap(RBP)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)
    ZSD_PRICE_CHG(no,session,path,stamp)  
    