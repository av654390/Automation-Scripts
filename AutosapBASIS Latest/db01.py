# ****************************************************************************
#  Program Description : Script Performs DB01 T-Code Action in SAP           *
#  Program Name:  AutosapBASIS\db01.py                                       *
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

def db01(nos=0,session=0,path=0,stamp=0):
    try:
        print("\n##### DB01 #####")
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/ndb01"
        session.findById("wnd[0]").sendVKey(0)
        import time
        time.sleep(1)
        name=path+f'{nos} DB01 {stamp}.png'
        session.findById("wnd[0]").HardCopy(name, 1)
        print("DB01: File/Screenshot Saved Successfully!!")
        return name
    except Exception as e:
        print({'Error in DB01':e})
        return "DB01: File/Screenshot Not Saved"