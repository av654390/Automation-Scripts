# ****************************************************************************
#  Program Description : Script to read credentials                           *
#  Program Name:  AutoSAP SD PostFunChecks/cc.py                              *
#          Date:  15/05/2025                                                  *
#       Version:  1.0.0                                                       *
#        Author:  Sharanya Akoju                                              *
#  Return Codes:                                                              *
#                 0 - Success                                                 *
#                 1 - Error check log file                                    *
# ****************************************************************************
#  AutoSAP Automation                                                         *
#  --------------------                                                       *
#  Sr.         Role           Member           Email                          *
#  ---------   ----------     --------------   ------------------------------ *
#  1           Developer      Erry Lavakumar    erry.8.lavakumar@gsk.com      *  
#  2           Developer      Akoju Sharanya    akoju.x.sharanya@gsk.com      *  
# ****************************************************************************#

f=open("cred.txt","r")
asid = f.readline().strip()
aspass = f.readline().strip()

