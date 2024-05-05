from . import views
from django.urls import path
urlpatterns = [
    path('report/',views.report.as_view(),name='report'),
]
