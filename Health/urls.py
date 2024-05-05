from django.urls import path 
from . import views

urlpatterns=[
    path('health_data/', views.FBV_health, name='health_data')
]