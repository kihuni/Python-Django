from django.urls import path
from . import views #importing views from views module

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter,name='counter')
]