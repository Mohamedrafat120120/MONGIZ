from django.contrib import admin

from .models import health_state , medical_history
class display_health(admin.ModelAdmin):
    list_display=['Name']
    list_display_links=['Name']
admin.site.register(health_state,display_health)
admin.site.register(medical_history)
