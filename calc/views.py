from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    #return HttpResponse('Hello world')
    return render(request, 'home.html',{'name' : 'cdac'}) # after creating template, in dictionary sending dynamic name data


def add(request):
    val1 = int(request.POST['num1'])   # use GET ot POST
    val2 = int(request.POST['num2'])
    res = val1 + val2

    return render(request, "result.html",{'result':res})