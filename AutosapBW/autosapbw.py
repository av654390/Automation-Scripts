# ****************************************************************************
#  Program Description : Script Performs BW-QM Reconsoliation Task           *
#  Program Name:  AutosapBW\autosapbw.py                                     *
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
#  2           Developer      Erry Lavakumar    erry.8.lavakumar@gsk.com     *  
#  2           Developer      Akoju Sharanya    akoju.x.sharanya@gsk.com     *  
#                                                                            *
# ****************************************************************************

# Import User Defined Modules/Files #
import cc
import logon
import source
import target
import targetsap
import excel_report
import sender

# Import Required Existing Modules/Libraries #
import os
import sys
from datetime import datetime, timedelta

sid={'sbt':"1.2 - R/3 Acceptance [Informal Testing]",'bit':"2.2 - BW Test [Informal Testing]"}
now=datetime.now()
stamp=now.strftime("%Y-%m-%d-%H-%M-%S")
cd=os.getcwd()
path = cd + f'/excel data/AutoSAP_{stamp}/'

# Finding Required Days/Dates #
ftoday=datetime.today()
fyesterday=ftoday-timedelta(days=1)
ffirstday_of_month=fyesterday.replace(day=1)
today=ftoday.strftime('%d.%m.%Y')
yesterday=fyesterday.strftime('%d.%m.%Y')
firstday_of_month=ffirstday_of_month.strftime('%d.%m.%Y')
daterange='01.01.2023 - 31.01.2023'
daterange=f'{firstday_of_month} - {today}'

# Step 1 : Login to Source(SBP) and Download the Source Inspection Lots
session=logon.Autosap(sid['sbt']) 
sbt_file=source.source(nos=0,session=session,path=path,stamp=stamp,d1=firstday_of_month,d2=yesterday)
print("# Step 1 Completed : Login to Source(SBP) and Download the Source Inspection Lots, File Name:",sbt_file)

# Step 2 : Download the Target Inspection Lots from JAVA PORTAL
target.target(path=path,daterange=daterange,stamp=stamp)
print("# Step 2 Completed : Download the Target Inspection Lots from JAVA PORTAL")

# Step 3 : Combine and Analyze the Source and Target Inspection Lots
source_lots=excel_report.gen(nos=0,session=session,path=path,stamp=stamp,sbt_file=sbt_file)
print("# Step 3 Completed : Combine and Analyze the Source and Target Inspection Lots")
print("Source Inspection Lots:",source_lots)

# Step 4 : Take the Screenshot of Sum of X in Source
source.se16(nos=0,session=session,path=path,stamp=stamp,reason='sum',dict1=source_lots)
logon.logof(session)
print("# Step 4 Completed : Take the Screenshot of Sum of X in Source")

# Step 5 : Take the Screenshot of Sum of X in Target
session=logon.Autosap(sid['bit'])
targetsap.targetsap(nos=0,session=session,path=path,stamp=stamp,dict1=source_lots)
logon.logof(session)
print("# Step 5 Completed : Take the Screenshot of Sum of X in Target")

# Step 6 : Send Mail With Reports
frm =  "noreply-autosapautomation@gsk.com"
to= ["erry.8.lavakumar@gsk.com","nikhil.x.chalikwar@gsk.com","akoju.x.sharanya@gsk.com"]
cc =  ["erry.8.lavakumar@gsk.com"]
subject=f"AutoSAP BW QM-Reconsoliation {stamp}"
bdy="test mail"
html="BW.html"
sender.send_mail(send_from=frm, send_to=to, send_cc=cc, subject=subject, text=bdy, path=path,html=html)
print("# Step 6 Completed : Send Mail With Reports")
