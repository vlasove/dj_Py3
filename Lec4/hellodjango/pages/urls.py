"""
Здесь описываем пары URL/ViewFunction
"""
from django.urls import path 
from .views import homePageView # импортируем функцию которую сделали на шаге 1

urlpatterns = [
    path('', homePageView, name='home')
]