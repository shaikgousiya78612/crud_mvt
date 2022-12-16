from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topics(request):
    LTO=Topic.objects.all()
    LTO=Topic.objects.filter(topic_name='kabaddi').order_by('topic_name')
    LTO=Topic.objects.exclude(topic_name='kabaddi')
    LTO=Topic.objects.all().order_by('topic_name')
    LTO=Topic.objects.all().order_by('-topic_name')
    LTO=Topic.objects.order_by(Length('topic_name'))
    LTO=Topic.objects.order_by(Length('topic_name').desc())
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    LWo=Webpage.objects.all()
    #FIELD LOOKUPS
    LWo=Webpage.objects.filter(name__startswith='l')
    LWo=Webpage.objects.filter(name__endswith='u')
    LWo=Webpage.objects.filter(name__in='laddu')
    LWo=Webpage.objects.filter(name__contains='a')
    LWo=Webpage.objects.filter(name__regex='^s')
    d={'LWO':LWo}
    return render(request,'display_webpages.html',d)

def display_AC(request):
    LAO=AccessRecords.objects.all()
    LAO=AccessRecords.objects.filter(date='2022-12-13')
    LAO=AccessRecords.objects.exclude(date='2022-12-13')
    LAO=AccessRecords.objects.order_by('name')
    LAO=AccessRecords.objects.order_by('-name')
    LAO=AccessRecords.objects.order_by(Length('name'))
    LAO=AccessRecords.objects.order_by(Length('name').desc())
    LAO=AccessRecords.objects.all()[2:3:]
    LAO=AccessRecords.objects.all()[1:4:]
    LAO=AccessRecords.objects.all()
    #FIELD LOOKUPS 
    LAO=AccessRecords.objects.filter(date__gt='2022-12-9')
    LAO=AccessRecords.objects.filter(date__gte='2022-12-9')
    LAO=AccessRecords.objects.filter(date__lt='2022-12-13')
    LAO=AccessRecords.objects.filter(date__lte='2022-12-13')
    LAO=AccessRecords.objects.filter(date__month='12')
    LAO=AccessRecords.objects.filter(date__year='2019')
    LAO=AccessRecords.objects.filter(date__day='2')
    d={'LAO':LAO}
    return render(request,'display_AC.html',d)