from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
Внутри данного модуля излагаются правила ОТОБРАЖЕНИЯ информации на страницах
"""
def homePageView(request):
    return HttpResponse("Hello world!")