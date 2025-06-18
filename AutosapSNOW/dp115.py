import os
import datetime

def checkrole(session,touser):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nSU01D"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").text = "el491900"
        session.findById("wnd[0]/usr/ctxtSUID_ST_BNAME-BNAME").caretPosition = 8
        session.findById("wnd[0]/tbar[1]/btn[7]").press()
        session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_WORKPLACE-DEPARTMENT").setFocus()
        role = session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpADDR/ssubMAINAREA:SAPLSUID_MAINTENANCE:1900/txtSUID_ST_NODE_WORKPLACE-DEPARTMENT").text
        print("VAr",var)
        return role
    except Exception as e:
        print("Error while checking User Role:",e)
        return "O"
def dpinsider(session,path,docid,uuser):
    try:
        session.findById("wnd[0]").HardCopy(f"{path}/A before {docid}.png", 1)
        # filter
        session.findById("wnd[0]/usr/lbl[13,8]").setFocus()
        session.findById("wnd[0]/usr/lbl[13,8]").caretPosition = 0
        session.findById("wnd[0]").sendVKey( 2)
        session.findById("wnd[0]/mbar/menu[1]/menu[3]").select()
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = "@5W\QShow agent...@"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").caretPosition = 19
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[0]/usr/lbl[19,8]").setFocus()
        session.findById("wnd[0]/usr/lbl[19,8]").caretPosition = 1
        session.findById("wnd[0]").sendVKey( 2)
        session.findById("wnd[0]/mbar/menu[1]/menu[3]").select()
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").text = "@CS\QReady@"
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").text = "@CU\QIn Process@" # @CW?QWaiting@
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").setFocus()
        session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").caretPosition = 11
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        #filter
        session.findById("wnd[0]/usr/lbl[13,11]").setFocus()
        session.findById("wnd[0]/usr/lbl[13,11]").caretPosition = 0
        session.findById("wnd[0]").sendVKey( 2)
        session.findById("wnd[1]/usr/btnB1").press()

        try :
            session.findById("wnd[1]/tbar[0]/btn[5]").press()
        except :
            print("no overall view")
        session.findById("wnd[1]").HardCopy(f"{path}/B beforeagents {docid}.png", 1)
        session.findById("wnd[1]").close()
        session.findById("wnd[0]/usr/lbl[22,11]").setFocus()
        session.findById("wnd[0]/usr/lbl[22,11]").caretPosition = 7
        session.findById("wnd[0]").sendVKey( 2)
        session.findById("wnd[0]/mbar/menu[1]/menu[0]").select()
        # #test
        session.findById("wnd[0]/shellcont/shell").selectItem( "0016","Column2")
        session.findById("wnd[0]/shellcont/shell").ensureVisibleHorizontalItem( "0016","Column2")
        session.findById("wnd[0]/shellcont/shell").pressButton( "0016","Column2")
        session.findById("wnd[1]/usr/ctxtPCHDY-SEARK").text = uuser
        session.findById("wnd[1]/usr/ctxtPCHDY-SEARK").caretPosition = 8
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        try:
            print("user not found")
            adp = session.findById("wnd[2]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-KEYWORD[0,0]").text
            session.findById("wnd[2]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-KEYWORD[0,0]").caretPosition = 6
            session.findById("wnd[2]").HardCopy(f"{path}/usererrorscreen {docid}.png", 1)
            session.findById("wnd[2]").close()
            session.findById("wnd[1]").close()
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nex"
            session.findById("wnd[0]/tbar[0]/btn[0]").press()
            print(adp)
            return {"error":4,"message":adp,"ttype":"user"}
        except Exception as e:
            print("user found",e)
        session.findById("wnd[0]").HardCopy(f"{path}/F action {docid}.png", 1)
        
        bar = "Function executed" in session.findById("wnd[0]/sbar").text 
        print(bar)
        # return 0
        try :
            # session.findById("wnd[0]/tbar[0]/btn[3]").press()  #back
            session.findById("wnd[0]/tbar[0]/btn[15]").press() #up
            status = session.findById("wnd[0]/usr/lbl[59,4]").text
            if status in " In Process ":
                print("In Process",status)  # In Process
            else :
                session.findById("wnd[0]/tbar[0]/btn[15]").press() #up
            # filter
            try:
                session.findById("wnd[0]/mbar/menu[1]/menu[4]").select()
            except:
                print("till line 162")
            session.findById("wnd[0]/usr/lbl[13,8]").setFocus()
            session.findById("wnd[0]/usr/lbl[13,8]").caretPosition = 0
            session.findById("wnd[0]").sendVKey( 2)
            session.findById("wnd[0]/mbar/menu[1]/menu[3]").select()
            session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = "@5W\QShow agent...@"
            session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").caretPosition = 19
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[0]/usr/lbl[19,8]").setFocus()
            session.findById("wnd[0]/usr/lbl[19,8]").caretPosition = 1
            session.findById("wnd[0]").sendVKey( 2)
            session.findById("wnd[0]/mbar/menu[1]/menu[3]").select()
            session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").text = "@CS\QReady@"
            session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").text = "@CU\QIn Process@"
            session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").setFocus()
            session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").caretPosition = 11
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            #filter
            session.findById("wnd[0]/usr/lbl[13,11]").setFocus()
            session.findById("wnd[0]/usr/lbl[13,11]").caretPosition = 0
            session.findById("wnd[0]").sendVKey( 2)
            session.findById("wnd[1]/usr/btnB1").press()
        
        except Exception as e:
            print(e,"new exception")

        try :
            session.findById("wnd[1]/tbar[0]/btn[5]").press()
        except :
            print("no overall view")
        session.findById("wnd[1]").HardCopy(f"{path}/C afteragents {docid}.png", 1)
        session.findById("wnd[1]").close()
        try :
            session.findById("wnd[0]/mbar/menu[1]/menu[4]").select()
        except Exception as e:
            print(e,"error i n not found")
        session.findById("wnd[0]").HardCopy(f"{path}/D after {docid}.png", 1)

        # session.findById("wnd[0]/tbar[0]/okcd").text = "/nex"
        session.findById("wnd[0]/tbar[0]/btn[0]").press()
        return {"error":1,"message":f"{ bar} in dpforward",'ttype':'success'}
    except Exception as e:
        session.findById("wnd[0]").HardCopy(f"{path}/error {docid}.png", 1)
        # print(f"in rrforward {e}")
        return {"error":5,"message":f"in dpforward {e}",'ttype':'dpforward'}


def dpforward(session, path, stamp, docid,uuser):
    try:
        #dpstatus = 0
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/n/opt/vim_analytics"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtS_DPNUM-LOW").text = docid
        session.findById("wnd[0]/usr/ctxtS_DPNUM-LOW").setFocus()
        session.findById("wnd[0]/usr/ctxtS_DPNUM-LOW").caretPosition = 6
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        
        try:
            print("rrrrrrrrrrrrr")
            adp = session.findById("wnd[1]/usr/txtMESSTXT1").text
            session.findById("wnd[1]").HardCopy(f"{path}/errorscreen.png", 1)
            session.findById("wnd[1]").close()
            session.findById("wnd[0]").HardCopy(f"{path}/dp.png", 1)
            print(adp)
            return {"error": 2, "message": adp, "ttype": "DP"}
        except Exception as e:
            print("dp found", e)

        try:
            session.findById("wnd[0]/tbar[1]/btn[18]").press()
            session.findById("wnd[0]/usr/cntlCL_GRID/shellcont/shell").currentCellColumn = ""
            session.findById("wnd[0]/usr/cntlCL_GRID/shellcont/shell").selectedRows = "0"
            session.findById("wnd[0]/usr/cntlCL_GRID/shellcont/shell").pressToolbarContextButton("&MB_EXPORT")
            session.findById("wnd[0]/usr/cntlCL_GRID/shellcont/shell").selectContextMenuItem("&PC")
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
            name = f'dp115_{stamp}.html'
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 10
            session.findById("wnd[1]/tbar[0]/btn[11]").press()
            print("kkkkkkkkk")
        except Exception as e:
            session.findById("wnd[0]").HardCopy(f"{path}/dperror.png", 1)
            print(e)
            return {"error": 2, "message": e, "ttype": "DP"}
        # Construct the full path for the HTML file
        import os
        import pandas as pd

        file_path = os.path.join(path, name)
        print("Reading HTML file:", file_path)  # Debug print to verify the file path

        # Check if the file exists before attempting to read it
        if os.path.exists(file_path):
            try:
                aass = pd.read_html(file_path, header=0)[0]  # Read table
                aass.columns = [col.replace("\xa0", " ").strip().lower() for col in aass.columns]  # Standardize column names
                # print(aass.columns)
                # Define possible column name variations
                doc_status_cols = ["doc status", "document status","documentstatus"]
                current_role_cols = ["current role","cur role"]
                wi_status_cols = ["wi status", "workflow status"]

                # Find the correct column names
                doc_status_col = next((col for col in doc_status_cols if col in aass.columns), None)
                current_role_col = next((col for col in current_role_cols if col in aass.columns), None)
                wi_status_col = next((col for col in wi_status_cols if col in aass.columns), None)

                # Ensure all required columns exist
                # if not all([doc_s

                # Debugging: Print assigned column names
                print(f"DOC Status Column: {doc_status_col}")
                print(f"Current Role Column: {current_role_col}")
                print(f"WI Status Column: {wi_status_col}")
                # if not doc_status_col:
                #     return {"error":4,"message":"No valid rows found","ttype":"dpstatus"}
                # Standardize column values (lowercase, remove spaces)
                for col in [doc_status_col, current_role_col, wi_status_col]:
                    aass[col] = aass[col].fillna("").astype(str).str.strip().str.lower().str.replace("\xa0", " ")

                # Define allowed DOC status values (in lowercase)
                allowed_status = {
                    "rejected by approver", "approval complete", "approval recalled",
                    "created", "blocked", "scanned", "indexed", "doc creation in bg failed",
                    "document created", "sent for rescan", "rescan complete",
                    "suspected duplicate", "confirmed duplicate", "sent back",
                    "move forward to workflow", "sent to workflow"
                }

                # Define roles that should be excluded (in lowercase)
                excluded_roles = {"ZNPO_AP_ICSS", "ZNPO_AP_OFFSHOR", "ZPO_AP_ICSS", "ZPO_AP_OFFSHOR"}  #ZNPO_AP_OFFSHOR

                # Print unique values for debugging
                print("Unique DOC status values:", aass[doc_status_col].unique())
                print("Unique Current Role values:", aass[current_role_col].unique())
                print("Unique WI Status values:", aass[wi_status_col].unique())
                print("ABC:",any(aass[doc_status_col].isin(allowed_status)))
                if any(aass[current_role_col].isin(excluded_roles)):
                    role = checkrole(session,uuser)
                    msg = f"DP Role is {aass[current_role_col]}  And the role of {uuser} is {role}"
                    if role.startswith('P2P'):
                        print(f"{msg}. Hence Proceeding to next step! ")
                    else:
                        return {"error":6,"message":msg,'ttype':"userrole"}
                
                if any(aass[doc_status_col].isin(allowed_status)):
                    pass
                else:
                    return {"error":3,"message":f"DP status is {aass[doc_status_col]}",'ttype':"dpStatus"}
                # Filter data based on conditions
            
                filtered_df = aass[
                    (aass[doc_status_col].isin(allowed_status)) &  # DOC status matches
                    (~aass[current_role_col].isin(excluded_roles)) &  # Not in excluded roles
                    (aass[wi_status_col] == "in process")  # WI Status must be 'In Process'
                ]

                # Print filtered count
                print("Filtered rows count:", filtered_df.shape[0])
                print(filtered_df)

                # Proceed only if there are valid rows
                if not filtered_df.empty:
                    print("Valid rows found, proceeding with further processing...")
                    session.findById("wnd[0]").HardCopy(f"{path}/DPstatus.png", 1)

                    # Extract matching row indices from the DataFrame
                    valid_row_indices = filtered_df.index.tolist()
                    print(f"Valid SAP GUI Row Indices: {valid_row_indices}")

                    # Convert indices to a comma-separated string (SAP expects this format)
                    selected_rows_str = ",".join(map(str, valid_row_indices))
                    
                    # Select only the correct rows in SAP GUI
                    session.findById("wnd[0]/usr/cntlCL_GRID/shellcont/shell").selectedRows = selected_rows_str
                    
                    # Proceed with next action
                    session.findById("wnd[0]/usr/cntlCL_GRID/shellcont/shell").pressToolbarButton("WFLOG")

                    print("pppppppppppp")
                    return dpinsider(session, path, docid, uuser)
                else:
                    print("No valid rows found, stopping execution.")
                    return {"error":3,"message":"No valid rows found","ttype":"dpstatus"}
            except Exception as e:
                print(f"Unexpected error in dpforward: {e}")
                return {"error":5,"message":e,"ttype":"Unexpected"}
        else:
            print("File does not exist:", file_path)

    except Exception as e:
        print(f"Unexpected error in dpforward: {e}")
        return {"error":5,"message":e,"ttype":"Unexpected"}

        
        

if __name__ == "__main__":
    import os
    import logon
    import datetime
    #docid = "444517"
    docid = "445511"
    RBQ= "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    session=logon.Autosap(RBQ)
    uuser = "mg992450"
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # tempdir= f"autosap {stamp}"
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    # print(dpforward(session,path,stamp,docid,uuser))
    checkrole(session,'el491900')