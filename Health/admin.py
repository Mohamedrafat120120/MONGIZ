from django.contrib import admin

from .models import health_state 
class display_health(admin.ModelAdmin):
    list_display=['Name','Age','User']
    list_display_links=['Name','Age','User']
admin.site.register(health_state,display_health)

