import os
from docx import Document
from docxtpl import DocxTemplate
from docx.shared import Inches
import shutil
# org='DCF.docx'
# tar=path+f'AutoSAP_Report_{stamp}.xlsx'
# doc=DocxTemplate(os.getcwd()+"\Closure_Doc.docx")

def gen(org,tar,path,stamp,data={}):

    shutil.copy(org,tar)
    print("Copied Successfully")
    doc = DocxTemplate(tar)
    screenshots = [f for f in os.listdir(path) if f.endswith('.png')]
    print(screenshots)
    context={"request_item":data['request_item'],"date":stamp,"Request_type":"115","login_id":"AutoSAP Automation"}
        
    doc.render(context)
    print(os.listdir(path))
    for j in os.listdir(path):
        if j.lower().endswith(".png"):
            # print(i)
            # mail.Attachments.Add(Source=path+i)
            doc.add_heading(f" {j}",3)
            doc.add_picture(path+"\\"+j,width=Inches(5),height=Inches(3))
            
    # outputerror_path = os.path.join(path, f"[ERROR] SD {system} Post Functional Checks {stamp}.docx")
    doc.save(tar)

if __name__ == "__main__":
    import os
    import logon
    import datetime
    #docid = "444517"
    docid = "445511"
    # RBQ= "4.4 - RBQ - SAP ERP 6.0(R/3) System Informal System"
    # session=logon.Autosap(RBQ)
    uuser = "mg992450"
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    org=os.path.join(os.getcwd(),'Data Change Form.docx')
    
    path=r"C:\Users\el491900\OneDrive - GSK\Desktop\scripts\venv\AutosapSNOW\excel data\AutoSAP_2025-04-11-19-42-22\SCTASK2707364"
    tar=path+f'AutoSAP_Report_{stamp}.docx'
    gen(org,tar,path,stamp,data={"request_item":"123"})
    # tempdir= f"autosap {stamp}"
    # path = os.path.join(os.getcwd(), "excel data", f"autosap {stamp}")
    # print(dpforward(session,path,stamp,docid,uuser))