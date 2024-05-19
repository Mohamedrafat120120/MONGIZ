from django.contrib import admin
from .models import *
# Register your models here.
class display_education_certificates(admin.ModelAdmin):
    list_display=['User','Degree']
    list_display_links=['User','Degree']
# Register your models here.
admin.site.register(certification,display_education_certificates)