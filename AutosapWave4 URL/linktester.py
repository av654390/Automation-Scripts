# from urllib.request import urlopen
# import urllib
# export PYTHONWARNINGS="ignore:Unverified HTTPS request"
# import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning

# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# def urlchecker4(url):
#     try :
#         import http.client
#         conn = http.client.HTTPConnection(url)
#         conn.request("HEAD", "/")
#         r1 = conn.getresponse()
#         # print r1.status, r1.reason
#         return r1.status
#     except Exception as e:
#         return 400,e
# def urlchecker3(url):
#     try :
#         import requests
#         a= requests.head(url,verify=True,allow_redirects=True,cert=r"C:\Users\nc843765\OneDrive - GSK\NKISLIVE\thecode\AutoSAP JAVA\GlaxoSmithKline Certificate Authority.crt") 
#         return a.status_code
#     except Exception as e:
#         return 400,e
# def urlchecker2(url):
#     try :
#         from urllib.request import urlopen
#         return urlopen(url,capath=r"C:\Users\nc843765\OneDrive - GSK\NKISLIVE\thecode\AutoSAP JAVA\GlaxoSmithKline Certificate Authority.crt").getcode()
#     except Exception as e:
#         print(e,"hi hello")
#         return 400,e
# def urlchecker1(url):
#     try :
#         import requests
#         a= requests.get(url,verify = r'C:\Users\nc843765\OneDrive - GSK\NKISLIVE\thecode\AutoSAP JAVA\GlaxoSmithKline Certificate Authority.crt',allow_redirects=True) 
#         print(a,"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#         return a.status_code
#     except Exception as e:
#         return 400,e
def urlchecker(url):
    try:
        import urllib
        from urllib.request import urlopen
        user="Edge/107.0.1418.56"
        user="Edge/125.0.2535.79"
        user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        # user="Edge"
        header={'User-Agent':user}
        req=urllib.request.Request(url,headers=header)
        # print("hi")
        return urlopen(req).getcode()
    except urllib.error.HTTPError as e:
        if e.code ==401:
            print(f"Exception for {url}",e)
            return 200
        else:
            return 400,e
    except Exception as e:
        return 400,e
    
def linktester(url):
    a = urlchecker(url)
    if a == 200 :
        return True
    else :
        return False
# def linktester1(url):
#     a1 = urlchecker(url)
#     a2 = urlchecker1(url)
#     a3 = urlchecker2(url)
#     a4 = urlchecker3(url)
#     a5 = urlchecker4(url)
#     return a1,a2,a3,a4,a5
#     if a == 200 :
#         return True
#     else :
#         return False
if __name__ == "__main__":
    import os,pandas as pd
    original = os.getcwd() +'\og3 - Copy.xlsx'
    df= pd.read_excel(original,header=6,engine='openpyxl')
    # print(df)
    # exit()
    # sb=[]
    for i in df.index:
        a=df['URL'][i]
        c=df['SYSTEM'][i]
        b=linktester(a)
        if not b :
        #     sb.append(i+1)
            print(i,c,a,"check manually")
    # print(len(sb),sb)    
    # print(*linktester1("https://us6salxrpp101.corpnet2.com:59001/nwa"),sep="\n")