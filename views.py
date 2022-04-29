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
        questionare = Createlist(request.POST)
        if questionare.is_valid():
            name = questionare.cleaned_data["name"]
            t = lists.objects.create(name=name)
            t.save()
            return render(request, 'main/create.html', {"form": questionare})
    else:
        questionare = Createlist()
    return render(request,'main/create.html',{"form":questionare})

def list(request,ls):
    category = lists.objects.get(name=ls)
    if request.method=="POST":
        txt = request.POST.get("add")

        category.question_set.create(Kattis_id=txt,link="https://open.kattis.com/problems/"+txt)

    return render(request,"main/list.html",{"ls":category})



