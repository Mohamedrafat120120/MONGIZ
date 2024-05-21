from django.contrib import admin

from Work.models import work_career

class display_word(admin.ModelAdmin):
    list_display=['Sender','__str__','Current_Jop']
    list_display_links=['Sender','__str__','Current_Jop']

admin.site.register(work_career,display_word)
