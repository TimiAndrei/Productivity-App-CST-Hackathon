# import cx_Oracle
import oracledb
import pandas as pd
from user_list import userList, l
from user import user
import getpass

pw = getpass.getpass("Enter database password: ")


def connect():
    conn = oracledb.connect(
        user='TIMI',
        password=pw,
        dsn="localhost/xepdb1")
    cur = conn.cursor()
    return conn, cur


def addTasks(*args):
    conn, cur = connect()
    sqlTxt = 'INSERT INTO Tasks values('
    for item in args:
        sqlTxt += str(item) + ", "

    sqlTxt = sqlTxt.rstrip(", ")
    sqlTxt += ")"

    cur.execute(sqlTxt)
    conn.commit()
    cur.close()
    conn.close()
    records = cur.fetchall()

    df = pd.DataFrame.from_records(
        records, columns=[x[0] for x in cur.description])
    return df


def getTasks():
    conn, cur = connect()
    sqlTxt = 'SELECT * FROM Tasks'
    cur.execute(sqlTxt)
    records = cur.fetchall()
    df = pd.DataFrame.from_records(
        records, columns=[x[0] for x in cur.description])
    cur.close()
    conn.close()
    return df


def addUser(*args):
    conn, cur = connect()
    sqlTxt = 'INSERT INTO Users(username, password, first_name, last_name, clan_tag) values('
    for item in args:
        sqlTxt += "\'" + str(item) + "\'" + ', '

    sqlTxt = sqlTxt.rstrip(', ')
    sqlTxt += ')'
    print(sqlTxt)
    cur.execute(sqlTxt)
    conn.commit()
    l.addUser(args[0], args[1], args[2], args[3], args[4])
    cur.close()
    conn.close()

    # records = cur.fetchall()
    # df = pd.DataFrame.from_records(records, columns = [x[0] for x in cur.description])
    # return df


def getUsers():

    conn, cur = connect()
    sqlTxt = 'SELECT * FROM Users'
    cur.execute(sqlTxt)
    records = cur.fetchall()
    df = pd.DataFrame.from_records(
        records, columns=[x[0] for x in cur.description])
    cur.close()
    conn.close()
    return df


df = getUsers()
for index, row in df.iterrows():
    l.addUser(row['FIRST_NAME'], row['LAST_NAME'],
              row['PASSWORD'], row['CLAN_TAG'], row['USERNAME'])
