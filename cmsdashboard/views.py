from venv import create
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponse
from .models import *
from .form import CsvModelForm, addEmpform, changeStatus
import csv
import datetime
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from .filters import empfilter

# Create your views here.
@login_required(login_url='/dashboard/dashboardlogin')
# emp_obj = emp.objects.all().order_by('id')
def dashboardhome(request):
    datelist = []
    if request.method == "POST":
        day = str(request.POST['day'])
        print(day)
        # month = int(request.POST['month'])
        # year = int(request.POST['year'])
        # y = 2022
        # m = 9
        # d = 11
        # presentday = datetime.datetime(year, month, day) 
        entered_date = datetime.datetime.strptime(day, '%m/%d/%Y')
        presentday = entered_date.date()
        # presentday = entered_date - datetime.timedelta(days=datetime.datetime.today().weekday() % 7)

        date =presentday.strftime('%m/%d/%Y')
        datelist.append(date) 
        for x in range(1,7):
            tomorrow = presentday + timedelta(x)
            date =tomorrow.strftime('%m/%d/%Y')
            datelist.append(date) 
    else:
# when have current date
        currentdate = datetime.datetime.today()
        presentday = datetime.datetime.today() - datetime.timedelta(days=datetime.datetime.today().weekday() % 7)
        # presentday = datetime.datetime.today()
        date =presentday.strftime('%m/%d/%Y')
        datelist.append(date) 

        for x in range(1,7):
            tomorrow = presentday + timedelta(x)
            date =tomorrow.strftime('%m/%d/%Y')
            datelist.append(date) 

    monday = datelist[0]
    tuesday = datelist[1]
    wednessday = datelist[2]
    thruday = datelist[3]
    friday = datelist[4]
    saturday = datelist[5]
    sunday = datelist[6]

    Sdate= datetime.datetime.strptime(monday, '%m/%d/%Y')
    ldate= datetime.datetime.strptime(sunday, '%m/%d/%Y')
    # record_del()
    # record_add()
    obj = emp_status.objects.filter(Date__gte=Sdate,Date__lte=ldate)
    # obj = emp_status.objects.filter(Date__range=[Sdate, enddate])
    # if request.method == "POST":
    #     query = request.POST.get('query')
    #     print("query :", query)
    #     emp_obj = emp.objects.filter(emp_name__icontains=query)
    # else:
    emp_obj = emp.objects.all().order_by('id')

    myfilter = empfilter( request.GET, queryset=emp_obj)
    emp_obj = myfilter.qs

    # myfilter2 = emp_statusfilter( request.GET, queryset=obj)
    # obj = myfilter2.qs

    return render(request, 'cmsdashboard/dashbordHome.html',
    {
        'datelist':datelist,
        'obj':obj, 
        'emp_obj': emp_obj,
        'monday':monday,
        'tuesday':tuesday,
        'wednessday':wednessday,
        'thruday':thruday,
        'friday':friday,
        'saturday':saturday,
        'sunday':sunday,
        'myfilter':myfilter,
        # 'myfilter2':myfilter2,
    }
    )


def dashboardlogin(request):
    if request.method == "POST":
        username = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        user = User.objects.filter(username = username).first()
        try:
            if user is None:
                 messages.error(request, 'User not found.')
                 return redirect('/dashboard/dashboardlogin')
            loguser = authenticate(username = username, password = pass1)
            if loguser is None:
                messages.error(request, 'Wrong password.')
                return redirect('/dashboard/dashboardlogin')

            login(request , loguser)
            return redirect('/dashboard')

        except Exception as e:
            print(e)
    return render(request, 'cmsdashboard/dashboardlogin.html')

@login_required(login_url='/dashboard/dashboardlogin')
def dashboardlogout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/dashboard/dashboardlogin')
def dashboardfileupload(request):
    form =  CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row = " ".join(row)
                    row = row.split()
                    # print(row) 
                    # print(type(row)) 
                    
                    empobj = emp.objects.get(emp_name=row[0])
                    statuobj= emp_statustype.objects.get(status=row[1])
                    date = row[2]
                    emp_status.objects.create(
                         emp = empobj,
                         status = statuobj,
                         Date = date,
                    )


            obj.activated=True
            obj.save()
    return render(request, 'cmsdashboard/dashboardfileupload.html',
    {
        'form':form,
    })

@login_required(login_url='/dashboard/dashboardlogin')
def dashboardaddemp(request):
    form =  addEmpform(request.POST)
    if request.method == "POST":
        if form.is_valid():
            empname = form.cleaned_data['emp_name']
            form.save()
            # present week day monday
            presentday = datetime.datetime.today() - datetime.timedelta(days=datetime.datetime.today().weekday() % 7)
            # print("Emp name : ", empname)
            # print("present weekday monday date : ", presentday)
            emp_obj = emp.objects.filter(emp_name=empname).first()
            objstatus = emp_status.objects.filter(emp=emp_obj).first()
            # print("obj : ", emp_obj)
            # print("obj : ", objstatus)
            objlast = record_created.objects.latest('Date')
            # print("objlast : ", objlast.Date)
            ldate =objlast.Date
            ldate = ldate+ datetime.timedelta(days=1)
            date1 = ldate.strftime('%m/%d/%Y')
            # print("ldate : ", ldate)
            # olddate = ldate+ datetime.timedelta(days=0)
            
            # lastDate = presentday+ datetime.timedelta(days=111)
            # print("lastDate : ", lastDate)
            # print("olddate : ", olddate)
            # date1 = olddate.strftime('%m/%d/%Y')
            # date2 = lastDate.strftime('%m/%d/%Y')
            
            # print("date1 : ", date1)
            # print("date2 : ", date2)
            # print("date1 : ", date1)
            # print("New date was: ", NewDate)
            statuobj= emp_statustype.objects.get(status='Available')
            statuobjweekend= emp_statustype.objects.get(status='weekend')
            count=0
            x=0
            if objstatus is None:
                while(count == 0):
                    NewDate=presentday + datetime.timedelta(days=x)
                    date2 = NewDate.strftime('%m/%d/%Y')
                    # print("NewDate : ", NewDate)
                    # print("date4 : ", date2)
                    weekdayno = NewDate.weekday()
                    if date1 == date2:
                            count = 1
                    else:
                        x=x+1
                        if weekdayno < 5:
                            emp_status.objects.create(
                                emp=emp_obj,
                                Date=NewDate,
                                status=statuobj
                                )
                        else:
                            emp_status.objects.create(
                                emp=emp_obj,
                                Date=NewDate,
                                status=statuobjweekend
                                )
            form =  addEmpform
            return redirect('/dashboard')

    return render(request, 'cmsdashboard/dashboardaddemp.html',
    {
        'form':form,
    })

@login_required(login_url='/dashboard/dashboardlogin')
def dashboardeditEmp(request, empid):
    empobj = emp.objects.get(pk=empid)
    form = addEmpform(request.POST or None, instance=empobj)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form =  addEmpform
            return redirect('/dashboard')
        else:
            empobj = emp.objects.get(pk=empid)
            form = addEmpform(instance=empobj)

    return render(request, 'cmsdashboard/dashboardeditEmp.html',{
        'form':form,
    })

@login_required(login_url='/dashboard/dashboardlogin')
def dashboardeditStatus(request, statusid):
    statusobj = emp_status.objects.get(pk=statusid)
    form = changeStatus(request.POST or None, instance=statusobj)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form =  changeStatus
            return redirect('/dashboard')
        else:
            statusobj = emp.objects.get(pk=statusid)
            form = changeStatus(instance=statusobj)

    return render(request, 'cmsdashboard/dashboardeditStatus.html',{
        'form':form,
    })


def record_del():
    currentdate = datetime.datetime.today()
    yesterday = currentdate - timedelta(days = 105)
    
    # print("obj: ", obj)
    # print("Yesterday was: ", yesterday)
    # ydate =str(yesterday.strftime('%m/%d/%Y'))
    # print("Yesterday was: ", ydate)
    # (record_delete.day='yesterday').save()
    object = record_delete.objects.filter(Date=yesterday)
    if not object:
        obj = emp_status.objects.filter(Date__lte=yesterday)
        obj.delete()
        record_delete.objects.create(
            day='yesterday',
            Date=yesterday,
            deactivated=True,
        )

def record_add():
    # currentdate = datetime.datetime.today()
    # NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=105)

    # obj = emp_status.objects.filter(Date__gte=NextDay_Date)

    # object = record_created.objects.filter(Date=NextDay_Date)
    count = 0
    days =  105
    NewDate = datetime.datetime.today() + datetime.timedelta(days=105)
    # print("New date was: ", NewDate)
    while (count == 0):
        NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=days)
        obj = emp_status.objects.filter(Date__gte=NextDay_Date)
        if obj:
            days=days+1
            NewDate=datetime.datetime.today() + datetime.timedelta(days=days)
            count = 1
        else:
            days=days-1

    object = record_created.objects.filter(Date=NewDate)
    objstatus = emp_status.objects.filter(Date__gte=NewDate)

    # print("New date was: ", NewDate)
    # print("NextDay_Date was: ", NextDay_Date)
    # print("days: ", days)
    # print("obj: ", obj)
    # print("object: ", object)
    # print("object: ", objstatus)

    if not objstatus:
        if not object:
            # print("true: ")
            empobj=emp.objects.all()
            statuobj= emp_statustype.objects.get(status='Available')
            statuobjweekend= emp_statustype.objects.get(status='weekend')
            for x in empobj:
                weekdayno = NewDate.weekday()
                if weekdayno < 5: 
                    emp_status.objects.create(
                        emp=x,
                        Date=NewDate,
                        status=statuobj
                        )
                else:
                    emp_status.objects.create(
                        emp=x,
                        Date=NewDate,
                        status=statuobjweekend
                        )

        record_created.objects.create(
            day='NewDate',
            Date=NewDate,
            active=True,
            )





   
















