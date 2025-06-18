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
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[0]/shellcont/shell/shellcont[0]/shell").selectedNode = "          3"
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[0]/shellcont/shell/shellcont[0]/shell").topNode = "          1"
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").setCurrentCell(15,"_DESCR1")
        fms = session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").GetCellValue(15,"_DESCR1")
        print("Cross Checking FMS:",fms)
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").doubleClickCurrentCell()
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").pressToolbarContextButton("&MB_EXPORT")
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").selectContextMenuItem("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        nfname = f"{nos} [{sid}] ST06 Memory {stamp}.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = nfname
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 12
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        nf = pd.read_html(path+nfname,header=0,decimal=',',thousands='.')[0]
        latest_time=nf[(nf['Date']==nf.loc[0,'Date'])&(nf['Hour']==nf.loc[0,'Hour'])]
        try:
            print("Used memory percentages:",latest_time['User\xa0Utilization[%]'].to_list())
            average_value = latest_time['User\xa0Utilization[%]'].mean()
            # threshold_exceeded = latest_time['Percentage_Used[%]'].between(90, 100)

            print("Average memory Value:", average_value)
            average_memory_usage = round(average_value, 2)
        except:
            print("Used memory percentages:",latest_time['Percentage_Used[%]'].to_list())
            average_value = latest_time['Percentage_Used[%]'].mean()
            # threshold_exceeded = latest_time['Percentage_Used[%]'].between(90, 100)

            print("Average memory Value:", average_value)
            average_memory_usage = round(average_value, 2)

        return {"AvgCPU": average_cpu_usage, "AvgMemory": average_memory_usage}

    except Exception as e:
        print({'error in st06':e})

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
  