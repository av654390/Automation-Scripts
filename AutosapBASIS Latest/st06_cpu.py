def st06(nos,session,stamp,path,sid):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nst06"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[0]/shellcont/shell/shellcont[0]/shell").selectedNode = "          3"
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[0]/shellcont/shell/shellcont[0]/shell").topNode = "          3"
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").pressToolbarContextButton("&MB_EXPORT")
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").selectContextMenuItem("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        fname = f"{nos} [{sid}] ST06 {stamp}.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = fname
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = len(fname)
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        import pandas as pd
        import numpy as np
        f = pd.read_html(path + fname, header=0)[0]

        try:
            cpu_idle_value = pd.to_numeric(f.loc[(f['Monitoring\xa0Category'] == 'CPU') & (f['Description'] == 'Idle'),'Value'], errors='coerce').values
            cpu_used_value = 100 - cpu_idle_value
        except:
            cpu_idle_value = pd.to_numeric(f.loc[(f['Category'] == 'CPU') & (f['Description'] == 'Idle'),'Value'], errors='coerce').values
            cpu_used_value = 100 - cpu_idle_value
        
        

        print("CPU Idle Values:", cpu_idle_value)
        print("CPU Used Values:", cpu_used_value)

        # cpu_threshold_exceeded = cpu_used_value.between(85, 100)
        average_value = cpu_used_value.mean()
        print("Average CPU Used Value:", average_value)
        average_cpu_usage = round(average_value, 2)


        # try:
        #     freememory_value = pd.to_numeric(f.loc[(f['Category'] == 'Memory') & (f['Description'] == 'Free\xa0memory\xa0percentage'),'Value'], errors='coerce').values
        # except:
        #     freememory_value = pd.to_numeric(f.loc[(f['Monitoring\xa0Category'] == 'Memory') & (f['Description'] == 'Free\xa0memory\xa0percentage'),'Value'], errors='coerce').values

        # print("Free memory percentages:", freememory_value)
        
        # average_value = freememory_value.mean()
        # print("Average memory Value:", average_value)
       
        if average_cpu_usage<85:
            status='Green'
        elif average_cpu_usage>=85 and average_cpu_usage<95:
            status='Amber'
        elif average_cpu_usage>=95:
            status='Red'
        return {"AvgCPU": {"value":average_cpu_usage,"status":status}}

    except Exception as e:
        print({'Error in ST06 CPU':e})
        return {'value':'Nan','status':'Check Manually'}


if __name__ == "__main__":
    try:
        import os
        import datetime
        import logon
        stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        sid = {
            "BIV": "2.1 - BW Validation [Formal Testing]"
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
  