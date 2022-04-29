from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('hello/',views.hello),
    path('create/',views.create),
    path('list/<ls>',views.list)
]
