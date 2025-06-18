# ****************************************************************************
#  Program Description : Script Performs DB02 T-Code Action in SAP           *
#  Program Name:  AutosapBASIS\db02.py                                       *
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

def db02(nos=0,session=0,path=0,stamp=0):
    try:
        print("\n##### DB02 #####")
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/ndb02"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").selectItem("       1007-","Task")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").ensureVisibleHorizontalItem("       1007-","Task")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").doubleClickItem("       1007-","Task")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").selectItem("       1008","Task")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").ensureVisibleHorizontalItem("       1008","Task")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").doubleClickItem("       1008","Task")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").selectItem("         47","Task")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").ensureVisibleHorizontalItem("         47","Task")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[1]/shell").doubleClickItem("         47","Task")
        session.findById("wnd[0]/usr/tabsTS_TABSTRIP/tabpTS_TABSTRIP_TAB1_/ssub221_SCA:SAPLS_ORA_COCKPIT_5:0221/cntlCC_TAB1_0221/shellcont/shell").pressToolbarContextButton("&MB_EXPORT")
        session.findById("wnd[0]/usr/tabsTS_TABSTRIP/tabpTS_TABSTRIP_TAB1_/ssub221_SCA:SAPLS_ORA_COCKPIT_5:0221/cntlCC_TAB1_0221/shellcont/shell").selectContextMenuItem("&PC")
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        name=f'{nos} DB02_TableSpace_{stamp}.html'
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        import pandas as pd
        df2=pd.read_html(path+name,header=0)[0]
        ## Column Names in df2 ['Tablespace\xa0name', 'Size(MB)', 'Free(MB)', 'Used(%)', 'Autoextend', 'Total\xa0size(MB)', 'Total\xa0free\xa0space(MB)', 'Total\xa0used\xa0(%)', '#Files', '#Segments', '#Extents', 'Status', 'Contents', 'Compression', 'Compress\xa0for', 'Encrypted', 'Encrypt\xa0algorithm'] ##
        req=['PSAPR3I','PSAPUNDO','PSAPR3I750','PSAPR3IINDEX','PSAPSOFFCONT1']
        db02_dict={}
        for k in req:
            try:
                val=df2.loc[df2['Tablespace\xa0name']==k,'Used(%)'].values[0]
                if val <85:
                    status='Green'
                elif val>=85 and val<=90:
                    status='Amber'
                else:
                    status='Red'
            except:
                val='Nan'     
                status='Check Manually'       
        
            db02_dict[k]={'value':val,'status':status}
        return db02_dict
    
    except Exception as e:
        print({'error in DB02':e})
        return {'Check Manually':{'value':'Nan','status':'Check Manually'}}
    
