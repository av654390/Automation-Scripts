# ****************************************************************************
#  Program Description : Script reads credentilas from cred.txt file         *
#  Program Name:  AutosapBW\cc.py                                            *
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

creds=open('cred.txt','r').readlines()
elkid=creds[0].strip()
elkpass=creds[1].strip()
javaid=creds[2].strip()
javapass=creds[3].strip()