from django.urls import path
from . import views

urlpatterns = [
        path('',views.competitors),
        path('<str:name>',views.competitors_detail, name='competitors_detail'),
        
]