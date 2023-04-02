from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('login/',views.my_login, name='login'),
    path('register/',views.register, name='register'),
    path('my-login/',views.my_login, name='my-login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('register/',views.register, name='register'),
    path('addtask/',views.addtask, name='addtask'),
    path('adduser/',views.adduser, name='adduser'),
    path('dashboard/<str:username>/',views.dashboard, name='dashboard'),
]