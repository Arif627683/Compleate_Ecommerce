from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Author,Artical,Catagory
# Create your views here.
def index(request):
    post=Artical.objects.all()
    return render(request,'index.html',{'post':post})

def getauthor(request,name):
    return render(request,'profile.html')


