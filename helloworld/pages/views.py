from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello Chimpers! <br><br> Welcome to your Website')
