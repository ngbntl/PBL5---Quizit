import pymssql

MSSQL_SERVER = '172.31.48.1'
MSSQL_DATABASE = "trac_nghiem"
MSSQL_USER = "sa"
MSSQL_PASSWORD = "pbl5"
MSSQL_PORT = "1433"

mssql_connection = pymssql.connect(server=MSSQL_SERVER, user=MSSQL_USER, password=MSSQL_PASSWORD, database=MSSQL_DATABASE, port=MSSQL_PORT, as_dict=True)

cursor = mssql_connection.cursor()
cursor.execute("SELECT * FROM student")
students = cursor.fetchall()
cursor.close()
mssql_connection.close()
for student in students:
    print(students)
