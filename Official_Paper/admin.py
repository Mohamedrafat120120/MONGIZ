from django.contrib import admin
from Official_Paper.models import *
# Register your models here.
class display_papers(admin.ModelAdmin):
    list_display=['User','national_id']
    list_display_links=['User','national_id']

admin.site.register(paper,display_papers)