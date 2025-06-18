# ****************************************************************************
#  Program Description : Script to logon SAP                                 *
#  Program Name:  AutoSAPABAPdumps\logon.py                                               *
#          Date:  30/04/2025                                                 *
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

import win32com.client
import subprocess
#import pyautogui as p
from dateutil.relativedelta import relativedelta
import calendar
import cc 
import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import os

env="4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
secret_key = b'Autosap automation python team N'  # 32 bytes (256 bits)
key = secret_key

## Password Decrypting Function ##
# def decrypt_aes256(key, ciphertext):
#     ciphertext = base64.b64decode(ciphertext)
#     iv, ciphertext = ciphertext[:16], ciphertext[16:]
#     cipher = AES.new(key, AES.MODE_CBC, iv=iv)
#     plaintext = unpad(cipher.decrypt(ciphertext), 16).decode()
#     return plaintext

## SAP Logof Function ##
def logof(session):
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nex"
        session.findById("wnd[0]").sendVKey(0)
        return 0

## SAP Logon Function ##
def Autosap(env):
    try:
        #path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"

        # Try both common SAP GUI installation paths
        possible_paths = [
            r"C:\Program Files\SAP\FrontEnd\SAPGUI\saplogon.exe",
            r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
        ]
        saplogon_path = None
        for p in possible_paths:
            if os.path.exists(p):
                saplogon_path = p
                print(f"Using SAP path: {saplogon_path}")
                break

        if not saplogon_path:
            raise FileNotFoundError("SAP Logon executable not found in expected paths.")

        subprocess.Popen(saplogon_path)
        time.sleep(2)
        # subprocess.Popen(path)
        # time.sleep(2)
        SapGuiAuto = win32com.client.GetObject('SAPGUI')
        if not type(SapGuiAuto) == win32com.client.CDispatch:
            return
        application = SapGuiAuto.GetScriptingEngine
        if not type(application) == win32com.client.CDispatch:
            SapGuiAuto = None
            return
        connection = application.OpenConnection(env, True)
        if not type(connection) == win32com.client.CDispatch:
            application = None
            SapGuiAuto = None
            return
        session = connection.Children(0)
        if not type(session) == win32com.client.CDispatch:
            connection = None
            application = None
            SapGuiAuto = None
            return
        #session.findById("wnd[0]/usr/txtRSYST-MANDT").text = "040"
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = cc.asid
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = cc.aspass #decrypt_aes256(key, cc.aspass)
       
        session.findById("wnd[0]").sendVKey(0)
        bar = session.findById("wnd[0]/sbar").text
        print(bar)
        if "Name or password is incorrect (repeat logon)" in bar or "Password logon no longer possible - too many failed attempts" in bar:
            # raise Exception("Sorry,Name or password is incorrect")
            print(("Sorry, Name or password is incorrect"))
            #return [-2,asid,bar]
            return {"status": -2, "asid": cc.asid, "error": bar}

        print("in logon", bar)
        time.sleep(2)
        try :
            session.findById("wnd[1]/usr/radMULTI_LOGON_OPT1").select()
            # session.findById("wnd[1]/usr/radMULTI_LOGON_OPT1").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
        except:
            print("No other session found")
        return session
    except Exception as e:
        print("Logon Error:",str(e))
        return [-1,cc.asid,"Error in LOGON"+str(e)]
        # print("Sorry,Name or password is incorrect")
        # return "In LOGON"+str(e)
    
if __name__ == "__main__":
    print(Autosap(env))
