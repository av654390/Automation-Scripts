# ****************************************************************************
#  Program Description : Script for sm14 tcode                               *
#  Program Name:  RBP\sm14.py                                                *
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
#  1          Developer      erry lavakumar    erry.8.lavakumar@gsk.com     *  
#  2           Developer      akoju sharanya    akoju.x.sharanya@gsk.com     *  
#                                                                            *
# ****************************************************************************

import os
import datetime
import time

def sm14(nos, session, stamp, path,sid=0):
    try:
        # Ensure the directory exists
        if not os.path.exists(path):
            os.makedirs(path)
            
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsm14"
        session.findById("wnd[0]").sendVKey(0)
        name = os.path.join(path, f'{nos} [{sid}] sm14 {stamp}.png')
        session.findById("wnd[0]").hardCopy(name, 1)
        status = session.findById("wnd[0]/usr/tabsFOLDER/tabpUPDATE/ssubSUBSUPDATE:SAPMSM14:1010/txtINFOLINE-INFOTEXT").text
        print(status)
        status_colour = "Active" if status == "Update is active" else "InActive"
        return {"Status": status_colour, "message": "in Sm14"}
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    import logon

    rbq = "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    session = logon.Autosap(rbq)
    nos = 1
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    # Use os.path.join for proper path separator handling
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    
    print(sm14(nos, session, stamp, path))
