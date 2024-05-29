from django.urls import path
from . import views

urlpatterns = [
    path('Work/', views.work.as_view(), name='Work_career'),
    path('get_work/', views.get_work.as_view(), name='get_Work_career')
]
