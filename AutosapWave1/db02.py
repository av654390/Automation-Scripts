def db02(nos=0, session=0, sid=0, stamp=0, path=0):
    import os
    try:
        if not os.path.exists(path):
            os.makedirs(path)
                
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/ndb02"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").hierarchyHeaderWidth = 201
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").expandNode ("        100")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").topNode = ("        100")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").selectItem ("        101","Task")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").ensureVisibleHorizontalItem ("        101","Task")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").doubleClickItem ("        101","Task")
        name = os.path.join(path, f'{nos} [{sid}] db02 {stamp}.png')
        session.findById("wnd[0]").hardCopy(name, 1)
        session.findById("wnd[0]/usr/txtHDB_OVERVIEW-LABEL_DB_CPU").setFocus()
        status = session.findById("wnd[0]/usr/txtHDB_OVERVIEW-STATE_ICON").IconName
        print(status)
        if status == "S_TL_G":
            status_colour = "Green"
        elif status == "S_TL_Y":
            status_colour = "Amber"
        else:
            status_colour = "Red"

        session.findById("wnd[0]").sendVKey (2)
        session.findById("wnd[0]/usr/cntlSERVICES_ALV_CONTAINER/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
        session.findById("wnd[0]/usr/cntlSERVICES_ALV_CONTAINER/shellcont/shell").selectContextMenuItem ("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        name = f"{nos} [{sid}] db02_CPU {stamp}.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        import pandas as pd
        import numpy as np
        df2=pd.read_html(path+name,header=0)[0]
        DB_CPU_Utilization = df2['Total\xa0CPU\xa0(%)']
        DB_CPU_Utilization_cleaned = (
            DB_CPU_Utilization.str.replace("-", "", regex=False)  # Remove dashes
            .replace("", np.nan)  # Replace empty strings with NaN
            .astype(float)  # Convert to float
        )
        average_cpu_db = round(DB_CPU_Utilization_cleaned.mean(),2)
        print("Average_CPU_Utilization:", average_cpu_db)

        # if average_cpu_db <=90:
        #     status='Green' 
        # elif average_cpu_db>=90 and average_cpu_db<=95:
        #     status='Amber' 
        # else:
        #     status='Red'
        return {"cpumemory":average_cpu_db,"replicationstatus": status_colour}
        #return {"cpumemory":{'value':average_cpu_db,'status':status},"replicationstatus":{'Status': status_colour}}

    except Exception as e:
        print({'error in DB02':e})
        return {'Check Manually':{'value':'Nan','status':'Check Manually'}}
    
if __name__ == "__main__":
    try:
        import os
        import datetime
        import logon
        stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        sid = {"BIV": "2.1 - BW Validation [Formal Testing]",
        "RWQ": "4.5 - RWQ - SAP BW Informal System",
        }
        nos = 1
        path = os.getcwd() + f"\excel data\\autosap {stamp}\\"
        # File download section
        try:
            for system_id in sid:
                session = logon.Autosap(sid[system_id])
                print(db02(nos=nos, session=session, sid=system_id, stamp=stamp, path=path))
                print(logon.logof(session))
                nos += 1
        except Exception as e:
            print(f"Error during file download: {e}")
    except Exception as e:
        print(f"General error: {e}")
