from django.contrib import admin
from Messages.models import *
# Register your models here.
class display_message(admin.ModelAdmin):
    list_display=['Header']
    list_display_links=['Header']
admin.site.register(message,display_message)