from django.shortcuts import render
from django.http import HttpResponse
from first_project.models import *

# Create your views here.

def index(request):
    web_list = AccessRecord.objects.order_by('date')
    date_dict = {'webpage': web_list}
    # my_dict = {'insert_here': 'Hello view'}
    return render(request, "index.html", context=date_dict)


def sums(request):
    return HttpResponse(55)
