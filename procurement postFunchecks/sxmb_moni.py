# ****************************************************************************
#  Program Description : Script to capture sxmb_moni status                  *
#  Program Name:  Procurement Post-Fun Checks\sxmb_moni.py                   *
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
def sxmb_moni(no,session,path,stamp,system):
    try:
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nSXMB_MONI"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/cntlSPLITTER_CONTAINER_TR/shellcont/shell").selectedNode = ("MONI_LOG")
        #session.findById("wnd[0]/usr/cntlSPLITTER_CONTAINER_TR/shellcont/shell").doubleClickNode ("MONI_LOG")
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        ss_moni = f"{path}/{no} [{system}].SXMB_MONI - XML .png"
        session.findById("wnd[0]").HardCopy(ss_moni, 1)
        if system.lower() == "slp":
            try:
                session.findById("wnd[1]").HardCopy(ss_moni, 1)
                session.findById("wnd[1]/tbar[0]/btn[0]").press()
            except Exception as e:
                print("Optional window button press failed for SLP:", e)
                
        #session.findById("wnd[1]/tbar[0]/btn[0]").press()
        try:
            session.findById("wnd[0]/mbar/menu[3]/menu[11]").select()
            ss_moni_status = f"{path}/{no} [{system}].SXMB_MONI - XML Status .png"
            session.findById("wnd[1]").HardCopy(ss_moni_status, 1)
            session.findById("wnd[1]").close()
            print("Taken Status screenshot of SXMB_MONI status")
        except Exception as e:
            print("Unable to take Status screenshot of SXMB_MONI : ",e)
            #return {"status" : 0, "error" : "Unable to take Status screenshot of SXMB_MONI"}
        return {"status" : 1}
    except Exception as e:
        print("error while capturing SXMB_MONI - XML Status : ",e)
        error_ss = f"{path}/Error [{system}].SXMB_MONI - XML Status .png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error while capturing SXMB_MONI - XML Status"}

if __name__ == "__main__":
    import os
    import logon
    import sender
    import datetime

    no = 1
    system = {
        #"SLP": "1.4 - SLP -SAP SLM Buy Side"
        "RBP": "1.1 - RBP - SAP ERP 6.0(R/3) System"
    }

    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)

    output = []

    for sys_code in system:
        print(f"\n--- Running for {sys_code} ---")
        try:
            session = logon.Autosap(system[sys_code])
            sxmb_moni_resp = sxmb_moni(no, session, path, stamp, sys_code)
            print("SXMB_MONI Response:", sxmb_moni_resp)
            output.append(sxmb_moni_resp)
            no += 1
        except Exception as e:
            print(f"Error while processing {sys_code}:", e)
