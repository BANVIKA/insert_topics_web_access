from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()
        QSWO=Webpage.objects.all()
        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)   
    return render(request,'insert_webpage.html',d)




def insert_AccessRecord(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        pk=request.POST['pk']
        na=request.POST['na']
        ur=request.POST['ur']
        d=request.POST['d']
        au=request.POST['au']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=na)
        AC=AccessRecord.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        AC.save()
        QSAC=AccessRecord.objects.all()
        d1={'QSAC':QSAC}
        return render(request,'display_AccessRecord.html',d1)   
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
