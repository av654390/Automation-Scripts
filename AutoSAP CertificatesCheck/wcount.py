import re
import time
import datetime
from dateutil.relativedelta import *

def wcount(file):
    try:     
        f=open(file,'r').readlines()
        li=[]
        for i in f:
            if '=' in i and len(re.findall('[0-9]{2}.[0-9]{2}.[0-9]{4}',i))!=0:
                li.append(i[4:])
        # print(li)
        li2=list(set(li))
        # print(len(f))
        # print(len(li))
        # print(len(li2))
        # print(*li2,sep="\n")
        #print(set(f)-set(li))
        print("List 2:",li2)
        dates=[re.findall('[0-9]{2}.[0-9]{2}.[0-9]{4}',i)[-1] for i in li2]
        # dates=re.findall('[0-9]{2}.[0-9]{2}.[0-9]{4}',f) #string checking dates
        # print(f"Dates: {dates}")
        # extra=len(re.findall('Overview of Installed Certificates',f))
        weeks=[]
        now=datetime.datetime.now()
        overdue=week0=week1=week2=week3=week4=week5=week6=0
        format=lambda x:time.strptime(x,'%d.%m.%Y')
        for i in range(8):
            x=now+relativedelta(weeks=+i) # adding weeks
            wd=x.strftime('%d.%m.%Y')
            wday=format(wd)
            weeks.append(wday) 
        od=[]
        nex=[]
        nxt2=now+ relativedelta(years=+4)
        recent=nxt2.strftime('%d.%m.%Y') #for finding recent expiry date
        
        #print(weeks)
        for i in dates:
            if i.find('.')!=-1:
                date=format(i)
                # print("Date:",date)
                recentf=format(recent)
                if date<weeks[0] : # overdue
                    overdue=overdue +1
                    od.append(i)
                    recent=i
                    #print("overdue",i,overdue)
                elif weeks[0]<=date and date<weeks[1]:
                    week0=week0+1
                    recent=i
                    #print("week0",i,week0)
                elif weeks[1]<=date and date<weeks[2]:
                    week1=week1+1
                    recent=i
                    #print("week1",i)
                elif weeks[2]<=date and date<weeks[3]:
                    week2=week2+1
                    recent=i
                    #print("week2",i)
                elif weeks[3]<=date and date<weeks[4]:
                    week3=week3+1
                    recent=i
                    #print("week3",i)
                elif weeks[4]<=date and date<weeks[5]:
                    week4=week4+1
                    recent=i
                    #print("week4",i)
                elif weeks[5]<=date and date<weeks[6]:
                    week5=week5+1
                    recent=i
                    #print("week5",week5,i)
                elif weeks[6]<=date and date<weeks[7]:
                    week6=week6+1
                    recent=i
                    #print("week6",i)
                else:
                    if recentf>date:
                        recent=i

        # print("Recent:",recent)
        for c in li2:
            if recent in c:
                certname=c
                break
        else:
            certname='NA'
        # print(certname)
        return {"overdue":overdue,"week0":week0,"week1":week1,"week2":week2,"week3":week3,"week4":week4,"week5":week5,"week6":week6, "recent":recent, "certname":certname}
        # for i in dates:
        #     d=datetime.strptime(nw1,'%d.%m.%Y')
        #     i=datetime.strptime(i,'%d.%m.%Y')
        #     
    except Exception as e:
        print(e)


if __name__ == "__main__":
    pass