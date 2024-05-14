from django.urls import path
from . import views

urlpatterns = [
    path('Home/<int:national_id>/',views.Home.as_view(),name='Home_page')
]
