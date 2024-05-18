from django.contrib import admin

from .models import social_state , Family
class display_social(admin.ModelAdmin):
    list_display=['Name']
    list_display_links=['Name']
admin.site.register(social_state,display_social)
admin.site.register(Family,display_social)

