import sys
sys.path.append('./Product')
from tasks import task
from user import user
from user_list import userList
from retrieve_data import addUser
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import addUserForm, addTaskForm, loginForm
import cx_Oracle
import pandas as pd
from user_list import l
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def home(request,username):
    return render(request,'home.html',{'username':username})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    # form=addUserForm()
    if request.method == 'POST':
        form=addUserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            clan_tag = form.cleaned_data.get("clan_tag")
            messages.success(request, f'Account created for {username}!')
            addUser(first_name,last_name,username,password,clan_tag)
            #return redirect('my-login')
        else:
            messages.error(request, 'Fill out the form !')
            return redirect('register')
        return redirect('my-login')

def my_login(request):
    if request.method == 'GET':
        return render(request, 'my-login.html')
    if request.method == 'POST':
        form=loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            for person in l.users:
                if username == person.username and password == person.password:
                    messages.success(request, f'Welcome {username}!')
                    return redirect('home', username = request.POST.get('username'))
            messages.error(request, 'Username or password is incorrect !')
            return redirect('my-login')
        else :
            messages.error(request, 'Fill out the form !')
            return redirect('my-login')


def dashboard(request,username=None):
    if username is None:
        return redirect('my-login')
    else:
        person=l.getUserFromUsername(username)
        clan=l.getClan(person.clan_tag)
        top=l.getUserBracket(username)
        badges=person.badges
        impr_badges=badges["Improvements"]
        new_tech_badges=badges["New Technology"]
        tasks = person.task_list
        return render(request,'dashboard.html',{'person':person, 'clans':clan, 'top':top, 'improve':impr_badges, 'newtech':new_tech_badges, 'tasks':tasks, 'username':username})


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
    
    return redirect('listusers')

def addtask(request, username=None):
    if username is None:
        return redirect('my-login')
    if request.method == 'GET':
        return render(request, 'addtask.html', {'task':{}, 'username':username})
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
            return redirect('dashboard', username = username)
        else:
            messages.error(request, 'The form is not valid, fill the form correctly !')
            return redirect('addtask', username = username)
            #addTasks(title, description, difficulty, deadline, duration, task_type, username)


