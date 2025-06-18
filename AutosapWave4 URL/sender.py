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


def send_mail(send_from, send_to, send_cc, subject, text, files=None,html=None):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Cc'] = COMMASPACE.join(send_cc)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    print(msg['To'],msg['Cc'])
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

if __name__ == "__main__":
    frm =  "nikhil.x.chalikwar@gsk.com"
    to= ["preetham.x.aranha@gsk.com","aswin.x.johncherian@gsk.com"]
    cc =  ["nikhil.x.chalikwar@gsk.com"]
    subject="hi hello test"
    bdy="test mail"
    file_path=r"C:\Users\nc843765\OneDrive - GSK\NKISLIVE\thecode"
    send_mail(send_from=frm, send_to=to, send_cc=cc, subject=subject, text=bdy, files=file_path)