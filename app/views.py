from django.shortcuts import render

# Create your views here.
from app.models import *
def insert_Topic(request):
    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        QSTO=Topic.objects.all()
        d={'QSTO':QSTO}
        return render(request,'display_Topic.html',d)
    return render(request,'insert_Topic.html')

def insert_webpage(request):
    WTO=Topic.objects.all()
    d={'WTO':WTO}
    if request.method=='POST':
        tn=request.POST['tn']
        nm=request.POST['nm']
        ur=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        WO=webpage.objects.get_or_create(topic_name=TO,name=nm,url=ur)[0]
        WO.save()
        QSWO=webpage.objects.all()
        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'insert_webpage.html',d)

def insert_AccessRecord(request):
    ARO=webpage.objects.all()
    d={'ARO':ARO}
    if request.method=='POST':
        nm=request.POST['nm']
        dt=request.POST['dt']
        ar=request.POST['ar']
        WO=webpage.objects.get(name=nm)
        AO=Access_Records.objects.get_or_create(name=WO,date=dt,author=ar)
        AO.save()
        QSAO=Access_Records.objects.all()
        d1={'QSAO':QSAO}
        return render (request,'display_AccessRecord.html',d1)
    return render(request,'insert_AccessRecord.html',d)


def select_and_display(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        tnlist=request.POST.getlist('tn')
        print(tnlist)

        QSWO=Webpage.objects.none()

        for tn in tnlist:
            QSWO=QSWO|Webpage.objects.filter(topic_name=tn)

        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)   
        
    return render(request,'select_and_display.html',d)



def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    
    return render(request,'checkbox.html',d)