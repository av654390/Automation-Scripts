# ****************************************************************************
#  Program Description : Script Performs SAP Actions to find Sum_of_X        *
#  Program Name:  AutosapBW\targetsap.py                                     *
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

# Function to Find the Sum of X in Target(BIP) #
def targetsap(nos=0,session=0,path=0,stamp=0,dict1=0):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nrsa1"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/shellcont[0]/shell/shellcont[1]/shell/shellcont[1]/shell").selectItem("          5","1")
        session.findById("wnd[0]/shellcont[0]/shell/shellcont[1]/shell/shellcont[1]/shell").ensureVisibleHorizontalItem("          5","1")
        session.findById("wnd[0]/shellcont[0]/shell/shellcont[1]/shell/shellcont[1]/shell").topNode = "          1"
        session.findById("wnd[0]/shellcont[0]/shell/shellcont[1]/shell/shellcont[1]/shell").clickLink("          5","1")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[0]/shell/shellcont[1]/shell/shellcont[1]/shell").selectItem("         89","COL1")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[0]/shell/shellcont[1]/shell/shellcont[1]/shell").ensureVisibleHorizontalItem("         89","COL1")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[0]/shell/shellcont[1]/shell/shellcont[1]/shell").itemContextMenu("         89","COL1")
        session.findById("wnd[0]/shellcont[1]/shell/shellcont[0]/shell/shellcont[1]/shell/shellcont[1]/shell").selectContextMenuItem("DISPLAY_CONTENT")
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/cntlG_CONTAINER_2010/shellcont/shell/shellcont[0]/shell").pressButton("DESELECT_ALL")
        session.findById("wnd[1]/usr/cntlG_CONTAINER_2010/shellcont/shell/shellcont[0]/shell").pressButton("SEARCH")
        session.findById("wnd[2]/usr/txtG_FIND_STRING").text = "sum_of_x"
        session.findById("wnd[2]/usr/txtG_FIND_STRING").caretPosition = 8
        session.findById("wnd[2]/tbar[0]/btn[71]").press()
        session.findById("wnd[1]/usr/cntlG_CONTAINER_2010/shellcont/shell/shellcont[1]/shell").selectItem("        330","SELECT")
        session.findById("wnd[1]/usr/cntlG_CONTAINER_2010/shellcont/shell/shellcont[1]/shell").ensureVisibleHorizontalItem("        330","SELECT")
        session.findById("wnd[1]/usr/cntlG_CONTAINER_2010/shellcont/shell/shellcont[1]/shell").changeCheckbox("        330","SELECT",True)
        session.findById("wnd[1]/usr/cntlG_CONTAINER_2010/shellcont/shell/shellcont[0]/shell").pressButton("SEARCH")
        session.findById("wnd[2]/usr/txtG_FIND_STRING").text = "0insp_lot"
        session.findById("wnd[2]/usr/txtG_FIND_STRING").caretPosition = 9
        session.findById("wnd[2]/tbar[0]/btn[71]").press()
        session.findById("wnd[1]/usr/cntlG_CONTAINER_2010/shellcont/shell/shellcont[0]/shell").pressButton("SEARCHN")
        session.findById("wnd[1]/usr/cntlG_CONTAINER_2010/shellcont/shell/shellcont[0]/shell").pressButton("SEARCHN")
        session.findById("wnd[1]/usr/cntlG_CONTAINER_2010/shellcont/shell/shellcont[0]/shell").pressButton("SEARCHN")
        session.findById("wnd[1]/usr/cntlG_CONTAINER_2010/shellcont/shell/shellcont[0]/shell").pressButton("SEARCHN")
        session.findById("wnd[1]/usr/cntlG_CONTAINER_2010/shellcont/shell/shellcont[1]/shell").selectItem("         87","SELECT")
        session.findById("wnd[1]/usr/cntlG_CONTAINER_2010/shellcont/shell/shellcont[1]/shell").ensureVisibleHorizontalItem("         87","SELECT")
        session.findById("wnd[1]/usr/cntlG_CONTAINER_2010/shellcont/shell/shellcont[1]/shell").changeCheckbox("         87","SELECT",True)
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/usr/btn%_C001_%_APP_%-VALU_PUSH").press()
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
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/tbar[0]/btn[8]").press()

        session.findById("wnd[0]/tbar[1]/btn[25]").press()
        session.findById("wnd[0]/tbar[1]/btn[25]").press()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        try:
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").setCurrentCell(-1,"K____3767")
        except:
            session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").currentCellColumn = "K____3767"            
        session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectColumn("K____3767")
        session.findById("wnd[0]/tbar[1]/btn[30]").press()
        ssname=path+f'{nos} Sum in Target {stamp}.png'
        session.findById("wnd[0]").HardCopy(ssname, 1)
        print("Sum in Source Screenshot Taken Successfully!")

    except Exception as e:
        print({"Error in TargetSAP":e})