from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard),

    path('keyword',views.keyword), 
   
]