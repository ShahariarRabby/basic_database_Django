from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_here': 'Hello view'}
    return render(request, "index.html", context=my_dict)

def sums(request):
    return HttpResponse(55)