from django.urls import path
from . import views

urlpatterns = [
    path('Home/', views.FBV_home, name='Home_page')
]
