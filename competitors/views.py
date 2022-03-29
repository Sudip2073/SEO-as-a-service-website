from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import *

def competitors(request):
    competitors = Competitor.objects.all()
    return render(request,'competitors.html',{'competitors':competitors})