import pandas as pd
f = pd.read_html("me53n.html",header = 0)[0]
#print(f)
a=[]
for i in f:
    a.append(i)
print(a) #'Purch.Doc.' (sbp) ; 'Pur.\xa0Doc.' (rbp)

#f=f.loc[1,0] #when header not given
# print(f)

# f = f.loc[0,'Pur.\xa0Doc.'] #when header=0 given Purchasing
# print(f)

# f = f.loc[0,'Mat.\xa0Doc.']
# print(f)
#"SBP":"0.1 - R/3 Production"
#['Status', 'Item', 'A', 'I', 'Material', 'Short\xa0Text', 'Quantity', 'OUn', 'C', 'Deliv.Date', 'Net\xa0Price', 'Crcy', 'Per', 'OPU', 'Matl\xa0Group', 'Plant', 'Stor.\xa0Loc.', 'Batch', 'TrackingNo', 'Requisnr.', 'Material.1', 'Info\xa0rec.', 'R', 'Free', 'T', 'Purch.Req.', 'Item.1', 'Agmt.', 'Item.2', 'RFQ', 'Item.3', 'Ref.\xa0Doc.', 'Ref.Itm', 'HLIt', 'S']