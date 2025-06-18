def al08(nos, session, sid, stamp, path):
    try:
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nal08"
        session.findById("wnd[0]").sendVKey (0)
        try :
            session.findById("wnd[1]").close()
        except Exception as e :
            print(f"{e} causion window did not came in al08")
        session.findById("wnd[0]/tbar[1]/btn[9]").press()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = f"{nos} [{sid}] dialogueusers {stamp}.txt"
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        import pandas as pd
        import re
        # table = path+f"{nos} [{sid}] dialogueusers {stamp}.html"
        # df = pd.read_html(table,header=0)[0]
        # dialogueusers = len(df.index)
        # return {"Users" : dialogueusers}

        table = path+f"{nos} [{sid}] dialogueusers {stamp}.txt"
        df=pd.read_csv(table,header=None)
        userlogon = df.iloc[-1,0] # Get the last row, first column
        print("User Logon Line:", userlogon)
        first_number = re.search(r'\d+', userlogon).group()
        return {"Users" : int(first_number)} 

    except Exception as e:
        return {"error": 0, "message": f"An error occurred in al08: {e}"}

if __name__ == "__main__":
    try:
        import os
        import datetime
        import logon
        stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        sid = {"WMP" :"0.9 - eWM Production","HRP": "0.6 - HR Production","BIP" : "0.2 - BW Production"
        }
        nos = 1
        path = os.getcwd() + f"\excel data\\autosap {stamp}\\"
        # File download section
        try:
            for system_id in sid:
                session = logon.Autosap(sid[system_id])
                print(al08(nos=nos, session=session, sid=system_id, stamp=stamp, path=path))
                print(logon.logof(session))
                nos += 1
        except Exception as e:
            print(f"Error during file download: {e}")
    except Exception as e:
        print(f"General error: {e}")
  