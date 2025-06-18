# ****************************************************************************
#  Program Description : Script for ldap tcode                               *
#  Program Name:  RBP\ldap.py                                                *
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
#  1           Developer      erry lavakumar    erry.8.lavakumar@gsk.com     *  
#  2           Developer      akoju sharanya    akoju.x.sharanya@gsk.com     *  
#                                                                            *
# ****************************************************************************

import os
import datetime
import time

def ldap(nos,session,stamp,path,sid=0):
    try:
    
        if not os.path.exists(path):
            os.makedirs(path)

        session.findById("wnd[0]/tbar[0]/okcd").text = "/nldap"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/tbar[1]/btn[20]").press()
        #session.findById("wnd[0]/tbar[1]/btn[38]").press()  #rbq
        name = os.path.join(path, f'{nos} [{sid}] ldap {stamp}.png')
        session.findById("wnd[0]").hardCopy(name, 1)
        #session.findById("wnd[0]/usr/txtSEMSTAT").setFocus()
        status = session.findById("wnd[0]/usr/txtSEMSTAT").IconName
        print(status)
        if status == "S_TL_G":
            status_colour = "Green"
        elif status == "S_TL_Y":
            status_colour = "Amber"
        else:
            status_colour = "Red"
        #status_colour = "green" if status == "S_TL_G" else "red"
        return {"Status": status_colour, "message": "in ldap"}
    except Exception as e:
        return {"Status": "unknown", "message": str(e), "status": "ERROR"}


if __name__ == "__main__":
    import logon
    nbr = "3.1 - NBR - SAP ERP 6.0(R/3) Formal System"
    #rbq = "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    #rbp= "1.1 - RBP - SAP ERP 6.0(R/3) System"
    session = logon.Autosap(nbr)
    nos = 1
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    # Use os.path.join for proper path separator handling
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    
    print(ldap(nos, session, stamp, path))