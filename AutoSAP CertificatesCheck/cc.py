# ****************************************************************************
#  Program Description : Script Reads Credentials from cred.txt              *
#  Program Name:  AutosapLOGS/cc.py                                          *
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

##Reading Credentials ##
f= open("cred.txt",'r')
elkid= f.readline().strip()
elkpass= f.readline().strip()