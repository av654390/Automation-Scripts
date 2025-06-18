# ****************************************************************************
#  Program Description : Script Performs ST06 T-Code Action in SAP           *
#  Program Name:  AutosapBASIS\st06.py                                       *
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

def st06(nos=0,session=0,path=0,stamp=0,sid=0):
    try:
        print("\n##### ST06 #####")
        session.findById("wnd[0]").maximize()

        #RAGENT - IMPERVA
        def rcpu():
            session.findById("wnd[0]").maximize()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nsm51"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").currentCellColumn = "HOSTNAMELONG"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").clickCurrentCell()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nst06"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/mbar/menu[3]/menu[2]").select()
            session.findById("wnd[0]/tbar[1]/btn[13]").press()
            session.findById("wnd[0]/usr/btnPUSH6").press()
            session.findById("wnd[0]/tbar[1]/btn[45]").press()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            namer=f"{nos} ST06 Rcpu {stamp}.html"
            session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = namer
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
            session.findById("wnd[1]/tbar[0]/btn[11]").press()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nex"
            session.findById("wnd[0]").sendVKey(0)
            st=pd.read_html(path+namer,header=0,decimal=',',thousands='.')[0]
            #['Process\xa0ID', 'User', 'Process\xa0Name', 'Utilizatn', 'CPU\xa0Time', 'ResidentSz', 'Priority']
            val=st.loc[st['Process\xa0Name'].str.contains('ragent'),'Utilizatn'].values[0]
            rcpu=round(val/100,2)
            print("R CPU% : ",rcpu)
            return rcpu

        session.findById("wnd[0]/tbar[0]/okcd").text = "/nst06"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[0]/shellcont/shell/shellcont[0]/shell").selectedNode = "          3"
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[0]/shellcont/shell/shellcont[0]/shell").topNode = "          1"
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").pressToolbarButton("&MB_FILTER")
        session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/btnAPP_WL_SING").press()
        session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/cntlCONTAINER1_FILT/shellcont/shell").currentCellRow = 1
        session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/cntlCONTAINER1_FILT/shellcont/shell").selectedRows = "1"
        session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/btnAPP_WL_SING").press()
        session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/cntlCONTAINER1_FILT/shellcont/shell").selectedRows = "1"
        session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/btnAPP_WL_SING").press()
        session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/btn600_BUTTON").press()
        session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").text = "CPU"
        session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN003-LOW").text = "Idle"
        session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN003-LOW").setFocus()
        session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN003-LOW").caretPosition = 4
        session.findById("wnd[2]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").pressToolbarContextButton("&MB_EXPORT")
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").selectContextMenuItem("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path 
        name1=f'{nos} ST06 CPU {stamp}.html'
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 12
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").pressToolbarButton("&MB_FILTER")
        session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/btn600_BUTTON").press()
        session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = "Memory"
        session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").text = "Free memory"
        session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").setFocus()
        session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").caretPosition = 11
        session.findById("wnd[2]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").pressToolbarContextButton("&MB_EXPORT")
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").selectContextMenuItem("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path 
        name2=f'{nos} ST06 Memory {stamp}.html'
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name2
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 11
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        # Analysing CPU % and Free Memory
        import pandas as pd
        df1=pd.read_html(path+name1,header=0)[0] #For CPU Idle#
        # Column Names: ['App.Server', 'Category', 'Descript.', 'Value', 'Unit']
        dict1=df1.set_index('App.Server')['Value'].apply(lambda x:100-x).to_dict() #For CPU Utilization#
        print("For CPU Utilization : ",dict1)
        df2=pd.read_html(path+name2,header=0)[0] #For Free Memory
        dict2=df2.set_index('App.Server')['Value'].to_dict()
        print("For Free Memory :",dict2)

        combined_dict={k:[dict1[k],dict2[k]] for k in dict1}

        ### Checking for "/oracle/SBT/oraarch" Disk CPU ###
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[0]/shellcont/shell/shellcont[0]/shell").selectedNode = "          3"
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[0]/shellcont/shell/shellcont[0]/shell").topNode = "          1"
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[0]/shellcont/shell/shellcont[1]/shell").selectedNode = "          7"
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").setCurrentCell(-1,"FSYSNAME")
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").selectColumn("FSYSNAME")
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").contextMenu()
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").selectContextMenuItem("&FILTER")
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = f"/oracle/{sid}/oraarch"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").caretPosition = 19
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").currentCellColumn = "FREE_PERCENT"
        session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").selectedRows = "0"
        disk_cpu_free=session.findById("wnd[0]/shellcont/shellcont/shell/shellcont[1]/shell").GetCellValue(0,"FREE_PERCENT")
        name=path+f'{nos} ST06 Disk CPU {stamp}.png'
        session.findById("wnd[0]").HardCopy(name, 1)
        print("ST06 Disk CPU : File/Screenshot Saved Successfully!!")
        print(name)
        disk_cpu=100-int(disk_cpu_free)
        print("Disk CPU Utilized",disk_cpu)
        status1='Green' if int(disk_cpu)<40 else 'Red'

        ### Analysing RAgent and Disk CPU ###
        try:
            ragent=rcpu()
            if ragent<1.5:
                status='Green'
            elif ragent>=1.5 and ragent<2:
                status='Amber'
            elif ragent>=2:
                status='Red'
        except:
            return [{'rcpu':{'value':'Nan','status':"Check Manually"},'disk':{'value':disk_cpu,'status':status1}},combined_dict]
        
        return [{'rcpu':{'value':ragent,'status':status},'disk':{'value':disk_cpu,'status':status1}},combined_dict]
    except Exception as e:
        print({'Error in ST06':e})
        return [{'rcpu':{'value':'Nan','status':"Check Manually"},'disk':{'value':'Nan','status':"Check Manually"}},"Check Manually"]

if __name__ =="__main__":
    sid={"SBP":"0.1 - R/3 Production"}
    import os
    import logon
    from datetime import datetime
    session=logon.Autosap(sid['SBP'])
    nos=0
    now=datetime.now()
    stamp=now.strftime("%Y-%m-%d-%H-%M-%S")
    cd=os.getcwd()
    path = cd + f'/excel data/AutoSAP_{stamp}/'
    print(st06(nos=0,session=session,path=path,stamp=stamp,sid='SBP'))