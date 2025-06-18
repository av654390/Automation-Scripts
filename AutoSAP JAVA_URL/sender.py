# ****************************************************************************
#  Program Description : Script for SMPTP mail                               *
#  Program Name:  sender.py                                                  *
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
import smtplib
from os.path import basename
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(send_from, send_to, send_cc, send_bcc, subject, text, files=None,html=None):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Cc'] = COMMASPACE.join(send_cc)
    msg['Bcc'] = COMMASPACE.join(send_bcc)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    print(msg['To'],msg['Cc'],msg['Bcc'])
    # msg.attach(MIMEText(text))
    # part1 = MIMEText(text, 'plain')
    html=open(html,"r").read()
    if html !=None:
        part2 = MIMEText(html, 'html')
    # msg.attach(part1)
    msg.attach(part2)

    for f in os.listdir(files) or []:
        print(f)
        if f.lower().endswith(".html"):    
            with open(files+"\\"+f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)
        # else : print(f)
        # After the file is closed

    host = 'internal-smtp.gsk.com'
    port = 25        
    smtp = smtplib.SMTP(host,port)
    # smtp = smtplib.SMTP(server)
    # smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.send_message(msg)
    smtp.close()

def error_mail(lid, err, sid):
    try:
        # assert isinstance(send_to, list)
        import platform
 
        def print_device_info():
            a=""
            a+=f"System: {platform.system()}\n"
            a+=f"Device name: {platform.node()}\n"
            a+=f"Release: {platform.release()}\n"
            a+=f"Version: {platform.version()}\n"
            a+=f"Machine: {platform.machine()}\n"
            a+=f"Processor: {platform.processor()}\n"
            return a
        device_info=print_device_info()
        msg = MIMEMultipart('alternative')
        msg['From'] = "noreply-autosapautomation@gsk.com"
        msg['To'] = "shiva.x.prasad@gsk.com,akash.verma@gsk.com"
        msg['Cc'] = "shiva.x.prasad@gsk.com"
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = f"Logon Error occured AutoSAP URL Monitoring {formatdate(localtime=True)}"
 
        host = 'internal-smtp.gsk.com'
        port = 25
        if 1:
            body=f'''<table style="width: 100%; border-collapse: collapse;">
                <tr>
                    <td style="text-align: center;">
                        <img src="https://th.bing.com/th/id/OIP.biM9O9rkMc-40mI_3TsPxwAAAA?rs=1&pid=ImgDetMain" width="170" width="170" height="70" alt="Bing Logo">
                    </td>
 
                <tr>
                    <td style="padding: 0; text-align: center;">
                        <div style="background: #F36633; width: 80px; height: 150px; margin: auto; display: flex; align-items: center; justify-content: center;">
                            <strong><span class="content" style="font-size: 24px;">AutoSAP URL Monitoring</span></strong>
                        </div>
                    </td>
                </tr>
 
            </table>
            <br>
            <h3>Hello Team,<h3>
            <p>Automation faced a technical error while login!<p>
            <br>
            <pre>Login ID : {lid} </pre>
            <pre>System ID : {sid} </pre>
            <pre>Error Message : {err} </pre>
            <pre>{device_info} </pre>
            '''
        
        part2 = MIMEText(body, 'html')
        msg.attach(part2)
        with smtplib.SMTP(host, port) as smtp:
            smtp.send_message(msg)
            print("Mail sent!")
    except Exception as e:
        return{"error":0,"message":f"error in sender {e}"}                                                                                                                                                                                                                                                                                    
    

if __name__ == "__main__":
    frm =  "nikhil.x.chalikwar@gsk.com"
    to= ["preetham.x.aranha@gsk.com","aswin.x.johncherian@gsk.com"]
    cc =  ["nikhil.x.chalikwar@gsk.com"]
    subject="hi hello test"
    bdy="test mail"
    file_path=r"C:\Users\nc843765\OneDrive - GSK\NKISLIVE\thecode"
    send_mail(send_from=frm, send_to=to, send_cc=cc, subject=subject, text=bdy, files=file_path)