def st06(nos=0, session=0, path=0, stamp=0, sid=0):
    try:
        # Maximize the SAP GUI window and navigate to ST06 transaction
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nst06"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[0]/shellcont/shell/shellcont[0]/shell").selectedNode = "          3"
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[0]/shellcont/shell/shellcont[0]/shell").topNode = "          3"
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").pressToolbarContextButton("&MB_EXPORT")
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").selectContextMenuItem("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        
        # Set the file path and name for the export
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        fname = f"{nos} [{sid}] ST06 {stamp}.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = fname
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = len(fname)
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        # Read the exported HTML into a DataFrame
        import pandas as pd
        df = pd.read_html(path + fname, header=0)[0]

        # Dynamically construct the application server ID based on the SID
        application_server_id = df["Application\xa0Server"][0]

        cpu_idle = df.loc[
            (df['Application\xa0Server'].str.contains(application_server_id)) &
            (df['Monitoring\xa0Category'] == 'CPU') &
            (df['Description'] == 'Idle'),
            'Value'
        ]
       
        free_memory = df.loc[
            (df['Application\xa0Server'].str.contains(application_server_id)) &
            (df['Monitoring\xa0Category'] == 'Memory') &
            (df['Description'] == 'Free\xa0memory'),
            'Value'
        ]

        # Convert values to float with fallback
        average_cpu = float(cpu_idle.iloc[0]) if not cpu_idle.empty else None
        print(f"Average CPU Idle : {average_cpu}")
        average_memory = float(free_memory.iloc[0]) if not free_memory.empty else None

        # Subtract CPU idle from 100 to get CPU usage
        average_cpu_usage = 100 - average_cpu if average_cpu is not None else None

        return {"AvgCPU": average_cpu_usage, "AvgMemory": average_memory}

    except Exception as e:
        return {"error": 1, "message": f"An error occurred in st06: {e}"}

if __name__ == "__main__":
    try:
        import os
        import datetime
        import logon

        stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        sid = {
            "BIV": "2.1 - BW Validation [Formal Testing]",
            #"RBQ": "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
        }

        nos = 1
        path = os.getcwd() + f"\excel data\\autosap {stamp}\\"

        # File download section
        try:
            for system_id in sid:
                session = logon.Autosap(sid[system_id])
                print(st06(nos=nos, session=session, sid=system_id, stamp=stamp, path=path))
                print(logon.logof(session))
                nos += 1
        except Exception as e:
            print(f"Error during file download: {e}")

    except Exception as e:
        print(f"General error: {e}")
