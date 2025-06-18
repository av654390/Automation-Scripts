# ****************************************************************************
#  Program Description : Script to read&capture se16 view table              *
#  Program Name:  Procurement Post-Fun Checks\se16.py                        *
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
def se16(no,session,path,stamp,system):
    try:
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nse16"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtDATABROWSE-TABLENAME").text = "BUT000"
        session.findById("wnd[0]/usr/ctxtDATABROWSE-TABLENAME").caretPosition = 6
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/txtMAX_SEL").text = ""
        session.findById("wnd[0]/usr/txtMAX_SEL").setFocus()
        session.findById("wnd[0]/usr/txtMAX_SEL").caretPosition = 10
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        ss_se16 = f"{path}/{no} [{system}].SE16 - View Table.png"
        session.findById("wnd[0]").HardCopy(ss_se16, 1)
        try:
            try:
                session.findById("wnd[0]/mbar/menu[6]/menu[11]").select()
            except:
                session.findById("wnd[0]/mbar/menu[4]/menu[11]").select()
            sname=f'{path}/{no} [{system}].SE16 - View Table_Status.png'
            session.findById("wnd[1]").HardCopy(sname, 1)
            session.findById("wnd[1]").close()
            print(f"Taken Status screenshot of SE16")
        except Exception as e:
            print("Unable to take Status screenshot of SE16 :",e)
        return {"status" : 1}
    except Exception as e:
        print("error while capturing SE16 - View Table : ",e)
        error_ss = f"{path}/Error [{system}].SE16 - View Table.png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error while capturing SE16 - View Table"}

if __name__ == "__main__":
    import os
    import logon
    import sender
    import datetime
    no = 1
    system = {
        "SLP" : "1.4 - SLP -SAP SLM Buy Side"
        #"LMP" : "1.5 - LMP-SLM Sell Side"
        }
    session = logon.Autosap(system["SLP"])
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)
    se16(no,session,path,stamp,"SLP")
