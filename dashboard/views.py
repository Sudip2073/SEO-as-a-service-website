from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import *

# @login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')

def keyword(request):
    return render(request,'key.html')





