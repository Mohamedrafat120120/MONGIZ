from django.contrib import admin
from .models import educational_state
class display_education(admin.ModelAdmin):
    list_display=['Name','User','Schools']
    list_display_links=['Name','User','Schools']
admin.site.register(educational_state,display_education)


