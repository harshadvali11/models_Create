from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    tn=input('enter topic name')
    TOD=Topic.objects.get_or_create(topic_name=tn)
    if TOD[1]:
        LTO=Topic.objects.all()
        d={'LTO':LTO}
        return render(request,'display_topics.html',d)

        
    else:
        return HttpResponse('Given Topic is Already Present')


def display_topics(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)




def insert_webpage(request):
    tn=input('enter topicname')
    n=input('enter name')
    url=input('enter url')
    email=input('enter email')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        WTOD=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url,email=email)
        if WTOD[1]:
            LWO=Webpage.objects.all()
            d={'LWO':LWO}
            return render(request,'display_webpages.html',d)

            #return HttpResponse('New Webpage is Created')
        else:
            return HttpResponse('With Given Details Webapge is Already Present')
    else:
        return HttpResponse('Given Parent Topic Table Data is Not present in DB')

def insert_access(request):
    
    pk=int(input('enter pk of webpage'))
    author=input('enter author')
    date=input('enter date')

    LWO=Webpage.objects.filter(pk=pk)
    if LWO:
        WO=LWO[0]
        ATOD=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)

        if ATOD[1]:
            return HttpResponse('New Access is Created')
        else:
            return HttpResponse('With Given Details Access is Already Present')
    else:
        return HttpResponse('Given Parent Webpage Table Data is Not present in DB')

def display_topics(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)







