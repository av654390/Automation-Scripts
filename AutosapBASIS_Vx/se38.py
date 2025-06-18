# ****************************************************************************
#  Program Description : Script Performs SE38 T-Code Action in SAP           *
#  Program Name:  AutosapBASIS\se38.py                                       *
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

def se38(nos=0,session=0,path=0,stamp=0,sid=0):
    try:
        print("\n##### SE38 #####")
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nse38"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/radRS38M-FUNC_SSET").select()
        session.findById("wnd[0]/usr/ctxtRS38M-PROGRAMM").text = "/SDF/MON"
        session.findById("wnd[0]/usr/ctxtRS38M-PROGRAMM").caretPosition = 8
        session.findById("wnd[0]/usr/btnSHOP").press()
        session.findById("wnd[0]/usr/ctxtRSVAR-VARIANT").text = "TEST_Auto"
        session.findById("wnd[0]/usr/ctxtRSVAR-VARIANT").caretPosition = 4
        session.findById("wnd[0]/usr/btnCREA").press()
        session.findById("wnd[1]/usr/radFLAG1").setFocus()
        session.findById("wnd[1]/usr/radFLAG1").select()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/tbar[1]/btn[25]").press()
        session.findById("wnd[0]/usr/ctxtST_DAT").text = ""
        session.findById("wnd[0]/usr/ctxtST_TIM").text = ""
        session.findById("wnd[0]/usr/ctxtENDDAT").text = ""
        session.findById("wnd[0]/usr/ctxtENDTIM").text = ""
        session.findById("wnd[0]/usr/ctxtENDTIM").setFocus()
        session.findById("wnd[0]/usr/ctxtENDTIM").caretPosition = 8
        session.findById("wnd[0]/tbar[1]/btn[25]").press()
        session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").setCurrentCell(-1,"ST_DAT")
        session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectColumn("ST_DAT")
        session.findById("wnd[0]/tbar[1]/btn[40]").press()
        import re
        pattern="Daily Monitoring \d{2}.\d{2}.\d{4}"
        for i in range(10):
            x=session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").GetCellValue(i,"DESCRIPTION")
            if bool(re.match(pattern,x)):
                session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").currentCellRow = i
                session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectedRows = str(i)
                session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").doubleClickCurrentCell()
                break
        
        
        # Filtering only latest minute's data #
        count=0
        while True:
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").currentCellRow = -1
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectColumn("TIME")
            session.findById("wnd[0]/tbar[1]/btn[29]").press()
            session.findById("wnd[1]").sendVKey(4)
            session.findById("wnd[2]/usr/lbl[1,3]").caretPosition = 3
            session.findById("wnd[2]").sendVKey(2)
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            name=path+f'{nos} SE38 {stamp}.png'
            session.findById("wnd[0]").HardCopy(name, 1)

            #Exporting Data
            session.findById("wnd[0]/tbar[1]/btn[45]").press()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
            name2=f"{nos} SE38 {stamp}.html"
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name2
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
            session.findById("wnd[1]/tbar[0]/btn[11]").press()

            import pandas as pd
            nf=pd.read_html(path+name2,header=0,thousands='.',decimal=',')[0]
            if sid.lower()=='sbt':
                count+=1
                try:
                    cpu_idle=nf.loc[nf['AS\xa0Instance']=='rixsasp1_SBP_00','CPU\xa0Idle'].values[0]
                    break
                except:
                    session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").currentCellRow = -1
                    session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectColumn("TIME")
                    session.findById("wnd[0]/tbar[1]/btn[29]").press()
                    session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = ""
                    session.findById("wnd[1]/tbar[0]/btn[0]").press()
                    session.findById("wnd[0]/tbar[1]/btn[8]").press() #Refresh
                finally:
                    if count==2:
                        print("SE38: Refresh Count exceeds 2")
                        break
            elif sid.lower()=='sbv':
                count+=1
                try:
                    cpu_idle=nf.loc[nf['AS\xa0Instance']=='rixsap2v_SBV_09','CPU\xa0Idle'].values[0]
                    break
                except:
                    session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").currentCellRow = -1
                    session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectColumn("TIME")
                    session.findById("wnd[0]/tbar[1]/btn[29]").press()
                    session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = ""
                    session.findById("wnd[1]/tbar[0]/btn[0]").press()
                    session.findById("wnd[0]/tbar[1]/btn[8]").press() #Refresh
                finally:
                    if count==2:
                        print("SE38: Refresh Count exceeds 2")
                        break
            elif sid.lower()=='sbp':
                count+=1
                try:
                    cpu_idle=nf.loc[nf['AS\xa0Instance']=='rixsasp1_SBP_00','CPU\xa0Idle'].values[0]
                    break
                except:
                    session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").currentCellRow = -1
                    session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectColumn("TIME")
                    session.findById("wnd[0]/tbar[1]/btn[29]").press()
                    session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = ""
                    session.findById("wnd[1]/tbar[0]/btn[0]").press()
                    session.findById("wnd[0]/tbar[1]/btn[8]").press() #Refresh
                finally:
                    if count==2:
                        print("SE38: Refresh Count exceeds 2")
                        break
            
        
        import pandas as pd
        nf=pd.read_html(path+name2,header=0,thousands='.',decimal=',')[0]
        ## Column Names in nf -- ['Time', 'AS\xa0Instance', 'Act.\xa0WPs', 'Dia.WPs', 'RFC\xa0Normal', 'CPU\xa0Usr', 'CPU\xa0Sys', 'CPU\xa0Idle', 'Paging\xa0in', 'Paging\xa0out', 'Free\xa0Mem.', 'EM\xa0alloc.', 'EM\xa0attach.', 'Em\xa0global', 'Heap\xa0Memor', 'Pri.', 'Paging\xa0Mem', 'Dia.', 'Upd.', 'Enq.', 'Logins', 'Sessions'] ##

        latest_time=nf[nf['Time']==nf.loc[0,'Time']]

        ##Logins Data##
        try:
            logins=latest_time['Logins'].sum()
            print("Logins : ",logins)
            if logins<6000:
                logins_status='Green'
            elif logins>=6000 and logins<7000:
                logins_status='Amber'
            elif logins>=7000:
                logins_status='Red'
        except:
            return {'logins':{'value':'Nan','status':"Check Manually"},'sessions':{'value':"Nan",'status':"Check Manually"},'wps':{'value':'Nan','status':"Check Manually"},'cpu%':{'value':'Nan','status':"Check Manually"}}

        ##Sessions Data##
        try:
            sessions=latest_time['Sessions'].sum()
            print("Session : ",sessions)
            if sessions<9500:
                sessions_status='Green'
            elif sessions>=9500 and sessions<10000:
                sessions_status='Amber'
            elif sessions>=10000:
                sessions_status='Red'
        except:
            return {'logins':{'value':logins,'status':logins_status},'sessions':{'value':"Nan",'status':"Check Manually"},'wps':{'value':'Nan','status':"Check Manually"},'cpu%':{'value':'Nan','status':"Check Manually"}}

        ##WPs Priv Mode Data##
        try:
            wps=latest_time['Pri.'].sum()
            print("WPs Priv Mode: ",wps)
            if wps<150:
                wps_status='Green'
            elif wps>=150 and wps<200:
                wps_status='Amber'
            elif wps>200:
                wps_status='Red'
        except:
            return {'logins':{'value':logins,'status':logins_status},'sessions':{'value':sessions,'status':sessions_status},'wps':{'value':'Nan','status':"Check Manually"},'cpu%':{'value':'Nan','status':"Check Manually"}}
    
        try:
            ##CPU Utilization% Data##
            cpu=100-cpu_idle
            print("CPU Idle %:",cpu_idle)
            print("CPU Utilization %:",cpu)
            if cpu<80:
                cpu_status='Green'
            elif cpu>=80 and cpu<=90:
                cpu_status='Amber'
            elif cpu>90:
                cpu_status='Red'
        except:
            return {'logins':{'value':logins,'status':logins_status},'sessions':{'value':sessions,'status':sessions_status},'wps':{'value':wps,'status':wps_status},'cpu%':{'value':'Nan','status':"Check Manually"}}
        
        return {'logins':{'value':logins,'status':logins_status},'sessions':{'value':sessions,'status':sessions_status},'wps':{'value':wps,'status':wps_status},'cpu%':{'value':cpu,'status':cpu_status}}
    
    except Exception as e:
        print({'Error in SE38':e})
        return {'logins':{'value':'Nan','status':"Check Manually"},'sessions':{'value':"Nan",'status':"Check Manually"},'wps':{'value':'Nan','status':"Check Manually"},'cpu%':{'value':'Nan','status':"Check Manually"}}
    

if __name__ =="__main__":
    # sid={'sbt':"1.2 - R/3 Acceptance [Informal Testing]"}
    # sid={'sbv':"1.1 - R/3 Validation [Formal Testing]"}
    sid={'sbp':"0.1 - R/3 Production"}
    import os
    import logon
    from datetime import datetime
    session=logon.Autosap(sid['sbp'])
    nos=0
    now=datetime.now()
    stamp=now.strftime("%Y-%m-%d-%H-%M-%S")
    cd=os.getcwd()
    path = cd + f'/excel data/'
    # sm59_dict=sm59(nos=0,session=session,path=path,stamp=stamp)
    se38_dict=se38(nos=0,session=session,path=path,stamp=stamp,sid='sbp')
    print(se38_dict)
    # print(sm59_dict[100])
    



