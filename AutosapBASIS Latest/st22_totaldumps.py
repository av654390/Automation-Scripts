# *****************************************************************************
#  Program Description : downloads the dumps report from st22T-code           *
#  Program Name:  AutoSAPABAPdumps/st22.py                                    *
#          Date:  21/06/2024                                                  *
#       Version:  1.0.0                                                       *
#        Author:  Erry Lavakumar                                              *
#  Return Codes:                                                              *
#                 0 - Success                                                 *
#                 1 - Error check log file                                    *
# *****************************************************************************
#  AutoSAP Automation                                                         *
#  --------------------                                                       *
#  Sr.         Role           Member           Email                          *
#  ---------   ----------     --------------   ------------------------------ *
#  1           Developer      Nikhil Chalikwar  nikhil.x.chalikwar@gsk.com    *
#  2           Developer      Erry Lavakumar    erry.8.lavakumar@gsk.com      *
#  3           Developer      Akoju Sharanya    akoju.x.sharanya@gsk.com      *
# *****************************************************************************

def st22(nos=0,session=0,system_id=0,stamp=0,path=0):
    try:
        import datetime
        # Get today's date
        today_date = datetime.datetime.now().strftime("%d.%m.%Y")
        # Calculate the time range for the last 3 hours
        current_time = datetime.datetime.now()
        low_time = (current_time - datetime.timedelta(hours=3)).strftime("%H:%M:%S")
        high_time = current_time.strftime("%H:%M:%S")

        session.findById("wnd[0]/tbar[0]/okcd").text = "/nst22"
        session.findById("wnd[0]").sendVKey (0)
        session.findById("wnd[0]/mbar/menu[2]/menu[1]").select()
        session.findById("wnd[0]/usr/ctxtS_DATUM-LOW").text = today_date
        #session.findById("wnd[0]/usr/ctxtS_DATUM-HIGH").text = today_date
        # session.findById("wnd[0]/usr/ctxtS_UZEIT-LOW").text = low_time
        # session.findById("wnd[0]/usr/ctxtS_UZEIT-HIGH").text = high_time
        session.findById("wnd[0]/usr/ctxtS_UZEIT-HIGH").setFocus()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/mbar/menu[3]/menu[5]/menu[2]/menu[2]").select()
        #session.findById("wnd[0]/mbar/menu[3]/menu[5]/menu[2]/menu[1]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        dname=f"{nos} ST22 Total Dumps {stamp}.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = dname
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        import pandas as pd
        f= pd.read_html(path+dname,header=1)[0]
        a=[]
        for i in f['Runtime\xa0Errors Number']: 
            j = str(i).split()
            if j[-1].isdigit(): 
                a.append(int(j[-1]))  # Convert it to an integer and append to the list
        total_dumps = sum(a)

        if total_dumps <100:
            status='Green' 
        elif total_dumps>=100 and total_dumps<=200:
            status='Amber' 
        else:
            status='Red'
        return {'value':total_dumps,'status':status}
    except Exception as e:
        return {"error": 0, "message": f"An error occurred in : {e}"}

if __name__ == "__main__":
    try:
        import os
        import datetime
        import logon
        stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        system_ids = {"SBT":"1.2 - R/3 Acceptance [Informal Testing]"}

        nos = 1
        path = os.getcwd() + f"\excel data\\autosap {stamp}\\"
        
        # File download section
        try:
            for system_id in system_ids:
                session = logon.Autosap(system_ids[system_id])
                print(st22(nos=nos, session=session, system_id=system_id, stamp=stamp, path=path))
                print(logon.logof(session))
                nos += 1
        except Exception as e:
            print(f"Error during file download: {e}")

            
    except Exception as e:
        print(f"General error: {e}")
  