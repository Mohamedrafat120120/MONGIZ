from django.urls import path
from . import views

urlpatterns = [
    path('Work/', views.FBV_work, name='Work_career')
]
