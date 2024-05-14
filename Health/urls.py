from django.urls import path 
from . import views

urlpatterns=[
    path('health_data/<int:national_id>/',views.Health_State.as_view(), name='health_data')
]