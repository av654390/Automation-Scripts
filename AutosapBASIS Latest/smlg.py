# ****************************************************************************
#  Program Description : Script Performs SMLG T-Code Action in SAP           *
#  Program Name:  AutosapBASIS\smlg.py                                       *
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

def smlg(nos=0,session=0,path=0,stamp=0):
    try:
        print("\n##### SMLG #####")
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsmlg"
        session.findById("wnd[0]").sendVKey(0)
        try :
            session.findById("wnd[1]/tbar[0]/btn[0]").press()

        except Exception as e :
            print(e,"Table not locked in smlg")
 
        import time
        time.sleep(1)
        name=f'{path}/{nos} SMLG {stamp}.png'
        session.findById("wnd[0]").HardCopy(name, 1)
        print("SMLG : File/Screenshot Saved Successfully!!")
        return name
    except Exception as e:
        print({'Error in SMLG':e})
        return "SMLG : File/Screenshot Not Saved"