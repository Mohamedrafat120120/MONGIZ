from . import views
from django.urls import path
urlpatterns = [
    path('masseges/',views.Masseges.as_view(),name='massages'),
]
