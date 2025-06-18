# ****************************************************************************
#  Program Description : Script Performs SAP Actions to Download Source Files*
#  Program Name:  AutosapBW\source.py                                        *
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
#  2           Developer      Erry Lavakumar    erry.8.lavakumar@gsk.com     *  
#  2           Developer      Akoju Sharanya    akoju.x.sharanya@gsk.com     *  
#                                                                            *
# ****************************************************************************

# Function to Download the Lots Report from Source #
def source(nos=0,session=0,path=0,stamp=0,d1=0,d2=0):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nZQME06"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/tbar[1]/btn[17]").press()
        session.findById("wnd[1]/usr/txtENAME-LOW").text = "AS347896"
        session.findById("wnd[1]/usr/txtENAME-LOW").setFocus()
        session.findById("wnd[1]/usr/txtENAME-LOW").caretPosition = 8
        session.findById("wnd[1]/tbar[0]/btn[8]").press()
        session.findById("wnd[0]/usr/ctxtS_GSTRP-LOW").text = d1 
        session.findById("wnd[0]/usr/ctxtS_GSTRP-HIGH").text = d2 
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/usr/cntlGRID_CONTAINER/shellcont/shell").pressToolbarContextButton("&MB_EXPORT")
        session.findById("wnd[0]/usr/cntlGRID_CONTAINER/shellcont/shell").selectContextMenuItem("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        name=f'Source SBT {stamp}.html'
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 7
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        return name
    except Exception as e:
        print({"Error While downloading Source(SBT) Report":e})

# Function to Find the 1. Reason for Lots Missing and 2. Sum of X # 
def se16(nos=0,session=0,path=0,stamp=0,reason='NA',dict1=0):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nse16"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtDATABROWSE-TABLENAME").text = "QASR"
        session.findById("wnd[0]/usr/ctxtDATABROWSE-TABLENAME").caretPosition = 4
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/txtMAX_SEL").text = ""
        session.findById("wnd[0]/usr/txtMAX_SEL").setFocus()
        session.findById("wnd[0]/usr/txtMAX_SEL").caretPosition = 11
        session.findById("wnd[0]/usr/btn%_I1_%_APP_%-VALU_PUSH").press()

        # Pasting the Lots #
        for i in dict1:
            if i<=7:
                session.findById(f"wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,{i}]").text = str(dict1[i])
            elif (i-1)%7==0:
                n=1
                session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE").verticalScrollbar.position = 7 if i==8 else i
                session.findById(f"wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,{n}]").text = str(dict1[i])
                n+=1
            else:
                session.findById(f"wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,{n}]").text = str(dict1[i])
                n+=1
        session.findById("wnd[1]/tbar[0]/btn[8]").press()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()

        # To Find the Reason for Lots Missing #
        if reason=='reason':
            try:
                session.findById("wnd[0]/mbar/menu[3]/menu[3]").select()
            except:
                session.findById("wnd[0]/mbar/menu[3]/menu[8]").select()
            session.findById("wnd[1]/usr/tabsG_TABSTRIP/tabp0400/ssubTOOLAREA:SAPLWB_CUSTOMIZING:0400/radRSEUMOD-TBALV_GRID").select()
            session.findById("wnd[1]/usr/tabsG_TABSTRIP/tabp0400/ssubTOOLAREA:SAPLWB_CUSTOMIZING:0400/radSEUCUSTOM-FIELDNAME").select()
            session.findById("wnd[1]/usr/tabsG_TABSTRIP/tabp0400/ssubTOOLAREA:SAPLWB_CUSTOMIZING:0400/radSEUCUSTOM-FIELDNAME").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[0]/tbar[1]/btn[45]").press()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
            name=f'{nos} Missing Lots {stamp}.html'
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 10
            session.findById("wnd[1]/tbar[0]/btn[11]").press()

            import pandas as pd 
            df=pd.read_html(path+name,header=0)[0]
            # ['MANDANT', 'PRUEFLOS', 'VORGLFNR', 'MERKNR', 'PROBENR', 'SATZSTATUS', 'ATTRIBUT', 'QERGDATH', 'ERSTELLER', 'ERSTELLDAT', 'AENDERER', 'AENDERDAT', 'MBEWERTG', 'DBEWERTG', 'PRUEFER', 'PRUEFDATUV', 'PRUEFDATUB', 'PRUEFZEITV', 'PRUEFZEITB', 'PRUEFBEMKT', 'PRLTEXTKZ', 'LTEXTSPR', 'ISTSTPUMF', 'ANZFEHLEH', 'ANTEILNI', 'ANTEIL', 'ANZFEHLER', 'ANZWERTO', 'ANZWERTU', 'ANZWERTG', 'MAXWERTNI', 'MEDIANNI', 'MINWERTNI', 'MITTELWNI', 'VARIANZNI', 'MOMENT3NI', 'MOMENT4NI', 'ANTEILONI', 'ANTEILUNI', 'MAXWERT', 'MEDIANWERT', 'MINWERT', 'MITTELWERT', 'VARIANZ', 'MOMENT3', 'MOMENT4', 'ANTEILO', 'ANTEILU', 'KATALGART1', 'GRUPPE1', 'CODE1', 'VERSION1', 'KATALGART2', 'GRUPPE2', 'CODE2', 'VERSION2', 'KATALGART3', 'GRUPPE3', 'CODE3', 'VERSION3', 'KATALGART4', 'GRUPPE4', 'CODE4', 'VERSION4', 'KATALGART5', 'GRUPPE5', 'CODE5', 'VERSION5', 'FEHLKLAS', 'SENDEFLAG', 'MASCHINE', 'POSITION', 'AENDBELEG', 'KZBEWERTG', 'ZEITERSTL', 'ZEITAEND', 'ORIGINAL_INPUT', 'DIFF_DEC_PLACES', 'INPPROC_READY', 'SIGN_ID', 'SIGN_STATE']
            # Date Column - AENDERDAT, Time Column - ZEITERSTL 
            from datetime import datetime, timedelta
            df['date']=pd.to_datetime(df['AENDERDAT'], format='%d.%m.%Y')
            df['datetime']=pd.to_datetime(df['date'].dt.strftime("%Y-%m-%d") +' '+df['ZEITERSTL'])
            yd=datetime.now()-timedelta(days=1)
            threshold=yd.replace(hour=22,minute=30,second=0,microsecond=0)
            lots_after_1030=df[df['datetime'] > threshold]
            lots_before_1030=df[df['datetime'] < threshold]
            print("Lots After 10 30",lots_after_1030[['PRUEFLOS','AENDERDAT','ZEITERSTL']])
            print("Lots Before 10 30",lots_before_1030[['PRUEFLOS','AENDERDAT','ZEITERSTL']])
            bef=lots_before_1030['PRUEFLOS'].tolist()
            aft=lots_after_1030['PRUEFLOS'].tolist()
            return {'Before':bef,'After':aft}
        
        # To Find the Sum of X in Source #
        elif reason=='sum':
            try:
                session.findById("wnd[0]/mbar/menu[3]/menu[3]").select()
            except:
                session.findById("wnd[0]/mbar/menu[3]/menu[8]").select()
            session.findById("wnd[1]/usr/tabsG_TABSTRIP/tabp0400/ssubTOOLAREA:SAPLWB_CUSTOMIZING:0400/radRSEUMOD-TBALV_GRID").select()
            session.findById("wnd[1]/usr/tabsG_TABSTRIP/tabp0400/ssubTOOLAREA:SAPLWB_CUSTOMIZING:0400/radSEUCUSTOM-FIELDNAME").select()
            session.findById("wnd[1]/usr/tabsG_TABSTRIP/tabp0400/ssubTOOLAREA:SAPLWB_CUSTOMIZING:0400/radSEUCUSTOM-FIELDNAME").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").setCurrentCell(-1,"MITTELWERT")
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").firstVisibleColumn = "MAXWERT"
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectColumn("MITTELWERT")
            session.findById("wnd[0]/tbar[1]/btn[20]").press()
            ssname=path+f'{nos} Sum in Source {stamp}.png'
            session.findById("wnd[0]").HardCopy(ssname, 1)
            print("Sum in Source Screenshot Taken Successfully!")


    except Exception as e:
        print({'Error in SE16':e})

if __name__ =='__main__':
    sid={'sbt':"1.2 - R/3 Acceptance [Informal Testing]"}
    import os
    import logon
    from datetime import datetime
    session=logon.Autosap(sid['sbt'])
    nos=0
    now=datetime.now()
    stamp=now.strftime("%Y-%m-%d-%H-%M-%S")
    cd=os.getcwd()
    path = cd + f'/excel data/AutoSAP_{stamp}/'
    print(source(nos=0,session=session,path=path,stamp=stamp))
    logon.logof(session)