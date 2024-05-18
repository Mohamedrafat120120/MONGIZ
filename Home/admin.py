from django.contrib import admin
from .models import Home_page
class display_Home(admin.ModelAdmin):
    list_display=['Name']
    list_display_links=['Name']
admin.site.register(Home_page)