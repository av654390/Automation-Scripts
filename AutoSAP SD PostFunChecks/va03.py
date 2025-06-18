def va03(no, session, path, stamp, sd, ed):
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/NVA05N"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtSAUART-LOW").text = "ZEOR"
        session.findById("wnd[0]/usr/ctxtSAUDAT-LOW").text = sd
        session.findById("wnd[0]/usr/ctxtSAUDAT-HIGH").text = ed
        session.findById("wnd[0]/usr/ctxtSAUDAT-HIGH").setFocus()
        session.findById("wnd[0]/usr/ctxtSAUDAT-HIGH").caretPosition = 10
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        try:
            import time
            message1=session.findById("wnd[0]/sbar").text
            print(message1)
            if message1=="No documents were found for these selection criteria":
                time.sleep(2)
                errorss=f'{path}/Error_VA05N.png'
                session.findById("wnd[0]").HardCopy(path+errorss, 1)
                return {"error":"Error while capturing Display Sales Document ID",'status':0}
        except Exception as e:
            print({"document id found",e})
        session.findById("wnd[0]/tbar[1]/btn[45]").press()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = path  # "C:\\Users\\as776099\\OneDrive - GSK\\Documents\\SAP\\SAP GUI\\"
        name = f'{no}_va05n_{stamp}.html'
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        import os
        import pandas as pd
        file_path = os.path.join(path, name)
        f = pd.read_html(file_path, header=0)[0]
        Doc_ids = []
        try:
            Doc_ids = f['Document'].tolist()
        except:
            Doc_ids = f['SD\xa0Document'].tolist()
        # print(Doc_ids)
        # Loop through all Doc_ids
        for id in Doc_ids:
            session.findById("wnd[0]/tbar[0]/okcd").text = "/nva03"
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/ctxtVBAK-VBELN").text = id
            session.findById("wnd[0]/usr/ctxtVBAK-VBELN").caretPosition = 9
            session.findById("wnd[0]").sendVKey(0)
            ss_va03 = f"{path}/{no}. VA03-Display Sales Document & Document Flow.png"
            session.findById("wnd[0]").HardCopy(ss_va03, 1)
            try:
                session.findById("wnd[0]/mbar/menu[5]/menu[11]").select()
                ss_va03_status = f"{path}/{no}. VA03-Display Sales Document & Document Flow_Status.png"
                session.findById("wnd[1]").HardCopy(ss_va03_status, 1)
                session.findById("wnd[1]").close()
                print("Taken Status screenshot of VA03")
            except Exception as e:
                print("Unable to take status screenshot of VA03 :",str(e))

            session.findById("wnd[0]/tbar[1]/btn[5]").press()
            session.findById("wnd[0]/usr/shell/shellcont[1]/shell[0]").pressContextButton("&PRINT_BACK")
            session.findById("wnd[0]/usr/shell/shellcont[1]/shell[0]").selectContextMenuItem("&PRINT_PREV")
            session.findById("wnd[0]/mbar/menu[3]/menu[5]/menu[2]/menu[2]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").select()
            session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").setFocus()
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            session.findById("wnd[1]/usr/ctxtDY_PATH").text = path
            name1 = f'va03_txt.txt'
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1
            session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 8
            session.findById("wnd[1]/tbar[0]/btn[11]").press()

            # Check for outbound delivery and invoice in the downloaded text file
            import os
            import re
            file_path = os.path.join(path, name1)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()  # Reads the entire content as one string

            outbound_match = re.search(r"Outbound Delivery (\d+)", content)
            if outbound_match:
                print(f"Found Outbound Delivery for Doc ID: {id}")
                print(f"Outbound Delivery : {outbound_match.group(1)}")
                #print(f"Invoice: {invoice_match.group(1)}")
                session.findById("wnd[0]/tbar[0]/okcd").text = "/nvl03n"
                session.findById("wnd[0]").sendVKey(0)
                session.findById("wnd[0]/usr/ctxtLIKP-VBELN").text = outbound_match.group(1)
                session.findById("wnd[0]/usr/ctxtLIKP-VBELN").caretPosition = 10
                session.findById("wnd[0]").sendVKey(0)
                no +=1
                ss_vl03n = f"{path}/{no}. VL03N-Display Delivery Document.png"
                session.findById("wnd[0]").HardCopy(ss_vl03n, 1)
                try:
                    session.findById("wnd[0]/mbar/menu[6]/menu[11]").select()
                    ss_vl03n_status = f"{path}/{no}. VL03N-Display Delivery Document_Status.png"
                    session.findById("wnd[1]").HardCopy(ss_vl03n_status, 1)
                    session.findById("wnd[1]").close()
                    print("Taken Status screenshot of VL03N")
                except Exception as e:
                    print("Unable to take Status screenshot of VL03N :",str(e))    
                try:
                    # Try to get the 'Sold-To Party' value for the matching Doc ID
                    sold_to_party = f.loc[f['Document'] == id, 'Sold-To\xa0Pt'].values[0]
                    print(f"Sold-To Party for Doc ID {id}: {sold_to_party}")
                except IndexError:  # In case no match is found for the 'Document' column
                    print(f"Sold-To Party not found for Doc ID {id}")
                    sold_to_party = "1100290311"
                
                return {"sold_to_party" : sold_to_party, "status" : 1}  
            else:
                print(f"Outbound Delivery not found for Doc ID: {id}")
                #continue  # Skip to the next Doc ID if they are not found
        else:
            print(f"Outbound Delivery not found for Doc ID of entire week: {id}")
            return {"sold_to_party" : "1100290311", "status" : 2}
    except Exception as e:
        print("error while capturing Display Sales & Outbound Delivery : ",e)
        error_ss = f"{path}/Error Display Sales Outbound Delivery.png"
        session.findById("wnd[0]").HardCopy(error_ss, 1)
        return {"status" : 0, "error" : "Error while capturing Display Sales & Outbound Delivery","sold_to_party" : "1100290311" }

if __name__ == "__main__":
    import os
    import logon
    import sender
    import datetime
    no = 1
    RBQ = "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    session = logon.Autosap(RBQ)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    os.makedirs(path, exist_ok=True)
    va03(no,session,path,stamp,sd="01.03.2025",ed="21.03.2025")  

