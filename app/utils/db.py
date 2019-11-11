import pymssql
import _mssql

def getCursor():
    cnn = pymssql.connect(
        host=r'ACER-E5\MSSQLSERVER',
        user=r'sa',
        password=r'1234',
        database=r'Contact'
    )
    return cnn