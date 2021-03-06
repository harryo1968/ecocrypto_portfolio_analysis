import base64
import pandas as pd
from IPython.display import HTML

def download_link(df, title = "Download CSV file"):
    """
    Creates a download link from a dataframe!  :)
    Returns: html encoded link
    """
    filename = "data.csv"
    csv = df.to_csv()
    b64 = base64.b64encode(csv.encode())
    payload = b64.decode()
    html = '<a download="{filename}" href="data:text/csv;base64,{payload}" target="_blank">{title}</a>'
    html = html.format(payload=payload,title=title,filename=filename)

    return HTML(html)
