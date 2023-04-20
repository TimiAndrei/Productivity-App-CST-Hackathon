import cx_Oracle
import pandas as pd
from user_list import userList, l
from user import user

cx_Oracle.init_oracle_client(lib_dir=r"D:/Oracle_libraries/instantclient_21_8")

# conStr = 'ioantudoranghel/ioantudor#16@193.226.51.37:1521/o11g'\
conn = cx_Oracle.connect(user='TIMI', password='BananaBanana', dsn="localhost/xepdb1")
cur = conn.cursor()

def addTasks(*args):
    conn = cx_Oracle.connect(user='TIMI', password='BananaBanana', dsn="localhost/xepdb1")
    cur = conn.cursor()
    sqlTxt = 'INSERT INTO Tasks values('
    for item in args:
        sqlTxt += str(item) + ", "

    sqlTxt = sqlTxt.rstrip(", ")
    sqlTxt += ")"

    cur.execute(sqlTxt)

    conn.commit()

    records = cur.fetchall()

    df = pd.DataFrame.from_records(records, columns = [x[0] for x in cur.description])
    return df

def getTasks():
    conn = cx_Oracle.connect(user='TIMI', password='BananaBanana', dsn="localhost/xepdb1")
    cur = conn.cursor()
    sqlTxt = 'SELECT * FROM Tasks'

    cur.execute(sqlTxt)

    records = cur.fetchall()

    df = pd.DataFrame.from_records(records, columns = [x[0] for x in cur.description])
    return df

def addUser(*args):
    conn = cx_Oracle.connect(user='TIMI', password='BananaBanana', dsn='localhost/xepdb1')
    cur = conn.cursor()
    sqlTxt = 'INSERT INTO Users(username, password, first_name, last_name, clan_tag) values('
    for item in args:
        sqlTxt += "\'" + str(item) + "\'" + ', '

    sqlTxt = sqlTxt.rstrip(', ')
    sqlTxt += ')'
    print(sqlTxt)

    cur.execute(sqlTxt)

    conn.commit()
    l.addUser(args[0], args[1], args[2], args[3], args[4])

    # records = cur.fetchall()
    # df = pd.DataFrame.from_records(records, columns = [x[0] for x in cur.description])
    # return df

def getUsers():
    conn = cx_Oracle.connect(user='TIMI', password='BananaBanana', dsn="localhost/xepdb1")
    cur = conn.cursor()
    sqlTxt = 'SELECT * FROM Users'

    cur.execute(sqlTxt)

    records = cur.fetchall()

    df = pd.DataFrame.from_records(records, columns = [x[0] for x in cur.description])
    return df

df = getUsers()
for index, row in df.iterrows():
    l.addUser(row['FIRST_NAME'], row['LAST_NAME'], row['PASSWORD'], row['CLAN_TAG'], row['USERNAME'])
#con.commit()


# print(getTasks())

cur.close()
conn.close()
