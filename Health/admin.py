from django.contrib import admin

from .models import health_state 
class display_health(admin.ModelAdmin):
    list_display=['Name','national_id','Age']
    list_display_links=['Name','national_id','Age']
admin.site.register(health_state,display_health)

