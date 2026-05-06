import pandas as pd
import pyodbc

df = pd.read_excel(r'D:\PRACTICE_FOLDER\EXCEL\Superstore.xlsx')

df.columns = df.columns.str.replace(' ', '_').str.replace('-', '_')

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=LAPTOP-AVNISHA\\SQLEXPRESS01;'
    'DATABASE=Superstore DB;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute('''
        INSERT INTO Superstore VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''',
    int(row.Row_ID),
    str(row.Order_ID),
    str(row.Order_Date),
    str(row.Ship_Date),
    str(row.Ship_Mode),
    str(row.Customer_ID),
    str(row.Customer_Name),
    str(row.Segment),
    str(row.Country),
    str(row.City),
    str(row.State),
    str(row.Postal_Code),
    str(row.Region),
    str(row.Product_ID),
    str(row.Category),
    str(row.Sub_Category),
    str(row.Product_Name),
    float(row.Sales),
    int(row.Quantity),
    float(row.Discount),
    float(row.Profit)
    )

conn.commit()
conn.close()
print("Done! All rows inserted successfully.")