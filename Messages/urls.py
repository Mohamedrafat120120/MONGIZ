from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.FBV_msg, name='message')
]
