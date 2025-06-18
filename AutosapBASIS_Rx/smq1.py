# ****************************************************************************
#  Program Description : Script for smq1 tcode                               *
#  Program Name:  RBP\smq1.py                                                *
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




def smq1(nos=4,session=0,stamp=0,path=0,queue="SAP_ALE_YAMMES*",sid=0):
    # total=[]    
    try:
        total1=-1
        total2=-1
        session.findById("wnd[0]").maximize
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsmq1"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/txtCLIENT").text = "600"
        session.findById("wnd[0]/usr/txtQNAME").text = queue
        session.findById("wnd[0]/usr/ctxtQDEST").text = "*"
        session.findById("wnd[0]/usr/txtQERROR").text = "x"
        # session.findById("wnd[0]/usr/txtQERROR").setFocus
        # session.findById("wnd[0]/usr/txtQERROR").caretPosition = 1
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        # try :
        #     total2=session.findById("wnd[0]/usr/lbl[2,1]").text
        #     if "Nothing selected".lower() in total2.lower():
        #         total2=0
        #     print(total2,"sap ale yammies1")
        # except Exception as e:
        #     print(f"eror in smq1 {e}")

        try :
            total1=session.findById("wnd[0]/usr/lbl[36,2]").text.replace(".","")
            total2=session.findById("wnd[0]/usr/lbl[36,3]").text.replace(".","") 
        except Exception as e:
            print(f"eror in smq1 {e}")
        # session.findById("wnd[0]/usr/lbl[36,3]").caretPosition = 10
        # session.findById("wnd[0]").sendVKey 2
        session.findById("wnd[0]/mbar/menu[4]/menu[5]/menu[2]/menu[2]").select()
        session.findById("wnd[0]/mbar/menu[4]/menu[5]/menu[2]/menu[2]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        # session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = f"{nos} [{sid}] smq1 {stamp}.html"
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        # print(int(total1),int(total2))
        return {"total":int(total1),"error":int(total2),"message":"in smq1"}

    except Exception as e:
        return {"error":0,"message":f"check file once in smq1 {e}"}
    # finally:
    #     pass
        # f"smq1 redo {stamp}.html"
if __name__ == "__main__":
    import os
    import sys
    import logon
    import datetime
    rbq= "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    session=logon.Autosap(rbq)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    path = os.getcwd() + f"\excel data\\autosap {stamp}\\"
    os.mkdir(path)
    #path=os.getcwd()+f"\excel data\\autosap {stamp}\\"
    sys.stdout = open(path + "LOG" + stamp + ".txt", "w")
    nos=4
    print(smq1(nos,session,stamp,path,queue="SAP_ALE_YAMMES*"))
