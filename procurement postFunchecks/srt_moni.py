# ****************************************************************************
#  Program Description : Script to capture web service monitor               *
#  Program Name:  Procurement Post-Fun Checks\srt_moni.py                    *
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
def srt_moni(no,session,path,stamp,system):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsrt_moni"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        ss_moni = f"{path}/{no} [{system}].SRT_MONI - web service monitor.png"
        session.findById("wnd[0]").HardCopy(ss_moni, 1)
        try:
            session.findById("wnd[0]/mbar/menu[3]/menu[11]").select()
            ss_moni_status = f"{path}/{no} [{system}].SRT_MONI - web service monitor Status .png"
            session.findById("wnd[1]").HardCopy(ss_moni_status, 1)
            session.findById("wnd[1]").close()
            print("Taken Status screenshot of SRT_MONI - web service monitor")
        except Exception as e:
            print("Unable to take Status screenshot of SRT_MONI - web service monitor : ",e)
            #return {"status" : 0, "error" : "Unable to take Status screenshot of SXMB_MONI"}
        return {"status" : 1}
    except Exception as e:
        print("error while capturing SRT_MONI - web service monitor : ",e)
        error_ss = f"{path}/Error [{system}].SRT_MONI - web service monitor.png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error while capturing SRT_MONI - web service monitor"}

if __name__ == "__main__":
    import os
    import logon
    import sender
    import datetime
    no = 1
    LMP = "1.5 - LMP-SLM Sell Side"
    session = logon.Autosap(LMP)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)
    srt_moni(no,session,path,stamp,system="LMP")