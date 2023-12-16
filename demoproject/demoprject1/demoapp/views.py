from django.http import HttpResponse
from django.shortcuts import render
from . models import news,work
# Create your views here.

def demo(request):
    obj=news.objects.all()
    obj1=work.objects.all()
    return render(request,'index.html',{'result':obj,'workd':obj1})

