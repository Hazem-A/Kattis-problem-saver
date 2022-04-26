from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response

def hello(request):
    return render(request, 'main/questions.html', {'name': 'Kattis'})


def home (request):
    return render(request, 'main/home.html')

#creates the form that will be used to
def create(request):
    return (render(request),'main/create.html')