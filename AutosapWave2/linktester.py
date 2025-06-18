def urlchecker(url):
    try:
        import urllib
        from urllib.request import urlopen
        # user="Edge/107.0.1418.56"
        # user="Edge/125.0.2535.79"
        user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Edge/107.0.1418.56 Edge/125.0.2535.79 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        header={'User-Agent':user}
        req=urllib.request.Request(url,headers=header)
        print(urlopen(req).getcode())
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
        #print("True")
        return True
    else :
        return False


if __name__ == "__main__":
    b=linktester(r"http://us6sdlxvep101.corpnet2.com:8095/oseries-auth/login")
    print(b,sep="+++++++++++++++++++++++++++++++")
    if not b :
        #   sb.append(i+1)
        print(b,"check manually")
    exit()
