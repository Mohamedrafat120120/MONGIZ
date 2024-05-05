from django.urls import path
from . import views

urlpatterns = [
    path('social_state/', views.FBV_social, name='social_state'),

]
