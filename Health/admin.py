from django.contrib import admin

from .models import health_state , medical_history
admin.site.register(health_state)
admin.site.register(medical_history)
