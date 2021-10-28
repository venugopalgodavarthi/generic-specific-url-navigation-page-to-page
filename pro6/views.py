from django.shortcuts import render
from django.http import HttpResponse



def welcome(request):
    return render(request,'welcome.html')

def aboutus(request,name):
    return render(request,'aboutus.html',{'name':name})