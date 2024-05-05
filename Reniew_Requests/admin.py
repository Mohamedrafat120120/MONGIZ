from django.contrib import admin
from .models import *
class Reniew(admin.ModelAdmin):
    list_display=['pk','Sender']
    list_display_links=['pk','Sender']
# Register your models here.
admin.site.register(Personal_Driving_License,Reniew)
admin.site.register(Personal_ID_Card,Reniew)