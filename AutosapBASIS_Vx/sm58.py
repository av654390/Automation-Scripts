# ****************************************************************************
#  Program Description : Script Performs SM58 T-Code Action in SAP           *
#  Program Name:  AutosapBASIS\sm58.py                                       *
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

def sm58(nos=0,session=0,path=0,stamp=0,td=0):
    try:
        print("\n##### SM58 #####")
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsm58"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtZEITRAUM-LOW").text = td #"20.05.2024" #today's date
        session.findById("wnd[0]/usr/ctxtZEITRAUM-HIGH").text =td # "20.05.2024"
        session.findById("wnd[0]/usr/txtBENUTZER-LOW").text = "*"
        session.findById("wnd[0]/usr/txtBENUTZER-LOW").setFocus()
        session.findById("wnd[0]/usr/txtBENUTZER-LOW").caretPosition = 1
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        import time
        time.sleep(1)
        name=f'{path}/{nos} SM58 {stamp}.png'
        session.findById("wnd[0]").HardCopy(name, 1)
        print("SM58 : File/Screenshot Saved Successfully!!")
        return name
    except Exception as e:
        print({'Error in SM58':e})
        return " SM58 : File/Screenshot Not Saved"