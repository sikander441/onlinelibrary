
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import *
from django.db import connection
# Create your views here.
def type(request):
    tech=Search.objects.filter(Type__contains='tech')
    non=Search.objects.filter(Type__contains='non')
    techlist=[]
    nonlist=[]
    for i in tech:
        techlist+=i.Type
    for i in non:
        nonlist+=i.Type
    labels=['Technical','Non-Technical']
    values=[len(tech),len(non)]
    import plotly as py
    import plotly.graph_objs as go
    trace = go.Bar(x=labels, y=values)
    py.offline.plot([trace], filename='basic_pie_chart.html')

    return render(request,'library/analysis.html')


def search(request):
    key=request.POST.get('key')
    tech_books=Books_technical.objects.filter(Book_name__contains=key)
    non_tech_books=Books_non_technical.objects.filter(Book_name__contains=key)
    #User_name=Curr_user.objects.get_user_name()
    context={'tech_books':tech_books,'non_tech_books':non_tech_books}
    template=loader.get_template('library/search.html')
    return HttpResponse(template.render(context,request))
def index(request):
    return render(request,'library/homepage.html')

def signup(request):
    return render(request,'library/form.html')


def add_book_tech(request):
    return render(request,'library/add_book_tech.html')


def add_book_non_tech(request):
    return render(request,'library/add_book_non_tech.html')


def delete_book_tech(request):
    User_name=Curr_user.objects.get_user_name()
    all_books=Book_record.objects.get_books(User_name,'tech')
    context={'all_books':all_books}
    template=loader.get_template('library/delete_tech.html')
    return HttpResponse(template.render(context,request))

def tech_search(request,Book_id):
    import datetime
    now = datetime.datetime.now()
    book=Books_technical.objects.get(pk=Book_id)
    user=Curr_user.objects.get_user_name()

    Search.objects.add(book.Book_name,book.Department,"tech",user)
    cursor=connection.cursor();
    cursor.execute("""
            UPDATE library_searcH SET date_of_search=%s where  date_of_search is NULL;
            """,[now])
    all_books=Book_record.objects.filter(Book_name=book.Book_name)
    template=loader.get_template('library/tech_book_details.html')
    context={'book':book,'all_books':all_books}
    return HttpResponse(template.render(context,request))

def non_tech_search(request,Book_id):
    import datetime
    now = datetime.datetime.now()
    book=Books_non_technical.objects.get(pk=Book_id)
    user=Curr_user.objects.get_user_name()

    Search.objects.add(book.Book_name,book.Department,"non",user)
    cursor=connection.cursor();

    cursor.execute("""
            UPDATE library_searcH SET date_of_search=%s where  date_of_search is NULL;
            """,[now])
    all_books=Book_record.objects.filter(Book_name=book.Book_name)
    template=loader.get_template('library/tech_book_details.html')
    context={'book':book,'all_books':all_books}
    return HttpResponse(template.render(context,request))


def delete_book_non_tech(request):
    User_name=Curr_user.objects.get_user_name()
    all_books=Book_record.objects.get_books(User_name,'non')
    context={'all_books':all_books}
    template=loader.get_template('library/delete_non_tech.html')
    return HttpResponse(template.render(context,request))

def delete_tech(request):
     book=request.POST.get('book')
     User_name=Curr_user.objects.get_user_name()
     Book_record.objects.delete(User_name,book)
     Books_technical.objects.update_no_of_books(book)
     user_n=User.objects.get_name(User_name)
     phone=User.objects.get_phone(User_name)
     email=User.objects.get_email(User_name)
     template=loader.get_template('library/profile.html')
     a='tech'
     b='non'
     tech_books=Book_record.objects.get_books(User_name,a)
     non_tech_books=Book_record.objects.get_books(User_name,b)

     context={'name':user_n,'phone':phone,'email':email,'tech_books':tech_books,'non_tech_books':non_tech_books}
     return HttpResponse(template.render(context,request))

def delete_non_tech(request):
     book=request.POST.get('book')
     User_name=Curr_user.objects.get_user_name()
     Book_record.objects.delete(User_name,book)
     Books_non_technical.objects.update_no_of_books(book)
     user_n=User.objects.get_name(User_name)
     phone=User.objects.get_phone(User_name)
     email=User.objects.get_email(User_name)
     template=loader.get_template('library/profile.html')
     a='tech'
     b='non'
     tech_books=Book_record.objects.get_books(User_name,a)
     non_tech_books=Book_record.objects.get_books(User_name,b)

     context={'name':user_n,'phone':phone,'email':email,'tech_books':tech_books,'non_tech_books':non_tech_books}
     return HttpResponse(template.render(context,request))


def add_tech(request):
    name=request.POST.get('name')
    department=request.POST.get('Department')
    subject=request.POST.get('subject')
    author=request.POST.get('author')
    Books_technical.objects.add(name,department,subject,author)
    User_name=Curr_user.objects.get_user_name()
    user_n=User.objects.get_name(User_name)
    phone=User.objects.get_phone(User_name)
    email=User.objects.get_email(User_name)
    template=loader.get_template('library/profile.html')
    a='tech'
    b='non'
    tech_books=Book_record.objects.get_books(User_name,a)
    non_tech_books=Book_record.objects.get_books(User_name,b)

    context={'name':user_n,'phone':phone,'email':email,'tech_books':tech_books,'non_tech_books':non_tech_books}
    return HttpResponse(template.render(context,request))


def add_non_tech(request):
    name=request.POST.get('name')
    department=request.POST.get('Department')
    subject=request.POST.get('subject')
    author=request.POST.get('author')
    Books_non_technical.objects.add(name,department,subject,author)
    User_name=Curr_user.objects.get_user_name()
    user_n=User.objects.get_name(User_name)
    phone=User.objects.get_phone(User_name)
    email=User.objects.get_email(User_name)
    template=loader.get_template('library/profile.html')
    a='tech'
    b='non'
    tech_books=Book_record.objects.get_books(User_name,a)
    non_tech_books=Book_record.objects.get_books(User_name,b)

    context={'name':user_n,'phone':phone,'email':email,'tech_books':tech_books,'non_tech_books':non_tech_books}
    return HttpResponse(template.render(context,request))


def add_user(request):
    name=request.POST.get('name')
    user_n=request.POST.get('user_name')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    password=request.POST.get('password')
    User.objects.add_user1(name,user_n,email,phone,password)
    return render(request,'library/success.html')


def profile(request):
    User_name=Curr_user.objects.get_user_name()
    user_n=User.objects.get_name(User_name)
    phone=User.objects.get_phone(User_name)
    email=User.objects.get_email(User_name)
    template=loader.get_template('library/profile.html')
    a='tech'
    b='non'
    tech_books=Book_record.objects.get_books(User_name,a)
    non_tech_books=Book_record.objects.get_books(User_name,b)

    context={'name':user_n,'phone':phone,'email':email,'tech_books':tech_books,'non_tech_books':non_tech_books}
    return HttpResponse(template.render(context,request))

def login(request):
    return render(request,'library/login.html')

def login_new(request):
    user_n=request.POST.get('user_name')
    password=request.POST.get('password')
    a=User.objects.check_user(user_n,password)

    if(a== -1):
        return render(request,'library/logout.html')
    if(a==1):
        b=User.objects.get_name(user_n)
        context={'name':b}
        template=loader.get_template('library/mainpage.html')
        return HttpResponse(template.render(context,request))
    else :
        return render(request,'library/login.html')

def mainpage(request):
    return render(request,'library/mainpage.html')

def logout(request):
    User.objects.logout()
    return render(request,'library/homepage.html')

def tech(request):
    return render(request,'library/tech.html')
def non_tech(request):
    return render(request,'library/non_tech.html')
def mech(request):
    all_books=Books_technical.objects.filter(Department='mechanical')
    template=loader.get_template('library/mech.html')
    context={'all_books':all_books}
    return HttpResponse(template.render(context,request))
def comp(request):
    all_books=Books_technical.objects.filter(Department='computer')
    template=loader.get_template('library/comp.html')
    context={'all_books':all_books}
    return HttpResponse(template.render(context,request))
def entc(request):
    all_books=Books_technical.objects.filter(Department='electronics')
    template=loader.get_template('library/entc.html')
    context={'all_books':all_books}
    return HttpResponse(template.render(context,request))
def tech_book_details(request,Book_id):
    book=Books_technical.objects.get(pk=Book_id)
    all_books=Book_record.objects.filter(Book_name=book.Book_name)
    template=loader.get_template('library/tech_book_details.html')
    context={'book':book,'all_books':all_books}
    return HttpResponse(template.render(context,request))
def non_tech_book_details(request,Book_id):
    book=Books_non_technical.objects.get(pk=Book_id)
    all_books=Book_record.objects.filter(Book_name=book.Book_name)
    template=loader.get_template('library/tech_book_details.html')
    context={'book':book,'all_books':all_books}
    return HttpResponse(template.render(context,request))
def fiction(request):
    all_books=Books_non_technical.objects.filter(Department='fiction')
    template=loader.get_template('library/fiction.html')
    context={'all_books':all_books}
    return HttpResponse(template.render(context,request))
def non_fiction(request):
    all_books=Books_non_technical.objects.filter(Department='non fiction')
    template=loader.get_template('library/non_fiction.html')
    context={'all_books':all_books}
    return HttpResponse(template.render(context,request))
def magazines(request):
    all_books=Books_non_technical.objects.filter(Department='magazines')
    template=loader.get_template('library/magazines.html')
    context={'all_books':all_books}
    return HttpResponse(template.render(context,request))
def user_details(request,User_name):
    user_n=User.objects.get_name(User_name)
    phone=User.objects.get_phone(User_name)
    email=User.objects.get_email(User_name)
    template=loader.get_template('library/user.html')
    context={'name':user_n,'phone':phone,'email':email}
    return HttpResponse(template.render(context,request))

def analysis(request):
    graph()
    import plotly as py
    import plotly.graph_objs as go

    total=Search.objects.all()
    total=len(total)
    tech=Search.objects.filter(Type='tech')
    tech=len(tech)
    non=Search.objects.filter(Type='non')
    non=len(non)
    mech=Search.objects.filter(Department='mechanical')
    mech=len(mech)
    comp=Search.objects.filter(Department='computer')
    comp=len(comp)
    entc=Search.objects.filter(Department='electronics')
    entc=len(entc)
    fiction=Search.objects.filter(Department='fiction')
    fiction=len(fiction)
    non_fiction=Search.objects.filter(Department='non fiction')
    non_fiction=len(non_fiction)
    Maga=Search.objects.filter(Department='magazines')
    Maga=len(Maga)

    context={'total':total,'tech':tech,'non':non,'mech':mech,'comp':comp,'entc':entc,'fiction':fiction,'non_fiction':non_fiction,'Maga':Maga}
    template=loader.get_template('library/analysis.html')

    labels = ['Technical','Non Technical']
    values = [tech,non]
    trace = go.Pie(labels=labels, values=values, hoverinfo='label+percent')
    py.offline.plot([trace], filename='pie_chart_1')
    labels = ['Mechanical','Computer','Electronics','Fiction','Non Fiction','Magazines']
    values = [mech,comp,entc,fiction,non_fiction,Maga]
    trace = go.Bar(x=labels, y=values)
    py.offline.plot([trace], filename='pie_chart_2')
    cursor=connection.cursor()
    cursor.execute("""SELECT Book_name, COUNT(*) c FROM library_search GROUP BY Book_name HAVING c > 1;""")
    j=0
    x=[]
    y=[]
    for i in cursor.fetchall():
       x.append(i[0])
       y.append(i[1])
       if j==4:
            break
       j+=1

    layout = go.Layout(
        xaxis=dict(
           title="BOOK NAME"
        ),
        yaxis=dict(
           title="No. of searches"
        )
    )
    data = [go.Scatter( x=x,y=y)]
    fig = go.Figure(data=data, layout=layout)

    py.offline.plot(fig)

    return HttpResponse(template.render(context,request))
def graph():
    import datetime
    from datetime import timedelta, date
    import pymysql.cursors
    import pandas as pd
    import sys
    import random
    import plotly as py
    import plotly.graph_objs as go
    sys.__stdout__ = sys.stdout
    cursor=connection.cursor()
    cursor.execute("""SELECT Book_name, COUNT(*) c FROM library_search GROUP BY Book_name HAVING c > 1 order by c DESC;""")
    j=0
    x=[]
    y=[]
    for i in cursor.fetchall():
       x.append(i[0])
       y.append(i[1])
       if j==2:
            break
       j+=1

    start_date = date(2017,9,13)
    end_date = date(2017,10,3)
    d = start_date
    delta = datetime.timedelta(days=1)
    z=[]
    ew=[]
    while d <= end_date:
        d += delta
        cursor.execute("""select count(*) c from library_search where Book_name=%s and date_of_search=%s;""",[x[1],d])
        z.append(cursor.fetchone()[0])
        ew.append(d.strftime("%Y-%m-%d"))
    layout = go.Layout(
            xaxis=dict(
               title="LAST 2 WEEKS DATA"
            ),
            yaxis=dict(
               title="No. of searches"
            )
        )
    trace =go.Scatter(y=z,x=ew,name=x[1])
    dsa=[]
    wq=[]
    d = start_date
    while d <= end_date:
        d += delta
        cursor.execute("""select count(*) c from library_search where Book_name=%s and date_of_search=%s;""",[x[0],d])
        dsa.append(cursor.fetchone()[0])
        wq.append(d.strftime("%Y-%m-%d"))
    print(z)
    print(dsa)
    trace1 =go.Scatter(y=dsa,x=wq,name=x[0])
    data=[trace,trace1]
    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig)
