If Not IsObject(application) Then
   Set SapGuiAuto  = GetObject("SAPGUI")
   Set application = SapGuiAuto.GetScriptingEngine
End If
If Not IsObject(connection) Then
   Set connection = application.Children(0)
End If
If Not IsObject(session) Then
   Set session    = connection.Children(0)
End If
If IsObject(WScript) Then
   WScript.ConnectObject session,     "on"
   WScript.ConnectObject application, "on"
End If
session.findById("wnd[0]").maximize
session.findById("wnd[0]/tbar[0]/okcd").text = "\nsm37"
session.findById("wnd[0]/tbar[0]/btn[0]").press()
session.findById("wnd[0]/usr/chkBTCH2170-PRELIM").selected = true
session.findById("wnd[0]/usr/chkBTCH2170-SCHEDUL").selected = true
session.findById("wnd[0]/usr/chkBTCH2170-READY").selected = true
session.findById("wnd[0]/usr/chkBTCH2170-RUNNING").selected = true
session.findById("wnd[0]/usr/chkBTCH2170-FINISHED").selected = true
session.findById("wnd[0]/usr/chkBTCH2170-ABORTED").selected = true
session.findById("wnd[0]/usr/txtBTCH2170-JOBNAME").text = "z_*_APO_D_CIF_DELTA"
session.findById("wnd[0]/usr/txtBTCH2170-USERNAME").text = "*"
session.findById("wnd[0]/usr/ctxtBTCH2170-FROM_DATE").text = "02.05.2024"
session.findById("wnd[0]/usr/ctxtBTCH2170-TO_DATE").text = "02.05.2024"
session.findById("wnd[0]/usr/ctxtBTCH2170-FROM_TIME").setFocus
session.findById("wnd[0]/usr/ctxtBTCH2170-FROM_TIME").caretPosition = 0
session.findById("wnd[1]/tbar[0]/btn[0]").press()
session.findById("wnd[0]/usr/ctxtBTCH2170-FROM_TIME").text = "12:10:36"
session.findById("wnd[0]/usr/ctxtBTCH2170-TO_TIME").text = "12:10:36"
session.findById("wnd[0]/usr/ctxtBTCH2170-TO_TIME").caretPosition = 8
session.findById("wnd[0]/tbar[1]/btn[8]").press()
session.findById("wnd[0]/usr/ctxtBTCH2170-FROM_DATE").setFocus
session.findById("wnd[0]/usr/ctxtBTCH2170-FROM_DATE").caretPosition = 10
session.findById("wnd[0]").sendVKey( 4)

session.findById("wnd[0]/tbar[1]/btn[8]").press()
session.findById("wnd[0]/tbar[1]/btn[8]").press()
session.findById("wnd[0]/mbar/menu[5]/menu[5]/menu[2]/menu[1]").select()
session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").select()
session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[3,0]").setFocus()
session.findById("wnd[1]/tbar[0]/btn[0]").press()
session.findById("wnd[1]/usr/ctxtDY_PATH").text = "C:\Users\nc843765\OneDrive - GSK\Documents\SAP\SAP GUI\"
session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "nk.html"
session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 7
session.findById("wnd[1]/tbar[0]/btn[11]").press()
