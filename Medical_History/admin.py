from django.contrib import admin
from .models import *
# Register your models here.
class display_medical_history(admin.ModelAdmin):
    list_display=['Name','national_id','User','Age']
    list_display_links=['Name','national_id','User','Age']
admin.site.register(medical_history,display_medical_history)