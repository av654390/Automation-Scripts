# ****************************************************************************
#  Program Description : Script to capture different job names               *
#  Program Name:  Procurement Post-Fun Checks\sm37.py                        *
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
import os
def get_job_details(system):
    if system == "SBP":
        return [
            {"JOBNAME": "ZP2P_ AUTO_SEND_ZAPO_ALL_VX"},
            {"JOBNAME": "*", "ABAPNAME": "ARBCIG_MASTER_DATA_EXPORT"}
        ]
    elif system == "RBP":
        return [
            {"JOBNAME": "ZARIBA_PO_DISPATCH"},
            {"JOBNAME": "ZSLM_REQ_CHG_NOTIFICATION"},
            {"JOBNAME": "*", "ABAPNAME": "ARBCIG_MASTER_DATA_EXPORT"}
        ]

    elif system == "SLP":
        return [{"JOBNAME": "*"}]

    elif system == "LMP":
        return [{"JOBNAME": "*"}]

    else:
        return []
def sm37(no, session, sid, stamp, path, job_details):
    try:
        import datetime
        import time
        today = datetime.datetime.today().strftime("%d.%m.%Y")
        print("Today's date:", today)
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsm37"
        session.findById("wnd[0]").sendVKey (0)
        #session.findById("wnd[0]/usr/chkBTCH2170-PRELIM").selected = True
        session.findById("wnd[0]/usr/txtBTCH2170-USERNAME").text = "*"
        session.findById("wnd[0]/usr/ctxtBTCH2170-FROM_DATE").text = today #"05.04.2025"
        session.findById("wnd[0]/usr/ctxtBTCH2170-TO_DATE").text = today #"05.04.2025"
        for job in job_details:
            session.findById("wnd[0]/usr/txtBTCH2170-JOBNAME").text = job.get("JOBNAME")
            if "ABAPNAME" in job:
                session.findById("wnd[0]/usr/txtBTCH2170-ABAPNAME").text = job.get("ABAPNAME")
            session.findById("wnd[0]/usr/txtBTCH2170-ABAPNAME").setFocus()
            session.findById("wnd[0]/usr/txtBTCH2170-ABAPNAME").caretPosition = 25
            session.findById("wnd[0]/tbar[1]/btn[8]").press()

            message1=session.findById("wnd[0]/sbar").text
            print(message1)
            import time
            if message1=="No job matches the selection criteria":
                time.sleep(2)
                if not os.path.exists(path):
                    os.makedirs(path)
                errorss=f'{path}/Error [{sid}] sm37 {stamp}.png'
                session.findById("wnd[0]").HardCopy(errorss, 1)
                #return {"status" : 0, "error" : "No job matches the selection criteria for SM37"}
                no += 1

                #session.findById("wnd[0]/tbar[0]/btn[3]").press()
                continue
                #return
            if sid == "SBP":
                try:
                    session.findById("wnd[0]/usr/lbl[159,10]").setFocus()
                    session.findById("wnd[0]").sendVKey (2)
                    session.findById("wnd[0]/tbar[1]/btn[40]").press()
                except:
                    try:
                        # Fallback to lbl[91,11] if lbl[91,10] fails
                        session.findById("wnd[0]/usr/lbl[159,11]").setFocus()
                        session.findById("wnd[0]").sendVKey(2)
                    except Exception as e:
                        print("Both attempts failed:", str(e))
            elif sid in ["RBP", "SLP", "LMP"]:
                try:
                    session.findById("wnd[0]/usr/lbl[91,10]").setFocus()
                    session.findById("wnd[0]").sendVKey (2)
                    session.findById("wnd[0]/tbar[1]/btn[40]").press()
                except:
                    try:
                        # Fallback to lbl[91,11] if lbl[91,10] fails
                        session.findById("wnd[0]/usr/lbl[91,11]").setFocus()
                        session.findById("wnd[0]").sendVKey(2)
                    except Exception as e:
                        print("Both attempts failed:", str(e))
            time.sleep(3)
            if not os.path.exists(path):
                os.makedirs(path)
            name=f'{path}/{no} [{sid}] sm37 {stamp}.png'
            session.findById("wnd[0]").HardCopy(name, 1)
            try:
                session.findById("wnd[0]/mbar/menu[5]/menu[11]").select()
                sname=f'{path}/{no} [{sid}] SM37_Status.png'
                session.findById("wnd[1]").HardCopy(sname, 1)
                session.findById("wnd[1]").close()
                print(f"Taken Status screenshot of SM37")
            except Exception as e:
                print("Unable to take Status screenshot of SM37 :",e) 
                return {"status" : 0, "error" : "Unable to take Status screenshot of SM37"}
            session.findById("wnd[0]/tbar[0]/btn[3]").press()
            no +=1 
        return {"status": 1}, no

    except Exception as e:
        print("Error in SM37 Job Monitoring : ",e )
        error_ss = f"{path}/Error SM37 Job Monitoring.png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return{"error": "Error in SM37 Job Monitoring", "status" : 0}


if __name__ == "__main__":
    try:
        import os
        import datetime
        import logon
        import sender

        stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        sid = {
            #"SBP":"0.1 - R/3 Production",
            "RBP" : "1.1 - RBP - SAP ERP 6.0(R/3) System",
            "SLP" : "1.4 - SLP -SAP SLM Buy Side",
            "LMP" : "1.5 - LMP-SLM Sell Side"
        }

        no = 1
        path = os.getcwd() + f"\excel data\\autosap {stamp}\\"
        for system in sid:
            try:
                job_details = get_job_details(system)
                session = logon.Autosap(sid[system])
                print(sm37(no=no, session=session, sid=system, stamp=stamp, path=path, job_details=job_details))
                print(logon.logof(session))
                #no += 1
            except Exception as e:
                print(f"Error during file download: {e}")

            
    except Exception as e:
        print(f"General error: {e}")
  
