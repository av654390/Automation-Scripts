# ****************************************************************************
#  Program Description : CyberArk fetch code                                 *
#  Program Name:  CIF\autosapcif.py                                          *
#          Date:  07/08/2024                                                 *
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
import requests
 
# Help tries direct / mud/ windows identity
 
from requests_kerberos import HTTPKerberosAuth  #windows identity
 
# import getpass only id mud id password
 
import json
 
def fetch_password():
 
    # Set the URL of the CyberArk Credential Provider
    
    url = "https://us1sawn04670.wmservice.corpnet1.com/AIMWebService-AUTH/api/Accounts?AppID=App_Python_Auto_Test&Safe=Python_Auto_Test"
    
    
    # Set up the Kerberos authentication (windows only)
    
    auth = HTTPKerberosAuth()
    # print(auth)
    
    try:
    
        response = requests.get(url, auth=auth,verify=False)
        
        # response = requests.get("https://AIMWebService-AUTH/api/Accounts?AppID={Appid}&Safe={SAFEID}&0bject={OBJECT}", au 
        # print(dir(response))
        response.raise_for_status()
        if response.status_code == 200 :
            print("connection esatblished with CyberArk !!!!!!!!!!!")
            password = response.text
            
            data =json.loads(response.text)
            data=dict(data)
            Client_id = data["Content"]
            # print(password,Client_id)
            for i,j in data.items():
                print(i,":",j)
            # print(,sep="\n")
        else :
            print("connection esatblished with CyberArk")
    except requests.exceptions. RequestException as e:
        print(f"Error: {e}")
 
# print("start",__name__)
if __name__ == "__main__":
    print("started")
    print(fetch_password())