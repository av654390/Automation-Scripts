# ****************************************************************************
#  Program Description : Script to read credentials                          *
#  Program Name:  115\cc.py                                                  *
#          Date:  08/05/2024                                                 *
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
#  2           Developer      erry lavakumar    erry.8.lavakumar@gsk.com     *  
#  2           Developer      akoju sharanya    akoju.x.sharanya@gsk.com     *  
#                                                                            *
# ****************************************************************************

f=open("cred.txt","r")
asid = f.readline().strip()
aspass = f.readline().strip()

