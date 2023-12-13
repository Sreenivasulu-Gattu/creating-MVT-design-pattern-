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

