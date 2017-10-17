from django.http import HttpResponse
from django.shortcuts import render

from first_project import forms
from first_project.models import *
from first_project.forms import NewUser


# Create your views here.

def index(request):
    web_list = AccessRecord.objects.order_by('date')
    date_dict = {'webpage': web_list}
    # my_dict = {'insert_here': 'Hello view'}
    return render(request, "index.html", context=date_dict)


def sums(request):
    return HttpResponse(55)


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation OK!")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    return render(request, 'form_page.html', {'form': form})


def user(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error")
    return render(request,'users.html',context={'form':form})
    # user_list = User.objects.order_by('first_name')
    # user_dect = {'user': user_list}
    # return render(request, 'users.html', context=user_dect)
