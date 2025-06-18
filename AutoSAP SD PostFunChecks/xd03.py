# import postchecks
# sold_to_party=postchecks.postcheck
def xd03(no, session, path, stamp, sold_to_party):
    try:
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nxd03"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[1]/usr/ctxtRF02D-KUNNR").text = sold_to_party #
        ss_cusdis =f"{path}/{no}. XD03 Customer Display.png"
        session.findById("wnd[1]").HardCopy(ss_cusdis, 1)
        session.findById("wnd[1]/usr/ctxtRF02D-KUNNR").caretPosition = 10
        session.findById("wnd[1]/usr/btnBUTTON2").press()
        session.findById("wnd[2]/usr/tblSAPMF02DTCTRL_KUNDENVERTRIEB/ctxtRF02D-VKOKU[0,0]").setFocus()
        session.findById("wnd[2]/usr/tblSAPMF02DTCTRL_KUNDENVERTRIEB/ctxtRF02D-VKOKU[0,0]").caretPosition = 4
        session.findById("wnd[2]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/tbar[1]/btn[27]").press()
        session.findById("wnd[0]/usr/subSUBTAB:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB05").select()
        no +=1
        ss_sale = f"{path}/{no}. XD03 Customer SalesAreaData.png"
        session.findById("wnd[0]").HardCopy(ss_sale, 1)
        try:
            session.findById("wnd[0]/mbar/menu[5]/menu[11]").select()
            ss_sale_status = f"{path}/{no}. XD03 Customer SalesAreaData_Status.png"
            session.findById("wnd[1]").HardCopy(ss_sale_status, 1)
            session.findById("wnd[1]").close()
            print("Taken Status screenshot of XD03")
        except Exception as e:
            print("Unable to take Status screenshot of XD03",e)
        
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nvk13"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtRV13A-KSCHL").text = "zpr0"
        session.findById("wnd[0]/usr/ctxtRV13A-KSCHL").caretPosition = 4
        session.findById("wnd[0]/tbar[1]/btn[16]").press()
        session.findById("wnd[0]/tbar[1]/btn[8]").press() #screenshot
        no +=1
        ss_pricing = f"{path}/{no}. VK13_Pricing.png"
        session.findById("wnd[0]").HardCopy(ss_pricing, 1)
        session.findById("wnd[0]/usr/chk[0,4]").selected = True
        session.findById("wnd[0]/tbar[1]/btn[5]").press() #screenshot
        no +=1
        ss_overview = f"{path}/{no}. VK13_Overview.png"
        session.findById("wnd[0]").HardCopy(ss_overview, 1)
        try:
            session.findById("wnd[0]/mbar/menu[6]/menu[11]").select()
            ss_overview_status = f"{path}/{no}. VK13_Overview_Status.png"
            session.findById("wnd[1]").HardCopy(ss_overview_status, 1)
            session.findById("wnd[1]").close()
            print("Taken Status screenshot of VK13")
        except Exception as e:
            print("Unable to take Status screenshot of VK13",e)
            return {"status" : 0, "error" : "Unable to take Status screenshot of VK13" }

        #return {"status": 1, "next_no": no}
        return {"status" : 1}
    except Exception as e:
        print("error in customer pricing" , e)
        error_ss = f"{path}/Error customer pricing.png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error in customer pricing" }

if __name__ == "__main__":
    import os
    import logon
    import sender
    import datetime
    no = 1
    RBQ = "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    session = logon.Autosap(RBQ)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)
    xd03(no,session,path,stamp,sold_to_party) 