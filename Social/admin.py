from django.contrib import admin
from account.models import User
from .models import social_state , Family
class display_social_state(admin.ModelAdmin):
    list_display=['User','Phone_Number','Marital_state']
    list_display_links=['User','Phone_Number','Marital_state']
class display_social_family(admin.ModelAdmin):
    list_display=['User','Husband_or_Wife_Name','Sons_Number']
    list_display_links=['User','Husband_or_Wife_Name','Sons_Number']
admin.site.register(social_state,display_social_state)
admin.site.register(Family,display_social_family)

