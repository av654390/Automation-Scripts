# ****************************************************************************
#  Program Description : Script to capture sost- mail notification           *
#  Program Name:  Procurement Post-Fun Checks\sost .py                       *
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
def sost(no,session,path,stamp,system):
    try:
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsost"
        session.findById("wnd[0]").sendVKey (0)
        ss_sost = f"{path}/{no} [{system}].SOST - Mail Notification.png"
        session.findById("wnd[0]").HardCopy(ss_sost, 1)
        try:
            session.findById("wnd[0]/mbar/menu[5]/menu[11]").select()
            sname=f'{path}/{no} [{system}].SOST - Mail Notification_Status.png'
            session.findById("wnd[1]").HardCopy(sname, 1)
            session.findById("wnd[1]").close()
            print(f"Taken Status screenshot of SOST")
        except Exception as e:
            print("Unable to take Status screenshot of SOST :",e)
        return {"status" : 1}
    except Exception as e:
        print("error while capturing SOST - Mail Notification : ",e)
        error_ss = f"{path}/Error [{system}].SOST - Mail Notification.png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error while capturing SOST - Mail Notification"}

if __name__ == "__main__":
    import os
    import logon
    import sender
    import datetime
    no = 1
    system = {
        #"SLP" : "1.4 - SLP -SAP SLM Buy Side"
        "LMP" : "1.5 - LMP-SLM Sell Side"
        }
    session = logon.Autosap(system["LMP"])
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)
    sost(no,session,path,stamp,"LMP")
