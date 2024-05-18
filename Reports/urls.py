from django.urls import path
from . import views

urlpatterns = [
    path('Reports/', views.Message.as_view(), name='Reports')
]
