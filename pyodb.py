import pyodbc
SERVER = '103.7.40.78'
DATABASE = 'PlcReadDataBase'
USERNAME = 'sa'
PASSWORD = 'Tuan2193'
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes'
conn = pyodbc.connect(connectionString)
SQL_QUERY = """
SELECT TOP 10* FROM dbo.SaveData
"""
cursor = conn.cursor()
cursor.execute(SQL_QUERY)
records = cursor.fetchall()
for r in records:
    print(f"{r.ID}\t\t\t\t\t\t{r.DataValue}\t\t\t{r.TimeData}")
