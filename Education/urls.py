from django.urls import path
from . import views

urlpatterns = [
    path('eductional_data', views.FBV_education, name='eductional_data'),

]
