from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def silk(request):
    return HttpResponse('<marquee><h1>We are not Talking About Dairy Milk Silk</h1></marquee>')



def verma(request):
    return HttpResponse('<h1><marquee>Worth Vermaaa Worth........</h1></marquee>')
