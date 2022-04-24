from django.contrib import admin
from .models import *


@admin.register(Competitor)


class CompetitorsAdmin(admin.ModelAdmin):
    list_display=['name','description','Images']
# Register your models here.

# ,'Keyword','Search','Difficulty'
@admin.register(key)

class keysAdmin(admin.ModelAdmin):
    list_display=['Competename','Keyword','Search','Difficulty']

@admin.register(Compare)

class CompareAdmin(admin.ModelAdmin):
    list_display=['comparename','Parameter','Link_a','Link_b']