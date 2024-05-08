from django.urls import path
from . import views

urlpatterns = [
    path('Reports/', views.FBV_report, name='Reports')
]
