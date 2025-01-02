from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import *
from django.db.models.functions import Length

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
    LWO=Webpage.objects.filter(topic_name='Cricket')
    LWO=Webpage.objects.exclude(topic_name='Cricket')
    LWO=Webpage.objects.all()[0:3:1]
    LWO=Webpage.objects.all()[2:5:1]
    LWO=Webpage.objects.all()[::-1]
    LWO=Webpage.objects.all().order_by('name')
    
    LWO=Webpage.objects.all().order_by('-name')
    
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(name__startswith='h')
    LWO=Webpage.objects.filter(name__endswith='d')
    
    LWO=Webpage.objects.filter(name__contains='a')
    
    LWO=Webpage.objects.filter(name__regex='^h\w+')
    
    LWO=Webpage.objects.filter(id__range=(1,4))

    LWO=Webpage.objects.filter(id__in=(1,4))
    
    


    
    
    
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)


def display_access(request):
    LAO=AccessRecord.objects.all()
    LAO=AccessRecord.objects.filter(date='2025-01-02')
    LAO=AccessRecord.objects.filter(date__year='2025')
    LAO=AccessRecord.objects.filter(date__month='11')
    LAO=AccessRecord.objects.filter(date__day='7')
    LAO=AccessRecord.objects.filter(date__lt='2025-01-02')
    LAO=AccessRecord.objects.filter(date__lte='2025-01-02')
    LAO=AccessRecord.objects.filter(date__gt='2025-01-02')
    LAO=AccessRecord.objects.filter(date__year__gte='2024')
    
    
    

    
    
    d={'LAO':LAO}
    return render(request,'display_access.html',d)





