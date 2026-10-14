from django.urls import path
from w3school import views
urlpatterns = [
    path('', views.index),
]