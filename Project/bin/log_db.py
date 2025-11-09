import os
import pandas as pd
import sqlite3
from tkinter import Tk, filedialog, messagebox

#find select file
root = Tk()
root.withdraw()  

file_path = filedialog.askopenfilename(title='Select Excel file', filetypes=[('Excel Files', '*.xlsx *.xls')])
if not file_path:
    messagebox.showinfo('Info', 'No file selected. Exiting.')
    exit()

#-------------------

df = pd.read_excel(file_path)
df.columns = df.columns.str.strip()

text_cols = ['Account No.', 'Account Name Rekening Naam', 'Cell Number']
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()
df = df.replace('N/A', None)
df = df.replace(r'^\s*$', None, regex=True)

#Create DB will replace previous db file be careful

db_file = 'log_db.db'
if os.path.exists(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

#Create table
cursor.execute('''
CREATE TABLE accounts (
    account_no TEXT,
    account_name TEXT,
    cell_number TEXT,
    total TEXT,
    unallocated TEXT,
    current TEXT,
    days_30 TEXT,
    days_60 TEXT,
    days_90 TEXT,
    days_120 TEXT,
    days_150 TEXT,
    days_180 TEXT,
    days_210 TEXT,
    days_250_plus TEXT
)
''')
conn.commit()

df = df.rename(columns={
    'Account No.': 'account_no',
    'Account Name Rekening Naam': 'account_name',
    'Cell Number': 'cell_number',
    'Total Totale': 'total',
    'Unallocated Ongeallokeer': 'unallocated',
    'Current Huidig': 'current',
    '30 Days 30 Dae': 'days_30',
    '60 Days 60 Dae': 'days_60',
    '90 Days 90 Dae': 'days_90',
    '120 Days 120 Dae': 'days_120',
    '150 Days 150 Dae': 'days_150',
    '180 Days 180 Dae': 'days_180',
    '210 Days 210 Dae': 'days_210',
    '250+ Days 250+ Dae': 'days_250_plus'
})


df.to_sql('accounts', conn, if_exists='replace', index=False)
conn.close()

messagebox.showinfo('Success')
