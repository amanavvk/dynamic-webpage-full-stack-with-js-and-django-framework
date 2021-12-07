from pathlib import Path
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("connective_databases",views.connective_databases,name='connective_databases'),
    path("matplotlib",views.matplotlib,name='matplotlib'),
    path("compititions",views.compititions,name='compititions'),
    path("styles",views.styles,name='styles'),
 
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contect",views.contect,name='contect'),
    path("register",views.register,name='register'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('customer/',views.customer,name='customer'),
    path('search',views.search,name='search'),
    path('blog',views.blog,name='blog'),
    path('blogpost',views.blogpost,name='blogpost'),
    path("swimmers_pool",views.swimmers_pool,name='swimmers_pool'),
    path("my_swimming_students",views.my_swimming_students,name='my_swimming_students'),
    path("chartapp",views.chartapp,name='chartapp'),
    path("age",views.age,name='age')
    
   

    





]