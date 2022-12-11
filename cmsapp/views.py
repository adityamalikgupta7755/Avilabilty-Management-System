from operator import gt
from django.shortcuts import render
from cmsdashboard.models import emp_status,emp
import datetime
from datetime import timedelta
from django.http import HttpResponse
import csv
from cmsdashboard.views import  record_del, record_add

# Create your views here.
def home(request):
    datelist = []
    if request.method == "POST":
        day = str(request.POST['day'])
        print(day)
        today = datetime.date.today()
        datem = datetime.datetime.strptime(day, "%m/%d/%Y")
        someday = datetime.date(datem.year, datem.month, datem.day)
        Gdate = datetime.date.today()
        Ldate = datetime.date.today()
        if today > someday:
            Gdate = today
            Ldate = someday
        if today < someday:
            Gdate = someday
            Ldate = today
        diff = Gdate - Ldate
        noday = diff.days
        print(noday)

        if noday < 50:
            pasdate = day
        else:
            presentday = datetime.datetime.today() - datetime.timedelta(days=datetime.datetime.today().weekday() % 7)
            pasdate =presentday.strftime('%m/%d/%Y')


       
        # month = int(request.POST['month'])
        # year = int(request.POST['year'])
        # y = 2022
        # m = 9
        # d = 11
        # presentday = datetime.datetime(year, month, day) 
        entered_date = datetime.datetime.strptime(pasdate, '%m/%d/%Y')
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

    obj = emp_status.objects.filter(Date__gte=Sdate,Date__lte=ldate)
    # obj = emp_status.objects.filter(Date__range=[Sdate, enddate])
    emp_obj = emp.objects.all().order_by('id')
    record_del()
    record_add()
    return render(request, 'cmsapp/home.html',
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
    })

def expotcsvfile(request):
    if request.method == "POST":
        date = request.POST['date']
        enddate = request.POST['enddate']
        # print(date)
        Sdate = datetime.datetime.strptime(date, '%Y-%m-%d')
        ldate = datetime.datetime.strptime(enddate, '%Y-%m-%d')
        # print(Sdate)
        # Sdate= datetime.datetime.strptime(entered_date, '%m/%d/%Y')
        # ldate= datetime.datetime.strptime(enddate, '%m/%d/%Y')
        obj = emp_status.objects.filter(Date__gte=Sdate,Date__lte=ldate)
        # print(obj)
        filename =f"{date}-{enddate}Empfile"
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="'f"{date}-{enddate}Empfile"'.csv"' 

        writer = csv.writer(response)

        writer.writerow(['emp','status','Date'])

        for object in obj:
            writer.writerow([object.emp, object.status, object.Date])

        return response 

    return render(request, 'cmsapp/expotcsvfile.html')