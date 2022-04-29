from django.shortcuts import render
from django.http import HttpResponse
from .forms import Createlist
from .models import lists,question
# Create your views here.
# request -> response

def hello(request):
    return render(request, 'main/questions.html', {'name': 'Kattis'})


def home (request):
    return render(request, 'main/home.html',{})

#creates the form that will be used to
def create(request):
    if request.method=="POST":
        form = Createlist(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            t = lists(name=name)
            t.save()

    else:
        questionare = Createlist()
    return render(request,'main/create.html',{"form":questionare})

def list(request,ls):
    category = lists.objects.get(name=ls)
    return render(request,"main/list.html",{"ls":category})

#add items to the list
def add(request,name):
    if request.method == "POST":
        txt = request.POST.get("save")


