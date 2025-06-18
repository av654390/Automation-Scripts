
import pandas as pd
import os

def cif(session,path,stamp,fd,td,job,users):
    # return {"status":"other","value":"test"}
    import pandas as pd
    import logon
    import time
    import datetime
    import os
    
    # os.mkdir(path)
    name1 = f'/CIFJobReport_{fd}.html'
    #name2 = f'spoollist_{str(time.time())}.html'
    #path2 = os.getcwd() + '/spoollist_reports/'
    

    # Calculate yesterday's date 
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsm37"
        session.findById("wnd[0]").sendVKey(0)
        # session.findById("wnd[0]/usr/txtBTCH2170-JOBNAME").text = "CTE_COST_CENTER_EXPORT"
        # session.findById("wnd[0]/usr/txtBTCH2170-USERNAME").text = "RG636259"

        # session.findById("wnd[0]/usr/txtBTCH2170-JOBNAME").text = "ARFC:0A6D032005A66633ABC7017F"
        # session.findById("wnd[0]/usr/txtBTCH2170-USERNAME").text = "ALEREMOTE"
        
        # session.findById("wnd[0]/usr/txtBTCH2170-JOBNAME").text = "z_*_APO_D_CIF_DELTA"
        # session.findById("wnd[0]/usr/txtBTCH2170-USERNAME").text = "*"
        
        # session.findById("wnd[0]/usr/txtBTCH2170-JOBNAME").text = "*"
        # session.findById("wnd[0]/usr/txtBTCH2170-USERNAME").text = "*"
        
        session.findById("wnd[0]/usr/txtBTCH2170-JOBNAME").text = job
        session.findById("wnd[0]/usr/txtBTCH2170-USERNAME").text = users

        session.findById("wnd[0]/usr/txtBTCH2170-USERNAME").setFocus()
        session.findById("wnd[0]").sendVKey(0)
        # session.findById("wnd[0]/usr/chkBTCH2170-RUNNING").selected = True
        # session.findById("wnd[0]/usr/chkBTCH2170-READY").selected = True
        # session.findById("wnd[0]/usr/chkBTCH2170-SCHEDUL").selected = True
        session.findById("wnd[0]/usr/chkBTCH2170-PRELIM").selected = True
        session.findById("wnd[0]/usr/chkBTCH2170-SCHEDUL").selected = True
        session.findById("wnd[0]/usr/chkBTCH2170-READY").selected = True
        session.findById("wnd[0]/usr/chkBTCH2170-RUNNING").selected = True
        session.findById("wnd[0]/usr/chkBTCH2170-FINISHED").selected = True
        session.findById("wnd[0]/usr/chkBTCH2170-ABORTED").selected = True
        session.findById("wnd[0]/usr/ctxtBTCH2170-FROM_DATE").text = fd#"11.07.2023"
        session.findById("wnd[0]/usr/ctxtBTCH2170-TO_DATE").text = td#"11.07.2023"
        session.findById("wnd[0]/usr/ctxtBTCH2170-FROM_TIME").text = "00:00:00"
        session.findById("wnd[0]/usr/ctxtBTCH2170-TO_TIME").text = "00:00:00"
        session.findById("wnd[0]/usr/ctxtBTCH2170-TO_DATE").setFocus()
        session.findById("wnd[0]/usr/ctxtBTCH2170-TO_DATE").caretPosition = 10
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        # status='Green'
        bar=session.findById("wnd[0]/sbar").text
        print(bar)
        if "No job matches the selection criteria" in bar :
            return {"status":"nojob","value":"nojob"}
        try:
            # session.findById("wnd[0]").HardCopy(f"{path}/finishedss.png", 1)
            # Select options for canceled jobs in SAP
            # session.findById("wnd[0]/usr/lbl[72,10]").setFocus()
            # # session.findById("wnd[0]/usr/lbl[72,10]").caretPosition = 7
            # session.findById("wnd[0]").sendVKey(2)


            session.findById("wnd[0]/mbar/menu[5]/menu[5]/menu[2]/menu[1]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            # Specify path and filename for the first HTML file
            session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1
            session.findById("wnd[1]/usr/ctxtDY_PATH").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[11]").press()

            g = pd.read_html(path + name1, header=0)[0]
            # cj= g[g['Status'] == 'Canceled']['JobName'].tolist()
            # fj=g[g['Status'] == 'Finished']['JobName'].tolist()
            # print("CJJ",cj)
            # print("FJJ",fj)
            # op=[]
            # fj.remove('ALL_CF_CIF_REGENERATE')
            # fj.remove('ALL_CF_CIF_REGENERATE_NA')

            # for i in range(len(g.index)-1): ###Latest one (next line)
            #     d[g['JobName'][i]]=g['Status'][i]
            # d['ALL_CF_CIF_REGENERATE_NA']='Canceled'
            g=g[g['JobName']!='*Summary']
            g['Datetime']=pd.to_datetime(g['Sched.\xa0start\xa0date']+' '+g['Sched.\xa0start\xa0time'])

            #Sort the dataframe by 'Datetime' and 'Status' in descending order
            g.sort_values(by=['Datetime','Status'],ascending=[True,True], inplace=True)

            print("1hi hello +++++++++++++++++")
            #Drop the 'Date', 'Time', and 'Datetime' Columns
            g.drop(['Sched.\xa0start\xa0date','Sched.\xa0start\xa0time','Datetime'],axis=1,inplace=True)

            #Drop duplicate rows based on 'Job Name' and keep the first occurence (Latest status)
            latest_status=g.drop_duplicates(subset='JobName', keep='first')

            #Convert the result to a dictionary in key-value format

            d=latest_status.set_index('JobName')['Status'].to_dict()
            dval=d.values()
            print("2hi hello +++++++++++++++++",list(i=='Finished' for i in dval))
            if any(i=='Canceled' for i in dval):
                # print(fins(session,path,name1))
                print(dval)
                status="[RED] AutoSAP CIF job monitoring"

                return {"status":"Canceled","value":list(dval)}
            if any(i=='Active' for i in dval):
                # print(fins(session,path,name1))
                print(dval)
                return {"status":"Active","value":list(dval)}
            if all(i=='Finished' for i in dval):
                # print(fins(session,path,name1))
                print(dval)
                return {"status":"Finished","value":list(dval)}
            if all(i=='Schedule' or i=='Released' for i in dval):
                # print(fins(session,path,name1))
                print(dval)
                return {"status":"ScheduleorReleased","value":list(dval)}

            return {"status":"other","value":list(dval)}
            
            print("3hi hello +++++++++++++++++")



        except Exception as e:
            print("1An error occurred:", str(e))
    except Exception as e:
        print("2An error occurred:", str(e))

if __name__ == "__main__":
    # cif(session,path,stamp,fd,td):
    import os
    import logon
    import datetime
    session=logon.Autosap()
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # tempdir= f"autosap {stamp}"
    nos=9
    path=os.getcwd()+f"\excel_data\\autosap {stamp}\\"
    fd="27.05.2024"
    td="27.05.2024"
    # fd=""
    # td=""
    job = "z_*_APO_D_CIF_DELTA"
    job = "ZQMRP_JOB_BAT_QA_CTRL_E"
    users="*"
    temp=cif(session,path,stamp,fd,td,job=job,users=users)
    print(temp)


    # {'SAP_SRT_REORG_LOG_TRACE': 'Canceled', 'Z_256_MM_E_GDSMVT_AUTOCREATE_1': 'Canceled', 'ZFI_256_ZFI_BSIK_UPDATE': 'Canceled', 'ZFI_F110S\xa0:\xa0ADVICES': 'Canceled', 'ZQMRP_JOB_BAT_QA_CTRL_E': 'Canceled', 'ZWM_PHYSICAL_INVENTORY': 'Canceled'}