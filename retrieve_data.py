import cx_Oracle
import pandas as pd

cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\xelar\Downloads\instantclient-basic-windows.x64-21.8.0.0.0dbru\instantclient_21_8")

# conStr = 'ioantudoranghel/ioantudor#16@193.226.51.37:1521/o11g'\
conStr = 'system/parola@localhost:1522/xe'

conn = cx_Oracle.connect(conStr)
cur = conn.cursor()

def addTasks(*args):
    sqlTxt = 'INSERT INTO Tasks values('
    for item in args:
        sqlTxt += str(item) + ", "

    sqlTxt = sqlTxt.rstrip(",")
    sqlTxt += ")"

    cur.execute(sqlTxt)

    conn.commit()

    records = cur.fetchall()

    df = pd.DataFrame.from_records(records, columns = [x[0] for x in cur.description])
    return df

def getTasks():
    sqlTxt = 'SELECT * FROM Tasks'

    cur.execute(sqlTxt)

    records = cur.fetchall()

    df = pd.DataFrame.from_records(records, columns = [x[0] for x in cur.description])
    return df

def addUser(*args):
    sqlTxt = 'INSERT INTO Users values('
    for item in args:
        sqlTxt += str(item) + ", "

    sqlTxt = sqlTxt.rstrip(",")
    sqlTxt += ")"

    cur.execute(sqlTxt)

    conn.commit()

    records = cur.fetchall()

    df = pd.DataFrame.from_records(records, columns = [x[0] for x in cur.description])
    return df

def getUsers():
    sqlTxt = 'SELECT * FROM Users'

    cur.execute(sqlTxt)

    records = cur.fetchall()

    df = pd.DataFrame.from_records(records, columns = [x[0] for x in cur.description])
    return df

#con.commit()

print(getTasks())

cur.close()
conn.close()
