from django.contrib import admin
from .models import Home_page
class display_Home(admin.ModelAdmin):
    list_display=['Name','Id_Num']
    list_display_links=['Name','Id_Num']
admin.site.register(Home_page,display_Home)