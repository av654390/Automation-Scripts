# ****************************************************************************
#  Program Description : Script checks cif jobs                              *
#  Program Name:  logon.py                                                   *
#          Date:  08/05/2024                                                 *
#       version:  1.0.0                                                      *
#        Author:  Nikhil Chalikwar                                           *
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
import win32com.client
# import sys
import subprocess
from dateutil.relativedelta import relativedelta
# import calendar
import cc 
import time

# import datetime
# import pandas as pd

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def decrypt_aes256(key, ciphertext):
    ciphertext = base64.b64decode(ciphertext)
    iv, ciphertext = ciphertext[:16], ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), 16).decode()
    return plaintext
credit = b'Autosap automation python team N'
env="1.2 - R/3 Acceptance [Informal Testing]"
# env="A.2 - eWM Test [Informal Testing]"   #wmt
secret_key = credit
def logof(session):
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nex"
        session.findById("wnd[0]").sendVKey(0)
        # session.findById("wnd[0]/tbar[0]/okcd").text = "/nex"
        # session.findById("wnd[0]").sendVKey(0)
        return 0

def Autosap(env):
    try:
        path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
        subprocess.Popen(path)
        time.sleep(2)
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
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = cc.elkid
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = decrypt_aes256(secret_key,cc.elkpass)
        session.findById("wnd[0]").sendVKey(0)
        bar = session.findById("wnd[0]/sbar").text
        print(bar)
        if "Name or password is incorrect (repeat logon)" in bar or "Password logon no longer possible - too many failed attempts" in bar :
            raise Exception("Sorry, Name or password is incorrect")
        print("in logon ",bar)
        time.sleep(2)
        try :
            session.findById("wnd[1]/usr/radMULTI_LOGON_OPT1").select()
            # session.findById("wnd[1]/usr/radMULTI_LOGON_OPT1").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
        except:
            print("No other session found")
        print(session,str(type(session)))
        a="<class 'win32com.client.CDispatch'>"==str(type(session))
        if a:
            return session
        print("session not started")
        # session.findById("wnd[0]/tbar[0]/okcd").text = "/nsmq2"
        # session.findById("wnd[0]").sendVKey(0)
        return session
    except Exception as e:
        return "In LOGON"+str(e)
    
if __name__ == "__main__":
    print(Autosap(env))