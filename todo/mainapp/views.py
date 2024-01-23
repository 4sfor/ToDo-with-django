from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.

def index(request):
    taskList=Task.objects.all()
    return render(request,'mainapp/index.html',{'taskList': taskList})

