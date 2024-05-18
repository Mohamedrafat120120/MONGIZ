from django.urls import path
from . import views

urlpatterns = [
    path('social_state/', views.Social.as_view(), name='social_state'),

]
