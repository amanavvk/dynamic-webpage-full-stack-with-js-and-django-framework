

#from _typeshed import Self
from os import name, renames
from pathlib import Path
from django import forms
from django.db.models import query
from django.forms.forms import Form
from django.http import request

from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from home.models import AccessRecord, Age, Chartapp, Compititions, Contect,Customer, Matplotlib, My_swimming_students, Sports, Style, Swimmers_pool
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UsernameField

from home.utils import get_plot
from home.utilsconnector import plot
from .forms import Createuserform
from django.contrib.auth import authenticate , login , logout
from home.models import Strokes,Post,Age
import pandas as pd
from . import forms


def contect(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contect=Contect(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contect.save()
        messages.success(request, 'your massage has been sent!')
   


    return render(request,"contect.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,'services.html')
    
    
def index(request):
    strokes=Strokes.objects.all()

   

    
    
    messages.success(request,'The man who is swimming against the stream knows the strength of it')
    
    return render(request,"index.html",{'stroke':strokes})

def register(request):
    form=Createuserform()

    if request.method =='POST':
        form=Createuserform(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')

            messages.success(request,'account was created for ' +user )
            return redirect('login')


    context={'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect')

    return render(request,'login.html')


def logoutuser(request):
    logout(request)

    return redirect('login')





def customer(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        customer=Customer(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        customer.save()
        messages.success(request, 'your massage has been sent!')
    
    return render(request,'customer.html')


def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()

    #allPosts=Post.objects.all()
    else:
        allPostsTitle=Post.objects.filter(title__icontains=query)
        allPostsAdd=Post.objects.filter(content__icontains=query)
        allPostsslug=Post.objects.filter(slug__icontains=query)
        allPosts=allPostsTitle.union(allPostsAdd,allPostsslug)
       
    if allPosts.count() == 0:
        messages.error(request,"No search result found by mr. aman vyas.please refine your query")
    params={'allPosts': allPosts,'query':query}

    return render(request,'search.html',params)


def blog(request):
    allposts=Post.objects.all()
    print(allposts)
    context={'allposts':allposts}

    return render(request,'blog.html',context)

def blogpost(request):
    return render(request,'blogpost.html')



    
def swimmers_pool(request):
    swimmer_info=Swimmers_pool.objects.all()
    print(swimmer_info)
    context={'swimmer_info': swimmer_info}
    return render (request,'swimmers_pool.html',context)


def my_swimming_students(request):
    student_info=My_swimming_students.objects.all()
    print(student_info)
    context={'student_info':student_info}
    return render(request,'my_swimming_students.html',context)



def chartapp(request):
    chartapp_info=Chartapp.objects.all()
    print(chartapp_info)
    context={"chartapp_info":chartapp_info}

    return render(request,'chartapp.html',context)

def age(request):

    lables=[]
    data=[]

    
    age_info=Age.objects.all()
    
    
    
    context={'age_info':age_info}

    return render(request,'age.html',context)


def connective_databases(request):
    student_info=My_swimming_students.objects.all()
    swimmer_info=Swimmers_pool.objects.all()
    params={'student_info':student_info,'swimmer_info':swimmer_info}



    return render(request,'connective_databases.html',params)

def matplotlib(request):
    
    qs=Matplotlib.objects.all()
    s=Matplotlib.objects.all().values()
    #for s in Matplotlib.objects.raw('select * from home_matplotlib'):
        #print(s)
    data=pd.DataFrame(s)
    print(data)
    qs2=Matplotlib.objects.all().values_list()
    print(s)
    print("aman")
    print(qs2)
    swimmer_info=Swimmers_pool.objects.all().values()
    student_info=My_swimming_students.objects.all().values()
    
    data2=pd.DataFrame(swimmer_info)
    data3=pd.DataFrame(student_info)
    x=[x.item_name for x in qs]
    y=[y.price for y in qs]
    #a=[a.Swiimmingpool_name for a in swimmer_info]
    #b=[b.student_name for b in student_info]
    chart=get_plot(x,y)
    return render(request,'matplotlib.html',{'chart':chart,'df' : data.to_html,'discribe':data.describe().to_html(),'swimmer_info':data2.to_html(),'student_info':data3.to_html()})

def compititions(request):
    comp_name=Compititions.objects.all().values()
    data4=pd.DataFrame(comp_name)
    print(data4)

    return render(request,'compititions.html',{'comp_name':data4.to_html()})


def styles(request):
    webpage_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpage_list}
    qs=Style.objects.all()
    qs2=Sports.objects.all()

    ab=[a.sports_name_id for a in qs]
    data5=pd.DataFrame(qs)
    
    c=[c.sports_name_id for c in qs]
    #c=[a.]
    #c=a.name
    b=[b.name for b in qs]
    chart1=plot(c,b)
    return render(request,'styles.html',{'chart' : chart1,'qs':data5.to_html(),'date_dict' : date_dict})

def form_name_view(request):
    form=forms.Formname()

    if request.method =='POST':
        form=forms.Formname(request.POST)

        if form.is_valid():
            print("validation success!")
            print("name: " +form.cleaned_data['name'])
            print("email: " +form.cleaned_data['email'])
            print("text: " +form.cleaned_data['text'])


    return render(request,'forms.html',{'form' : form})