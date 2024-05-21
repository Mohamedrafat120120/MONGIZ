from django.contrib import admin
from Messages.models import *
# Register your models here.
class display_message(admin.ModelAdmin):
    list_display=['Header','User']
    list_display_links=['Header','User']
admin.site.register(message,display_message)