from django.forms import ModelForm
from django import forms

class addTaskForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    difficulty = forms.IntegerField()
    deadline = forms.DateField()
    visibility= forms.CharField(max_length=100)
    task_type = forms.CharField(max_length=100)
    username= forms.CharField(max_length=100)

class addUserForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    clan_tag= forms.CharField(max_length=100)

class loginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    
