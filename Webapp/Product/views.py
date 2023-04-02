import sys
sys.path.append('./Product')
from tasks import task
from user import user
from user_list import userList
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import addUserForm, addTaskForm
import cx_Oracle
import pandas as pd
from user_list import l

# from user import user

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def my_login(request):
    return render(request,'my-login.html')

def dashboard(request,username):
    person=l.getUserFromUsername(username)
    clan=l.getClan(person.clan_tag)
    top=l.getUserBracket(username)
    badges=person.badges
    return render(request,'dashboard.html',{'person':person, 'clans':clan, 'top':top, 'badges':badges})


def adduser(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'user':{}})
    if(request.method == 'POST'):
        form = addUserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            clan_tag = form.cleaned_data['clan_tag']
            new_user = user(first_name, last_name, username, password, clan_tag)
            # addUsers(username, password)
    
    return redirect('listusers')

def addtask(request):
    if request.method == 'GET':
        return render(request, 'addtask.html', {'task':{}})
    if(request.method == 'POST'):
        form = addTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            difficulty = form.cleaned_data['difficulty']
            deadline = form.cleaned_data['deadline']
            visibility = form.cleaned_data['visibility']
            task_type = form.cleaned_data['task_type']
            username = form.cleaned_data['username']
            new_task = task(title, description, visibility, difficulty, deadline, task_type)

            for person in userList.users:
                if person.username == username:
                    person.addTask(new_task)
            # addTasks(title, description, difficulty, deadline, duration, task_type, username)
    
    return redirect('listtasks')


