# ****************************************************************************
#  Program Description : Script for smq2cf tcode                               *
#  Program Name:  RBP\smq2cf.py                                                *
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

def smq2cf(nos=7,session=0,stamp=0,path=0,queue="CF*",sid=0):
    # total=[]    
    try:
        total1=-1
        total2=-1
        session.findById("wnd[0]").maximize
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsmq2"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/txtCLIENT").text = "600"
        session.findById("wnd[0]/usr/txtQNAME").text = queue
        session.findById("wnd[0]/usr/txtDPNDNCY").text = ""
        session.findById("wnd[0]/usr/txtQERROR").text = "x"
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        try:
            total1 = session.findById("wnd[0]/usr/lbl[36,2]").text.replace(".","")
            session.findById("wnd[0]/usr/lbl[36,2]").caretPosition = 12
            # session.findById("wnd[0]").sendVKey 2)
            total2 = session.findById("wnd[0]/usr/lbl[36,3]").text.replace(".","")
            session.findById("wnd[0]/usr/lbl[36,3]").caretPosition = 11
            # session.findById("wnd[0]").sendVKey 2
        except Exception as e:
            print(f"eror in smq1 {e}")
        session.findById("wnd[0]/mbar/menu[4]/menu[5]/menu[2]/menu[2]").select()
        session.findById("wnd[0]/mbar/menu[4]/menu[5]/menu[2]/menu[2]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        # session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = f"{nos} [{sid}] smq2 {stamp}.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 7
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        # print(int(total1),int(total2))
        return {"total":int(total1),"error":int(total2),"message":"in smq2cf"}

    except Exception as e:
        return {"error":0,"message":f"error in smq2cf {e}"}
    # finally:
    #     pass
        # f"smq2 redo {stamp}.html"
if __name__ == "__main__":
    import os
    import logon
    import sys
    import datetime
    rbq= "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    session=logon.Autosap(rbq)
    nos=7
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # tempdir= f"autosap {stamp}"
    path=os.getcwd()+f"\excel data\\autosap {stamp}\\"
    os.mkdir(path)
    sys.stdout=open(path+"LOG"+stamp+".txt","w")
    print(smq2cf(nos,session,stamp,path,queue="CF*"))