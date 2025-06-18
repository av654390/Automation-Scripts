# ****************************************************************************
#  Program Description : Script Performs Vx Monitoring                       *
#  Program Name:  AutosapBASIS\autosapVxMon.py                               *
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

# Importing Required Modules #
def autosapVxMon():
    import os
    import sys
    import time
    import pytz
    from datetime import datetime,timedelta

    start=time.time() ##Execution Start Time##
    tz=pytz.timezone('GMT')
    now=datetime.now(tz=tz)
    stamp=now.strftime("%Y-%m-%d-%H-%M-%S")
    sd=now.strftime("%Y-%m-%d")
    td=now.strftime("%d.%m.%Y")
    yes=now-timedelta(days=1)
    yest=yes.strftime("%d.%m.%Y")
    cd=os.getcwd()
    path = cd + f'/excel data/AutoSAP_{stamp}/'
    os.makedirs(os.path.dirname(path),exist_ok=True)
    sys.stdout = open(path+"LOG"+stamp+".txt", "w")
    print("Files will be stored in the path-",path)

    try:
        # Importing User Defined Modules of Performning Tcodes #
        import logon
        import db01, db02, se38, sm37, sm51, sm58, sm59, smlg, st06, st06_cpu, st07, st22
        import sender

        #Read System Details
        import json
        f=open('sys.txt','r')
        syst=f.read()
        sid=json.loads(syst)
        f.close()
        # sid={"SBT":"1.2 - R/3 Acceptance [Informal Testing]"} #SBT System
        # sid={"SBV":"1.1 - R/3 Validation [Formal Testing]"}   #SBV System

        for i in sid:
            session=logon.Autosap(sid[i])
            nos=1

            def islogonfine(session):
                if isinstance(session,list):
                    frm =  "noreply-autosapautomation@gsk.com"
                    to=["shiva.x.prasad@gsk.com","akash.2.verma@gsk.com"]
                    # cc=["erry.8.lavakumar@gsk.com","nikhil.x.chalikwar@gsk.com","akoju.x.sharanya@gsk.com"]
                    if session[0]==-2:
                        sender.error_mail(send_from=frm, send_to=to, lid=session[1], err=session[2], sid=i)
                        exit()
                    elif session[0]==-1:
                        time.sleep(3)
                        session=logon.Autosap(sid[i])

                    if isinstance(session,list):
                        sender.error_mail(send_from=frm, send_to=to, lid=session[1], err=session[2], sid=i)
                        exit()
                return "Logon is Fine"
            print(islogonfine(session))

            ### T-codes with Only Screenshots as Evidence ###
            db01_path=db01.db01(nos=nos,session=session,path=path,stamp=stamp)
            print("DB01-",db01_path)
            nos+=1
            sm51_path=sm51.sm51(nos=nos,session=session,path=path,stamp=stamp)
            print("SM51-",sm51_path)
            nos+=1
            sm58_path=sm58.sm58(nos=nos,session=session,path=path,stamp=stamp,td=td)
            print("SM58-",sm58_path)
            nos+=1
            smlg_path=smlg.smlg(nos=nos,session=session,path=path,stamp=stamp)
            print("SMLG-",smlg_path)
            nos+=1
            sm37_dict=sm37.sm37(nos=nos,session=session,path=path,stamp=stamp,dt=yest)
            sm37_path=sm37_dict['path']
            print("SM37-",sm37_path)
            nos+=1

            ### T-codes That Requires Analysis and Report ###
            db02_dict=db02.db02(nos=nos,session=session,path=path,stamp=stamp)
            print("DB02 -",db02_dict)
            nos+=1
            st06_cpu_dict = st06_cpu.st06(nos=nos,session=session,path=path,stamp=stamp,sid=i)
            print("ST06 CPU-",st06_cpu_dict)
            nos+=1
            st06_dict1=st06.st06(nos=nos,session=session,path=path,stamp=stamp,sid=i)
            st06_dict=st06_dict1[0]
            print("ST06-",st06_dict)
            nos+=1
            st07_dict=st07.st07(nos=nos,session=session,path=path,stamp=stamp)
            print("ST07-",st07_dict)
            nos+=1
            st22_dict=st22.st22(nos=nos,session=session,path=path,stamp=stamp)
            print("ST22-",st22_dict)
            nos+=1
            se38_dict=se38.se38(nos=nos,session=session,path=path,stamp=stamp,sid=i)
            nos+=1
            sm59_dict=sm59.sm59(nos=nos,session=session,path=path,stamp=stamp,sid=i)
            nos+=1
            logon.logof(session)

            sealcount=0
            for s in sm59_dict.values():
                if s.lower()=='ok':
                    pass
                else:
                    sealcount+=1
            
            sealstatus='Red' if sealcount>0 else 'Green'
            
            combined_dict=st06_dict1[1]
            # Format of final_values is {'st06_dict':{'rcpu':{'value':1.52,'status':'Amber'},'disk':{'value':30,'status':'Green'}},'st07_dict':{'act':{'value':172,'status':'Green'},'wp':{'value':272,'status':'Red'}},"sm37_dict":{'value':0,'status':'Green'},'st22_dict':{'dumps':210,'status':'Amber'},'db02_dict':{'PSAPR3I': {'value':71,'status':'Green'}, 'PSAPUNDO': {'value':24,'status':'Green'}, 'PSAPR3I750': {'value':85,'status':'Amber'}, 'PSAPR3IINDEX': {'value':95,'status':'Red'}, 'PSAPSOFFCONT1': {'value':89,'status':'Amber'}}}
            final_values={'db02_dict':db02_dict,'st06_cpu_dict':st06_cpu_dict,'st06_dict':st06_dict,'st07_dict':st07_dict,'st22_dict':st22_dict,"sm37_dict":sm37_dict,'se38_dict':se38_dict,'sm59_dict':{'value':sealcount,'status':sealstatus}}
            print("FINAL VALUES:",final_values)

            end=time.time() ## Execution End Time ##
            run_time=round(end-start,2) ## Time Taken For Execution ##

            try:
                ## Generating Excel Report ##
                import xlreport
                ht=xlreport.genxl(final_values=final_values,run_time=run_time,path=path,stamp=stamp)
                print(ht)

                xlreport.rfcxl(sm59_dict=sm59_dict,combined_dict=combined_dict,path=path,stamp=stamp,sid=i)
                all_status=[]
                for keys in final_values:
                    try:
                        all_status.append(final_values[keys]['status'])
                    except:
                        for key2 in final_values[keys]:
                            all_status.append(final_values[keys][key2]['status'])
                print("ALL STATUS:", all_status)

                if 'Red' in all_status:
                    overall_status='Red'
                elif 'Amber' in all_status:
                    overall_status='Amber'
                elif all(ele == 'Green' for ele in all_status):
                    overall_status='Green'
                else:
                    overall_status='Check Manually'

                print("OVERALL STATUS:",overall_status)

                ## Mail Part ##
                frm =  "noreply-autosapautomation@gsk.com"
                to= ["krishnamurthy.x.k@gsk.com","SABINE.RAVET@GSK.COM","globalerpsm@gsk.com"]
                cc = ["sivakaminathan.x.palaniappan@gsk.com","jay.x.menon@gsk.com","amit.k.prabhakar@gsk.com","sunil.k.s@gsk.com","ramakrishnareddy.x.banda@gsk.com","ITTCSESAT@gsk.com","ga&dSAPBASISopsind@gsk.com","anil.x.reddy@gsk.com","preetham.x.aranha@gsk.com","hareesh.x.s@gsk.com","shiva.x.prasad@gsk.com","akash.2.verma@gsk.com"]
                bcc=["erry.8.lavakumar@gsk.com","akoju.x.sharanya@gsk.com"]
                subject=f"[{overall_status}] AutoSAP {i} Hourly Monitoring {stamp} GMT"
                bdy="test mail"
                file_path=path
                html=ht
                sender.send_mail(send_from=frm, send_to=to, send_cc=cc, send_bcc=bcc, subject=subject, text=bdy, files=file_path,html=html)

            except Exception as e:
                print({'Error while Generating Report/Sending Mail':e})

    except Exception as e:
        print({'Error in Global Try ':e})
    finally:
        sys.stdout.close()  


if __name__=="__main__":
    autosapVxMon()

