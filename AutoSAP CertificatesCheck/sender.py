# ****************************************************************************
#  Program Description : Script Triggers Mail Notification                   *
#  Program Name:  AutosapLOGS/sender.py                                      *
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

import smtplib
from os.path import basename
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import COMMASPACE, formatdate


def send_mail(send_from, send_to, send_cc, subject, text, path=None,html=None):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Cc'] = COMMASPACE.join(send_cc)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    print("Mail Sent To:")
    print(msg['To'],msg['Cc'],'/n')
    html=open(html,"r").read()
    if html !=None:
        part2 = MIMEText(html, 'html')
        
    msg.attach(part2)
    for f in os.listdir(path) or []:
        print(f)
        newpath = path+"\\"+f
        if os.path.isdir(newpath):
            for sf in os.listdir(newpath):
                fi = os.path.getsize(newpath+"\\"+sf)
                fi = fi / (1024 * 1024)
                if fi < 20 and (sf.lower().endswith(".png")):    
                    with open(newpath+"\\"+sf, "rb") as fil:
                        part = MIMEApplication(
                            fil.read(),
                            Name=basename(sf)
                        )
                    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(sf)
                    msg.attach(part)
    host = 'internal-smtp.gsk.com'
    port = 25        
    smtp = smtplib.SMTP(host,port)
    smtp.send_message(msg)
    print("MAIL SENT SUCCESSFULLY")
    smtp.close()

if __name__ == "__main__":
    frm =  "erry.8.lavakumar@gsk.com"
    to= ["erry.8.lavakumar@gsk.com","nikhil.x.chalikwar@gsk.com","akoju.x.sharanya@gsk.com"]
    cc =  ["erry.8.lavakumar@gsk.com"]
    subject="hi hello test"
    bdy="test mail"
    file_path=r"C:\Users\el491900\OneDrive - GSK\Desktop\scripts\venv\AutosapBASIS\excel data\AutoSAP_2024-05-21-16-15-45\\"
    html=r"C:\Users\el491900\OneDrive - GSK\Desktop\scripts\venv\AutosapBASIS\excel data\AutoSAP_2024-05-21-16-15-45\AutoSAP_html_summary_2024-05-21-16-15-45.html"
    send_mail(send_from=frm, send_to=to, send_cc=cc, subject=subject, text=bdy, files=file_path,html=html)