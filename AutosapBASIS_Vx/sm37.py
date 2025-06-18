# ****************************************************************************
#  Program Description : Script Performs SM37 T-Code Action in SAP           *
#  Program Name:  AutosapBASIS\sm37.py                                       *
#          Date:  21/06/2024                                                 *
#       version:  1.0.0                                                      *
#        Author:  Erry Lavakumar                                             *
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

def sm37(nos=0,session=0,path=0,stamp=0,dt=0):
    try:
        print("\n##### SM37 #####")
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsm37"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/chkBTCH2170-SCHEDUL").selected = False
        session.findById("wnd[0]/usr/chkBTCH2170-READY").selected = False
        session.findById("wnd[0]/usr/chkBTCH2170-FINISHED").selected = False
        session.findById("wnd[0]/usr/chkBTCH2170-ABORTED").selected = False
        session.findById("wnd[0]/usr/txtBTCH2170-JOBNAME").text = "*"
        session.findById("wnd[0]/usr/txtBTCH2170-USERNAME").text = "*"
        session.findById("wnd[0]/usr/ctxtBTCH2170-FROM_DATE").text = ""
        print("DATEE",dt)
        session.findById("wnd[0]/usr/ctxtBTCH2170-TO_DATE").text = dt #Yesterday Date
        session.findById("wnd[0]/usr/ctxtBTCH2170-TO_DATE").setFocus()
        session.findById("wnd[0]/usr/ctxtBTCH2170-TO_DATE").caretPosition = 10
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        message1=session.findById("wnd[0]/sbar").text
        print(message1)
        import time
        if message1=="No job matches the selection criteria":
            time.sleep(2)
            name=f'{path}/{nos} SM37 {stamp}.png'
            session.findById("wnd[0]").HardCopy(name, 1)
            print("SM37 : File/Screenshot Saved Successfully!!")
            return {'value':0,'status':'Green','path':name}
        else:
            time.sleep(2)
            name=f'{path}/{nos} SM37 {stamp}.png'
            session.findById("wnd[0]").HardCopy(name, 1)
            print("SM37 : File/Screenshot Saved Successfully!!")
            return {'value':1,'status':'Red','path':name}
    except Exception as e:
        print({"Error in SM37":e})
        return {'value':'Nan','status':'Check Manually','path':"File/Screenshot Not Saved"}
