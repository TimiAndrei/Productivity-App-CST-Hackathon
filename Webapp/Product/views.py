from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateUserForm
import cx_Oracle
import pandas as pd

cx_Oracle.init_oracle_client(lib_dir=r"D:/Oracle_libraries/instantclient_21_8")

def connection():
    conn = cx_Oracle.connect(user='TIMI', password='BananaBanana', dsn="localhost/xepdb1")
    return conn


def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def my_login(request):
    return render(request,'my-login.html')

def dashboard(request):
    return render(request,'dashboard.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User registered successfully!')
    context = {'form':form}
    return render(request,'register.html',context=context) 

def addTasks(*args):
    sqlTxt = 'INSERT INTO Tasks values('
    for item in args:
        sqlTxt += str(item) + ", "
    sqlTxt += ")"

    cur.execute(sqlTxt)

    records = cur.fetchall()

    df = pd.DataFrame.from_records(records, columns = [x[0] for x in cur.description])
    return df


def listtasks(request):
    conn=connection()
    cursor = conn.cursor()
    sqlTxt = 'SELECT * FROM Tasks'
    tasks=[]
    cursor.execute(sqlTxt)
    for row in cursor.fetchall():
        tasks.append({"title": row[0], "description": row[1], "difficulty": row[2], "deadline": row[3], "duration": row[4], "task_type": row[5], "username": row[6]})
    conn.close()
    return render(request, 'listtasks.html', {'tasks': tasks})

def addUser(*args):
    sqlTxt = 'INSERT INTO Users values('
    for item in args:
        sqlTxt += str(item) + ", "
    sqlTxt += ")"

    cur.execute(sqlTxt)

    records = cur.fetchall()

    df = pd.DataFrame.from_records(records, columns = [x[0] for x in cur.description])
    return df

def getUsers():
    sqlTxt = 'SELECT * FROM Users'

    cur.execute(sqlTxt)

    records = cur.fetchall()

    df = pd.DataFrame.from_records(records, columns = [x[0] for x in cur.description])
    return df



