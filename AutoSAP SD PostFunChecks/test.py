                    # session.findById("wnd[0]/mbar/menu[5]/menu[5]/menu[2]/menu[2]").select()
                    # session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
                    # session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
                    # session.findById("wnd[1]/tbar[0]/btn[0]").press()
                    # session.findById("wnd[1]/usr/ctxtDY_PATH").text = path #"C:\Users\as776099\OneDrive - GSK\Documents\SAP\SAP GUI\"
                    # name1 = f"{nos} [{sid}] sm37 {stamp}.html"
                    # session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = name1
                    # session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
                    # session.findById("wnd[1]/tbar[0]/btn[11]").press()

# import pandas as pd
# f = pd.read_html('va05n.html', header=0)[0]
# print(f)
# Doc_ids=[]
# # for i in f.index:
#     #Doc_ids.append(f['Document'][i])
# Doc_ids = f['Document'].tolist()
# print(Doc_ids)

# for i in range(5):
#     if i ==4:
#         print("if-",i)
#         # break
#     else:
#         print(i)
    
# else:
#     print("10 not found")

# f = pd.read_html("va05n.html",header=0)[0]
# #print(f)
# a=[]
# # for i in f:
#     a.append(i)
#print(a) 
#['Document', 'TrG', 'Descript.', 'SaTy', 'Description', 'Sold-To\xa0Pt'or'Sold-To\xa0Party', 'Created\xa0On', 'Doc.\xa0Date', 'PO\xa0Number', 'Funct', 'Respons.', 'Created\xa0By', 'SOrg.', 'DChl', 'Dv', 'SOff.', 'SGrp', 'Curr.', 'Net\xa0value']
# for i in f.index:
#     a.append(int(f['Document'][i]))
# print(a)
# document_value = f.loc[0, 'Document']  # 0 refers to the first row, 'Document' is the column name
# print(document_value)

# import re
# with open('va03.txt', 'r') as file:
#     content = file.read()  # Reads the entire content as one string
# # Regex search for the first "Outbound Delivery" and "Invoice"
# outbound_match = re.search(r"Outbound Delivery (\d+)", content)
# invoice_match = re.search(r"Invoice (\d+)", content)
# # Print results
# if outbound_match and invoice_match:
#     print(f"First 'Outbound Delivery' ID: {outbound_match.group(1)}")
#     print(f"First 'Invoice' ID: {invoice_match.group(1)}")
#     print(f"Found both Outbound Delivery and Invoice for Doc ID: {id}")

# import pandas as pd
# g = pd.read_html("vf03.html",header = 0 )[0]
# print(g)
# a=[]
# for i in g:
#     a.append(i)
# print(a)
#['Ap', 'Object\xa0key', 'Msg.', 'Lng', 'Partner', 'Role', 'Created\xa0On', 'Time', 'Addr.\xa0No.', 'Med', 'No.', 'Time.1', 'Date', 'TimeFrom', 'To\xa0Time', 'N', 'Proc.date', 'Prc.time', 'Resp.date', 'User', 'Status', 'A', 'Strategy', 'Output\xa0Device', 'DSN', 'Suf1', 'Suffix\xa02', 'I', 'R', 'Fax', 'Telex', 'Teletex', 'Chng.', 'Repeat.', 'Not\xa0used', 'Not\xa0used.1', 'Not\xa0used.2', 'Not\xa0used.3', 'Form', 'Module', 'Not\xa0used.4', 'Not\xa0used.5', 'Not\xa0used.6', 'Not\xa0used.7', 'Not\xa0used.8', 'Obj.key', 'ID', 
#'Language', 'Dunn.\xa0Date', 'Dunn.\xa0Time', 'DR', 'Not\xa0used.9', 'Not\xa0used.10', 'Type', 'Requested\xa0Status', 'StatusMail', 
#'Not\xa0used.11', 'Not\xa0used.12', 'Not\xa0used.13', 'Not\xa0used.14', 'Not\xa0used.15', 'Not\xa0used.16', 'Not\xa0used.17', 'Not\xa0used.18', 'Automatic', 'Recipient', 'Department', 'SAP\xa0cover', 'Text', 'Auth.', 'Arch.Mode', 'ArchiveNo.', 'Number', 'Address', 'Event', 'Sort\xa0Order', 'Sort\xa0Order.1', 'Sort\xa0Order.2', 'Obj.type', 'Time\xa0pl.', 'Ctr', 'Data\xa0Filter\xa0Value\xa0for\xa0Data\xa0Aging']
# invoice_id = g.loc[0,'Object\xa0key']
# print(invoice_id)

# output = [{'status':1},{'status':1},{'status':0,'error':'A'},{'status':1},{'status':0,'error':'B'}]
# oastatus = 0 if any(item['status']==0 for item in output) else 1
# errormsgs = [msg.get('error') for msg in output if msg.get('error') ]

# print("Output : ",output)
# print("OA Status : ",oastatus)
# print("Error : ",errormsgs)

import pandas as pd
f = pd.read_html("sm37.html",header = 0)[0]
#print(f)
# a = []
# for i in f:
#     a.append(i)
#print(a) #['JobName', 'Spool', 'Job\xa0doc', 'Job\xa0CreatedB', 'Status', 'Start\xa0date', 'Start\xa0Time', 'Duration(sec.)', 'Delay\xa0(sec.)']
g = f['Status']
print(g)