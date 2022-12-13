from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topics(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    LWo=Webpage.objects.all()
    d={'LWO':LWo}
    return render(request,'display_webpages.html',d)

def display_AC(request):
    LAO=AccessRecords.objects.all()
    d={'LAO':LAO}
    return render(request,'display_AC.html',d)