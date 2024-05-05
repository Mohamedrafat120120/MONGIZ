from django.urls import path
from . import views

urlpatterns = [
    path('Official_Paper/', views.FBV_paper, name='Official_Paper')
]
