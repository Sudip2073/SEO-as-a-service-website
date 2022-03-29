from django.contrib import admin
from .models import *


@admin.register(Competitor)

class CompetitorsAdmin(admin.ModelAdmin):
    list_display=['name','description','Images','backlink','DA','SERP']
# Register your models here.
