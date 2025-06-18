# ****************************************************************************
#  Program Description : Script to read credentials                          *
#  Program Name:  Procurement Post-Fun Checks\cc.py                 *
#          Date:  02/06/2025                                                 *
#       version:  1.0.0                                                      *
#        Author:  Akoju Sharanya                                             *
#  Return Codes:                                                             *
#                 1 - Success                                                *
#                 0 - Error check log file                                   *
# ****************************************************************************
#  AutoSAP Automation                                                        *
#  --------------------                                                      *
#  Sr.         Role           Member          Email                          *
#  ---------   ----------     --------------  -------------------------------*
#  1           Developer      Akoju Sharanya    akoju.x.sharanya@gsk.com     *  
#                                                                            *
# ****************************************************************************

f=open("cred.txt","r")
asid = f.readline().strip()
aspass = f.readline().strip()

