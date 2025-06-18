# ****************************************************************************
#  Program Description : Script Performs ST07 T-Code Action in SAP           *
#  Program Name:  AutosapBASIS\st07.py                                       *
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

def st07(nos=0,session=0,path=0,stamp=0):
    try:
        print("\n##### ST07 #####")
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nst07"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/mbar/menu[4]/menu[5]/menu[2]/menu[1]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
        name1=f"{nos} ST07 {stamp}.html"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
        session.findById("wnd[1]/tbar[0]/btn[11]").press()

        import pandas as pd 
        df1=pd.read_html(path+name1,header=1)[1]
        # Column Names : ['Unnamed: 0', 'LoggedOn', 'Active', 'In\xa0WP', 'User', 'Server']
        row=df1[df1['Unnamed: 0']=='Total'].index
        print("Row No of 'Total' : ",row[0])
        act_users=df1.loc[row[0],'Active']
        wpo=df1.loc[row[0],'In\xa0WP']

        if wpo<150:
            wps='Green'
        elif wpo>=150 and wpo<260:
            wps='Amber'
        elif wpo>=260:
            wps='Red'

        if act_users<550:
            acts='Green'
        elif act_users>=550 and act_users<650:
            acts='Amber'
        elif act_users>=650:
            acts='Red'
        print('WP Occupied-',wpo)
        print('Active Users-',act_users)
        return {'wpo':{'value':wpo,'status':wps},'act':{'value':act_users,'status':acts}}
    
    except Exception as e:
        print({'Error in ST07':e})
        return {'wpo':{'value':'Nan','status':"Check Manually"},'act':{'value':'Nan','status':"Check Manually"}}
    
