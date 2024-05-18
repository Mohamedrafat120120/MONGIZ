from django.urls import path 
from . import views

urlpatterns=[
    path('health_data/',views.Health_State.as_view(), name='health_data'),
    path('medical_history/',views.medical_history.as_view(), name='medical_history')
]