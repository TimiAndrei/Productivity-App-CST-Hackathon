from django.forms import ModelForm
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class addTaskForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    difficulty = forms.IntegerField()
    deadline = forms.DateField()
    visibility= forms.CharField(max_length=100)
    task_type = forms.CharField(max_length=100)
    username= forms.CharField(max_length=100)
    
