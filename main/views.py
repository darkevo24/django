from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse

from main.models import User
# Create your views here.
from .forms import UserForm

def register(request):
    form = UserForm()
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     email = User.objects.raw("SELECT email FROM main_user").query
    #     for i in email :
    #         print(form.data.)
        # if form.is_valid():
        #     form.save()

    return render(request,"register.html",{'form' : form})

def login(request):
    return render(request,"login.html")

def index(request):
    return render(request,"index.html")

def xero(request):
    return render(request,"xero.html")

def cin7(request):
    return render(request,"cin7.html")