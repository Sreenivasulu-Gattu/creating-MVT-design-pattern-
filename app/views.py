from django.shortcuts import render

from app.models import *
# Create your views here.

def display_topic(request):
    QLTO = Topic.objects.all()
    d = {'QLTO':QLTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QLWO = Webpage.objects.all()
    d = {'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QLAO = AccessRecord.objects.all()
    d = {'QLAO':QLAO}
    return render(request,'display_access.html',d)

def insert_topic(request):
    tn = input('Enter topic name: ')
    NTO = Topic.objects.get_or_create(topic_name = tn)[0]
    NTO.save()
    QLTO = Topic.objects.all()
    d = {'QLTO':QLTO}
    return render(request,'display_topic.html',d)

def insert_webpage(request):
    tn = input('Enter topic name: ')
    n = input('Enter name : ')
    u = input('Enter URL: ')
    e = input('Enter email: ')
    TO = Topic.objects.get(topic_name = tn)
    NWO = Webpage.objects.get_or_create(topic_name = TO,name = n,url = u,email = e)[0]
    NWO.save()
    QLWO = Webpage.objects.all()
    d = {'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def insert_access(request):
    pk = int(input('Enter pk value for webpage: '))
    a = input('Enter author name: ')
    d = input('Enter date in YYYY-MM-DD')
    WO = Webpage.objects.get(pk = pk)
    NAO = AccessRecord.objects.get(name = WO,author = a,date = d)

    QLAO = AccessRecord.objects.all()
    d = {'QLAO':QLAO}
    return render(request,'display_access.html',d)