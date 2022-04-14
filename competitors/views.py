from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import *
from .models import Competitor

def competitors(request):
    competitors = Competitor.objects.all()
    return render(request,'competitors.html',{'competitors':competitors})

def competitors_detail(request, name):
    try:
        Mod = Competitor.objects.get(name=str(name))
    except Competitor.DoesNotExist:
        raise Http404('Competitor not found')
    return render(request, 'content.html',{
        'Mod': Mod,
    })

    