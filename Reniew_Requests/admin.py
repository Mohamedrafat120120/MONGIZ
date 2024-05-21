from django.contrib import admin
from .models import *
# class display_reniew_id(admin.ModelAdmin):
#     list_display=["Full_Name"]
    # list_display_links=["Full_Name"]
# class display_reniew_driving(admin.ModelAdmin):
#     list_display=['national_id']
#     list_display_links=['national_id']
# Register your models here.
admin.site.register(Personal_Driving_License)
admin.site.register(Personal_ID_Card)