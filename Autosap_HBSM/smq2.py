# ****************************************************************************
#  Program Description : Script Performs SMQ2 T-Code Actions in SAP          *
#  Program Name:  AutosapHBSM/smq2.py                                        *
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

def smq2(nos=0,session=0,path=0,stamp=0,system=0):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nsmq2"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/txtCLIENT").text = "100"
        session.findById("wnd[0]/usr/txtQNAME").text = "*"
        session.findById("wnd[0]/usr/txtQERROR").text = "X"
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/mbar/menu[4]/menu[5]/menu[2]/menu[1]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        name1=f'[{system}] {nos} All Queues {stamp}.html'
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 10
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        ##Filter Important Queues
        import pandas as pd 
        df=pd.read_html(path+name1,header=0)[1]
        print('\n',df)
        if df.empty:
            return {"value":0,'status':'Green','backlogs':{}}
        #Column Names-['Unnamed: 0', 'Cl.', 'Queue\xa0Name', 'Entries']
        queues=df['Queue\xa0Name'].to_dict()
        print("AVAILABLE QUEUES:",queues,'\n')

        imp=['CSRIXSBPI','CSAMPLE-BIDR','DL','ZRO','WMTH','WMD','EWMMEWMGOODSMVT','ZECC_FINDINGS','ZMNF','POFS']
        vimp=['EWMMEWMGOODSMVT','DL']

        if system.lower() =='sbp' or system.lower() =='sbt':
            fil_q={}
            for q in queues:
                for i in imp:
                    if queues[q].startswith(i) and df.loc[q,'Status']!='RUNNING':
                        print("QUEUE",q,queues[q])
                        fil_q[q]=queues[q]
        else:
            fil_q={}
            for q in queues:
               if df.loc[q,'Status']!='RUNNING':
                    print("QUEUE",q,queues[q])
                    fil_q[q]=queues[q]
        print("FILTERED QUEUES:",fil_q,'\n')
        backlogs={}

        import newsqlite
        for k in fil_q:
            bck=newsqlite.read_from_db(filename="my.db",name=fil_q[k])
            print("BACK----",bck)
            if bck:
                backlogs[k]=fil_q[k]
            newsqlite.insert_into_db(filename="my.db", name=fil_q[k], date=stamp[:10], time=stamp[11:])
        val=len(fil_q)-len(backlogs)  
        status='Green' if len(fil_q)<=0 else 'Red'
        print({"Len":val,"status":status})

        nos=0  
        for key in fil_q:
            if key<25:
                print("KEY:",key)
                session.findById(f"wnd[0]/usr/lbl[7,{8+key}]").setFocus()
                session.findById(f"wnd[0]/usr/lbl[7,{8+key}]").caretPosition = 11
                session.findById("wnd[0]").sendVKey(2)
            else:
                scrl=key
                nkey=0
                print("New Key:",nkey)
                print("NQ:",fil_q[key])
                session.findById("wnd[0]/usr").verticalScrollbar.position = scrl
                session.findById(f"wnd[0]/usr/lbl[7,{8+nkey}]").setFocus()
                session.findById(f"wnd[0]/usr/lbl[7,{8+nkey}]").caretPosition = 11
                session.findById("wnd[0]").sendVKey(2)
            session.findById("wnd[0]/mbar/menu[4]/menu[5]/menu[2]/menu[1]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[1]/usr/ctxtDY_PATH").text =path 
            name2=f'[{system}] {nos} {fil_q[key]} queue {stamp}.html'
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name2 #"smq2b.html"
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 10
            session.findById("wnd[1]/tbar[0]/btn[11]").press()
            session.findById("wnd[0]/usr/lbl[5,3]").setFocus()
            session.findById("wnd[0]/usr/lbl[5,3]").caretPosition = 11
            session.findById("wnd[0]").sendVKey(2)
            session.findById("wnd[0]/mbar/menu[4]/menu[5]/menu[2]/menu[1]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
            name3=f'[{system}] {nos} {fil_q[key]} queue3 {stamp}.html'
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name3
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 5
            session.findById("wnd[1]/tbar[0]/btn[11]").press()
            session.findById("wnd[0]/usr/lbl[99,3]").setFocus()
            session.findById("wnd[0]/usr/lbl[99,3]").caretPosition = 7
            session.findById("wnd[0]").sendVKey(2)
            ### Capture Screenshot ###
            ssname=path+f'{nos} [{system}] {fil_q[key]} {stamp}.jpg'
            try:
                message1=session.findById("wnd[0]/sbar").text
                print(message1)
                import time
                if message1=="No log was found for these selection criteria":
                    time.sleep(2)
                    session.findById("wnd[0]").HardCopy(ssname, 1)
                    session.findById("wnd[0]/tbar[0]/btn[3]").press()
                    session.findById("wnd[0]/tbar[0]/btn[3]").press()
                    session.findById("wnd[0]/tbar[0]/btn[3]").press()
                    break
                
                session.findById("wnd[0]/usr/subSUBSCREEN:SAPLSBAL_DISPLAY:0101/cntlSAPLSBAL_DISPLAY_CONTAINER/shellcont/shell/shellcont[1]/shell").contextMenu()
                session.findById("wnd[0]/usr/subSUBSCREEN:SAPLSBAL_DISPLAY:0101/cntlSAPLSBAL_DISPLAY_CONTAINER/shellcont/shell/shellcont[1]/shell").currentCellColumn = "T_MSG"
                session.findById("wnd[0]/usr/subSUBSCREEN:SAPLSBAL_DISPLAY:0101/cntlSAPLSBAL_DISPLAY_CONTAINER/shellcont/shell/shellcont[1]/shell").selectedRows = "0"
                session.findById("wnd[0]/usr/subSUBSCREEN:SAPLSBAL_DISPLAY:0101/cntlSAPLSBAL_DISPLAY_CONTAINER/shellcont/shell/shellcont[1]/shell").pressToolbarContextButton("&MB_EXPORT")
                session.findById("wnd[0]/usr/subSUBSCREEN:SAPLSBAL_DISPLAY:0101/cntlSAPLSBAL_DISPLAY_CONTAINER/shellcont/shell/shellcont[1]/shell").selectContextMenuItem("&HTML")
                session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
                name4=f'{nos} Error Page {stamp}.html'
                session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name4
                session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 10
                session.findById("wnd[1]/tbar[0]/btn[11]").press()
                # Filtering 'Red' Status #
                session.findById("wnd[0]/usr/subSUBSCREEN:SAPLSBAL_DISPLAY:0101/cntlSAPLSBAL_DISPLAY_CONTAINER/shellcont/shell/shellcont[1]/shell").currentCellRow = -1
                session.findById("wnd[0]/usr/subSUBSCREEN:SAPLSBAL_DISPLAY:0101/cntlSAPLSBAL_DISPLAY_CONTAINER/shellcont/shell/shellcont[1]/shell").selectColumn("%_ICON")
                session.findById("wnd[0]/usr/subSUBSCREEN:SAPLSBAL_DISPLAY:0101/cntlSAPLSBAL_DISPLAY_CONTAINER/shellcont/shell/shellcont[1]/shell").pressToolbarButton("&MB_FILTER")
                session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = "@5C\QError@"
                session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").caretPosition = 11
                session.findById("wnd[1]/tbar[0]/btn[0]").press()
                session.findById("wnd[0]/usr/subSUBSCREEN:SAPLSBAL_DISPLAY:0101/cntlSAPLSBAL_DISPLAY_CONTAINER/shellcont/shell/shellcont[0]/shell").setColumnWidth("101",450)
                session.findById("wnd[0]").HardCopy(ssname, 1)
                # Back to Queue Page #
                session.findById("wnd[0]/tbar[0]/btn[3]").press()
            except:
                try:
                    session.findById("wnd[1]").HardCopy(ssname, 1)
                    session.findById("wnd[1]").close()
                except:
                    session.findById("wnd[0]").HardCopy(ssname, 1)
            finally:
                session.findById("wnd[0]/tbar[0]/btn[3]").press()
                session.findById("wnd[0]/tbar[0]/btn[3]").press()
                session.findById("wnd[0]/tbar[1]/btn[6]").press()
                nos+=1
        return {"value":val,'status':status,'backlogs':backlogs}
    
    except Exception as e:
        print({'Error in smq2':e})
        return {"value":val,'status':status,'backlogs':backlogs}