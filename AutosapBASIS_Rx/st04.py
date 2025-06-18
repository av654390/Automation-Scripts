# ****************************************************************************
#  Program Description : Script for st04 tcode                               *
#  Program Name:  RBP\st04.py                                                *
#          Date:  08/05/2024                                                 *
#       version:  1.0.0                                                      *
#        Author:  Sharanya Akoju                                             *
#  Return Codes:                                                             *
#                 0 - Success                                                *
#                 1 - Error check log file                                   *
# ****************************************************************************
#  AutoSAP Automation                                                        *
#  --------------------                                                      *
#  Sr.         Role           Member          Email                          *
#  ---------   ----------     --------------  -------------------------------*
#  1           Developer      NIKHIL CHALIKWAR  nikhil.x.chalikwar@gsk.com   *
#  2           Developer      erry lavakumar    erry.8.lavakumar@gsk.com     *  
#  2           Developer      akoju sharanya    akoju.x.sharanya@gsk.com     *  
#                                                                            *
# ****************************************************************************

import os
def st04(nos=8,session=0,stamp=0,path=0,sid=0):    
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nst04"
        session.findById("wnd[0]").sendVKey(0)
        name = os.path.join(path, f'{nos} [{sid}] st04 {stamp}.png')
        session.findById("wnd[0]").hardCopy(name, 1)
        status=session.findById("wnd[0]/usr/txtHDB_OVERVIEW-STATE_ICON").IconName
        # print(status)
        # if status in "   S_TL_G   ":
        #     status_colour = "green"
        # else  : 
        #     status_colour = "red"
        # print(status_colour)
        ##or##
        status_colour = "Green" if status == "S_TL_G" else "Red"
        return {"Status": status_colour, "message": "in ST04", "status": "REPLICATION ACTIVE"}
    except Exception as e:
        return {"Status": "unknown", "message": str(e), "status": "ERROR"}


if __name__ == "__main__":
    import os
    import logon
    import datetime
    rwq= "4.5 - RWQ - SAP BW Informal System"
    session=logon.Autosap(rwq)
    nos=8
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # tempdir= f"autosap {stamp}"
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    print(st04(nos,session,stamp,path))
