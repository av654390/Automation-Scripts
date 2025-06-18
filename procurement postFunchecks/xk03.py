# ****************************************************************************
#  Program Description : Script to capture xk03 vendor id                    *
#  Program Name:  Procurement Post-Fun Checks\xk03.py                        *
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
def xk03(no, session, path, stamp, system):
    try:
        # Vendor numbers for respective systems
        vendor_ids = {
            "SBP": "119149",       # SBP system vendor
            "RBP": "9900748733"    # RBP system vendor
        }

        vendor_id = vendor_ids.get(system, "")
        if not vendor_id:
            raise ValueError(f"Vendor ID not found for system '{system}'")

        session.findById("wnd[0]/tbar[0]/okcd").text = "/nxk03"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtRF02K-LIFNR").text = vendor_id
        session.findById("wnd[0]/usr/ctxtRF02K-LIFNR").caretPosition = len(vendor_id)
        session.findById("wnd[0]/tbar[1]/btn[7]").press()
        session.findById("wnd[0]").sendVKey(0)
        # Save screenshot with SID name
        ss_xk03 = f"{path}/{no} [{system}].XK03 - Vendor Display.png"
        session.findById("wnd[0]").HardCopy(ss_xk03, 1)
        try:
            session.findById("wnd[0]/mbar/menu[5]/menu[11]").select()
            sname=f'{path}/{no} [{system}] XK03_Status.png'
            session.findById("wnd[1]").HardCopy(sname, 1)
            session.findById("wnd[1]").close()
            print(f"Taken Status screenshot of XK03")
        except Exception as e:
            return {"status" : 0, "error" : "Unable to take Status screenshot of XK03"}
        return {"status" : 1}
            #print("Unable to take Status screenshot of XK03 :",e) 
    except Exception as e:
        print("Error while capturing XK03 - Vendor Display:", e)
        error_ss = f"{path}/Error_{system}.XK03 - Vendor Display.png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status": 0, "error": f"Error while capturing XK03 - Vendor Display: {e}"}
if __name__ == "__main__":
    import os
    import logon
    import sender
    import datetime

    sid = {
        "SBP": "0.1 - R/3 Production",
        "RBP": "1.1 - RBP - SAP ERP 6.0(R/3) System"
    }

    no = 1
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)

    for system in sid:
        try:
            session = logon.Autosap(sid[system])
            xk03(no, session, path, stamp, system)
            logon.logof(session)
            no += 1
        except Exception as e:
            print(f"Error for system {system}: {e}")
