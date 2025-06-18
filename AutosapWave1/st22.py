def st22(nos=0, session=0, stamp=0, path=0, sid=0):
    try:
        import datetime
        import os
        import pytz
        from datetime import timedelta
        if not os.path.exists(path):
            os.makedirs(path)
        tz = pytz.timezone('CET')
        current_time = datetime.datetime.now(tz=tz)
        three_hours_ago = current_time - timedelta(hours=3)

        # Format dates and times
        start_date = three_hours_ago.strftime("%d.%m.%Y")
        end_date = current_time.strftime("%d.%m.%Y")
        start_time = three_hours_ago.strftime("%H:%M:%S")
        end_time = current_time.strftime("%H:%M:%S")

        print(f"Start Date: {start_date}, Start Time: {start_time}")
        print(f"End Date: {end_date}, End Time: {end_time}")

        session.findById("wnd[0]/tbar[0]/okcd").text = "/nst22"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/usr/ctxtS_DATUM-LOW").text = start_date
        session.findById("wnd[0]/usr/ctxtS_DATUM-HIGH").text = end_date
        session.findById("wnd[0]/usr/ctxtS_UZEIT-LOW").text = start_time
        session.findById("wnd[0]/usr/ctxtS_UZEIT-HIGH").text = end_time
        session.findById("wnd[0]/usr/txtS_UNAME-LOW").text = "*"
        session.findById("wnd[0]/usr/txtS_UNAME-LOW").setFocus()
        session.findById("wnd[0]/usr/txtS_UNAME-LOW").caretPosition = 1
        session.findById("wnd[0]/usr/btnSTARTSEL").press()
        message1=session.findById("wnd[0]/sbar").text
        print(message1)
        import time
        if message1=="No short dumps match the selection criteria":
            time.sleep(2)
            name=f'{path}/{nos} [{sid}] Dumps {stamp}.png'
            session.findById("wnd[0]").HardCopy(name, 1)
            return {'Dumps_count':0,'status':'Green'}
        session.findById("wnd[0]/usr/cntlRSSHOWRABAX_ALV_100/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
        session.findById("wnd[0]/usr/cntlRSSHOWRABAX_ALV_100/shellcont/shell").selectContextMenuItem ("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        name1 = f"{nos} [{sid}] Dumps {stamp}.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        import pandas as pd
        df=pd.read_html(path+name1,header=0)[0]
        dumps_count=len(df.index)
        print("Dumps_Count :", dumps_count)
        if dumps_count <=10:
            status='Green' 
        elif dumps_count>=10 and dumps_count<=25:
            status='Amber' 
        else:
            status='Red'
        return{"Dumps_Count" : dumps_count}
        #return {'value':dumps_count,'status':status}
    except Exception as e:
        print({'Error in ST22':e})
        return {'value':'Nan','status':'Check Manually'}
    # except Exception as e:
    #     return {"error": 0, "message": f"An error occurred: {e}"}


if __name__ == "__main__":
    try:
        import os
        import datetime
        import logon

        stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        sid = {
            #"BIV": "2.1 - BW Validation [Formal Testing]",
                        "RBQ": "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
        }

        nos = 1
        path = os.getcwd() + f"\excel data\\autosap {stamp}\\"

        # File download section
        try:
            for system_id in sid:
                session = logon.Autosap(sid[system_id])
                print(st22(nos=nos, session=session, sid=system_id, stamp=stamp, path=path))
                print(logon.logof(session))
                nos += 1
        except Exception as e:
            print(f"Error during file download: {e}")

    except Exception as e:
        print(f"General error: {e}")
