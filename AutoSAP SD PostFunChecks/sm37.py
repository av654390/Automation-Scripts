def sm37(no,session,path,stamp,today):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsm37"
        session.findById("wnd[0]").sendVKey (0)
        job_details = [
            {"JOBNAME": "*C64*", "USERNAME": "*"},
            {"JOBNAME": "*BACK*", "USERNAME": "*"},
            {"JOBNAME": "*", "USERNAME": "*", "ABAPNAME": "SDBILLDL"},
            {"JOBNAME": "*", "USERNAME": "*", "ABAPNAME": "RVV50R10C"}
        ]

        for job in job_details:
            # Set job name and user details
            session.findById("wnd[0]/usr/txtBTCH2170-JOBNAME").text = job["JOBNAME"]
            session.findById("wnd[0]/usr/txtBTCH2170-USERNAME").text = job["USERNAME"]

            if "ABAPNAME" in job:
                session.findById("wnd[0]/usr/txtBTCH2170-ABAPNAME").text = job["ABAPNAME"]
            # else:
            #     session.findById("wnd[0]/usr/txtBTCH2170-ABAPNAME").text = ""
            session.findById("wnd[0]/usr/ctxtBTCH2170-FROM_DATE").text = today
            session.findById("wnd[0]/usr/ctxtBTCH2170-TO_DATE").text = today
            session.findById("wnd[0]/usr/ctxtBTCH2170-TO_DATE").setFocus()
            session.findById("wnd[0]/usr/ctxtBTCH2170-TO_DATE").caretPosition = 10
            session.findById("wnd[0]/tbar[1]/btn[8]").press()
        
            message1=session.findById("wnd[0]/sbar").text
            print(message1)
            import os
            import time
            if message1=="No job matches the selection criteria":
                time.sleep(2)
                if not os.path.exists(path):
                    os.makedirs(path)
                name=f'{path}/Error sm37- No jobs found.png'
                session.findById("wnd[0]").HardCopy(name, 1)
                no += 1
                #session.findById("wnd[0]/tbar[0]/btn[3]").press()
                continue
                #return
            else:
                #n = job['ABAPNAME'] if 'ABAPNAME' in job else job['JOBNAME']
                if "ABAPNAME" in job:
                    n = job["ABAPNAME"]  # Use ABAP name for last two
                else:
                    n = job["JOBNAME"]
                # Ensure valid file names (remove or replace special characters)
                n = n.replace("*", "_")  # Replace * with _
                session.findById("wnd[0]/mbar/menu[5]/menu[5]/menu[2]/menu[2]").select()
                session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
                session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
                session.findById("wnd[1]/tbar[0]/btn[0]").press()
                session.findById("wnd[1]/usr/ctxtDY_PATH").text = path #"C:\Users\as776099\OneDrive - GSK\Documents\SAP\SAP GUI\"
                name = f'{no}_sm37_{n}_{stamp}.html'
                session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name
                session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
                session.findById("wnd[1]/tbar[0]/btn[11]").press()
                time.sleep(2)
                import pandas as pd

                allcanceled_job = True

                try:
                    html_file_path = os.path.join(path, name)
                    f = pd.read_html(html_file_path, header=0)[0]
                    #f = pd.read_html(path+name, header =0)[0]
                    allcanceled_job = f['Status'].astype(str).str.contains("canceled", case=False).all()
                except Exception as e:
                    print(f"Error reading HTML or checking status: {e}")

                print(f"Processing: JOBNAME = {job.get('JOBNAME', 'N/A')}, ABAPNAME = {job.get('ABAPNAME', 'N/A')} -> Assigned n = {n}")
                #name1=f'{path}/{no} SM37_{n}.png'

                if allcanceled_job:
                    name1 = f'{path}/Error {no} SM37_{n}.png'
                else:
                    name1 = f'{path}/{no} SM37_{n}.png'
                session.findById("wnd[0]").HardCopy(name1, 1)
                try:
                    session.findById("wnd[0]/mbar/menu[5]/menu[11]").select()
                    sname=f'{path}/{no} SM37_{n}_Status.png'
                    session.findById("wnd[1]").HardCopy(sname, 1)
                    session.findById("wnd[1]").close()
                    print(f"Taken Status screenshot of SM37")
                except Exception as e:
                    print("Unable to take Status screenshot of SM37 - {n}:",e) 
        
                #return 
            session.findById("wnd[0]/tbar[0]/btn[3]").press()    
            # except Exception as e:
            #     return{"error": 1, "message" :f"error during selection {e}"}
            #     continue
            no +=1
        return {"status" : 1}       
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
        import datetime
        import time
        today = datetime.datetime.today().strftime("%d.%m.%Y")
        print("Today's date:", today)
        stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        sid = {
            #"RBQ": "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
            #"SBT" : "Z.1.2 - SBT [rixsasap001.sbbio.be]"
            #"SBP" : "Z.0.1 - SBP SYSTEM Restricted - for SAP Basis only",
            "RBP" : "1.1 - RBP - SAP ERP 6.0(R/3) System"
        }

        no = 1
        #path = os.getcwd() + f"\\excel data\\autosap {stamp}\\"
        path = os.path.join(os.getcwd(), f"excel data", f"autosap {stamp}")

        # File download section
        try:
            for system_id in sid:
                session = logon.Autosap(sid[system_id])
                print(sm37(no=no, session=session, stamp=stamp, path=path,today = today))
                print(logon.logof(session))
                #no += 1
        except Exception as e:
            print(f"Error during file download: {e}")

            
    except Exception as e:
        print(f"General error: {e}")
  
