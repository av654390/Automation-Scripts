import pandas as pd

# Load HTML file
dps = "dpstatus.html"
df = pd.read_html(dps, header=0)[0]  # Read HTML into DataFrame

# Clean column names by replacing non-breaking spaces and stripping whitespace
df.columns = df.columns.str.replace('\xa0', ' ', regex=False).str.strip()
print(df.columns)
# Debugging: Print original DataFrame shape
print("Original DataFrame shape:", df.shape)

# Allowed Document Status values (converted to lower case)
allowed_status = {
    "rejected by approver", "approval complete", "approval recalled",
    "created", "blocked", "scanned", "indexed", "doc creation in bg failed",
    "document created", "sent for rescan", "rescan complete",
    "suspected duplicate", "confirmed duplicate", "sent back",
    "move forward to workflow", "sent to workflow"
}

# Excluded Current Role values
excluded_roles = {"ZNPO_AP_ICSS", "ZNPO_AP_OFFSHOR", "ZPO_AP_ICSS", "ZPO_AP_OFFSHOR"}

# Debugging: Print unique values before filtering
print("\nUnique Document Status values:\n", df["Document Status"].unique())
print("\nUnique Current Role values:\n", df["Current Role"].unique())
print("\nUnique WI Status values:\n", df["WI Status"].unique())

# Apply filtering conditions
filtered_df = df[
    (df["Document Status"].str.lower().isin(allowed_status)) &  # Check allowed Document Status
    (~df["Current Role"].isin(excluded_roles)) &  # Exclude specific Current Roles
    (~df["WI Status"].str.contains("Completed", case=False, na=False))  # Exclude Completed WI Status
]

# Debugging: Print filtered DataFrame shape
print("\nFiltered DataFrame shape:", filtered_df.shape)

# Display final filtered data
if not filtered_df.empty:
    print(filtered_df)
else:
    print("No records found after filtering.")







# import pandas as pd

# # Read the table
# dps = "dp115.html"  # Ensure path and file name are correct
# aass = pd.read_html(dps, header=0)[0]  # Read table

# # Clean column names (remove non-breaking spaces '\xa0')
# aass.columns = [col.replace("\xa0", " ") for col in aass.columns]

# # Replace NaN values, convert to lowercase, and remove non-breaking spaces
# for col in ["DOC status", "Current Role", "WI Status"]:
#     aass[col] = aass[col].fillna("").astype(str).str.strip().str.lower().str.replace("\xa0", " ")

# # Define allowed DOC status values (in lowercase)
# allowed_status = {
#     "rejected by approver", "approval complete", "approval recalled",
#     "created", "blocked", "scanned", "indexed", "doc creation in bg failed",
#     "document created", "sent for rescan", "rescan complete",
#     "suspected duplicate", "confirmed duplicate", "sent back",
#     "move forward to workflow", "sent to workflow"
# }

# # Define roles that should be excluded (in lowercase)
# excluded_roles = {"ap_offshore", "ap_icss"}

# # Print unique values for debugging
# print("Unique DOC status values:", aass["DOC status"].unique())
# print("Unique Current Role values:", aass["Current Role"].unique())
# print("Unique WI Status values:", aass["WI Status"].unique())

# # Filter data based on conditions
# filtered_df = aass[
#     (aass["DOC status"].isin(allowed_status)) &  # DOC status matches
#     (~aass["Current Role"].isin(excluded_roles)) &  # Not in excluded roles
#     (aass["WI Status"] == "in process")  # WI Status must be 'In Process'
# ]

# # Print filtered count
# print("Filtered rows count:", filtered_df.shape[0])
# print(filtered_df)

# # Proceed only if there are valid rows
# if not filtered_df.empty:
#     print("Valid rows found, proceeding with further processing...")
#     # Further processing logic here
# else:
#     print("No valid rows found, stopping execution.")






#     # session.findById("wnd[0]/usr/lbl[13,8]").setFocus()
#     # session.findById("wnd[0]/usr/lbl[13,8]").caretPosition = 0
#     # session.findById("wnd[0]").sendVKey (2)
#     # session.findById("wnd[0]/mbar/menu[1]/menu[3]").select()
#     # session.findById("wnd[1]").sendVKey (4)
#     # session.findById("wnd[2]/usr/lbl[1,5]").setFocus()
#     # session.findById("wnd[2]/usr/lbl[1,5]").caretPosition = 0
#     # session.findById("wnd[2]/tbar[0]/btn[0]").press()
#     # session.findById("wnd[1]/tbar[0]/btn[0]").press()
#     # session.findById("wnd[0]/usr/lbl[19,8]").setFocus()
#     # session.findById("wnd[0]/usr/lbl[19,8]").caretPosition = 0
#     # session.findById("wnd[0]").sendVKey (2)
#     # session.findById("wnd[0]/mbar/menu[1]/menu[3]").select()
#     # session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").setFocus()
#     # session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").caretPosition = 0
#     # session.findById("wnd[1]").sendVKey (4)
#     # session.findById("wnd[2]/usr/lbl[1,5]").setFocus()
#     # session.findById("wnd[2]/usr/lbl[1,5]").caretPosition = 0
#     # session.findById("wnd[2]/tbar[0]/btn[0]").press()
#     # session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").setFocus()
#     # session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").caretPosition = 0
#     # session.findById("wnd[1]").sendVKey (4)
#     # session.findById("wnd[2]/tbar[0]/btn[0]").press()
#     # session.findById("wnd[1]/tbar[0]/btn[0]").press()
#     # session.findById("wnd[0]/usr/lbl[13,11]").setFocus()
#     # session.findById("wnd[0]/usr/lbl[13,11]").caretPosition = 0
#     # session.findById("wnd[0]").sendVKey (2)
#     # session.findById("wnd[1]/usr/btnB1").press()
#     # session.findById("wnd[1]").close()
#     # session.findById("wnd[0]/usr/lbl[22,11]").setFocus()
#     # session.findById("wnd[0]/usr/lbl[22,11]").caretPosition = 8
#     # session.findById("wnd[0]").sendVKey (2)
#     # session.findById("wnd[0]/mbar/menu[1]/menu[0]").select()
#     # session.findById("wnd[0]/shellcont/shell").selectItem ("0016","Column2")
#     # session.findById("wnd[0]/shellcont/shell").ensureVisibleHorizontalItem ("0016","Column2")
#     # session.findById("wnd[0]/shellcont/shell").pressButton ("0016","Column2")
#     # session.findById("wnd[1]/usr/ctxtPCHDY-SEARK").text = uuser
#     # session.findById("wnd[1]/usr/ctxtPCHDY-SEARK").caretPosition = 8
#     # session.findById("wnd[1]/tbar[0]/btn[0]").press()
#     # session.findById("wnd[0]/tbar[0]/btn[3]").press()
#     # session.findById("wnd[0]/usr/lbl[13,8]").setFocus()
#     # session.findById("wnd[0]/usr/lbl[13,8]").caretPosition = 0
#     # session.findById("wnd[0]").sendVKey (2)
#     # session.findById("wnd[0]/mbar/menu[1]/menu[3]").select()
#     # session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").setFocus()
#     # session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").caretPosition = 4
#     # session.findById("wnd[1]").sendVKey (4)
#     # session.findById("wnd[2]/usr/lbl[1,5]").setFocus()
#     # session.findById("wnd[2]/usr/lbl[1,5]").caretPosition = 0
#     # session.findById("wnd[2]/tbar[0]/btn[0]").press()
#     # session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").setFocus()
#     # session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").caretPosition = 11
#     # session.findById("wnd[1]").sendVKey (4)
#     # session.findById("wnd[2]/usr/lbl[1,5]").setFocus()
#     # session.findById("wnd[2]/usr/lbl[1,5]").caretPosition = 0
#     # session.findById("wnd[2]/tbar[0]/btn[0]").press()
#     # session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").setFocus()
#     # session.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-HIGH").caretPosition = 15
#     # session.findById("wnd[1]").sendVKey (4)
#     # session.findById("wnd[2]/tbar[0]/btn[0]").press()
#     # session.findById("wnd[1]/tbar[0]/btn[0]").press()
#     # session.findById("wnd[0]/usr/lbl[13,11]").setFocus()
#     # session.findById("wnd[0]/usr/lbl[13,11]").caretPosition = 0
#     # session.findById("wnd[0]").sendVKey (2)
#     # session.findById("wnd[1]/usr/btnB1").press()
#     # session.findById("wnd[1]").close()
