# import os, sys
# x=os.path.dirname(sys.executable)
# print(x)
import pandas as pd

# Load HTML file
dps = "dpcur.html"
df = pd.read_html(dps, header=0)[0]  # Read HTML into DataFrame

# Clean column names by replacing non-breaking spaces and stripping whitespace
df.columns = df.columns.str.replace('\xa0', ' ', regex=False).str.strip()
print(df.columns)