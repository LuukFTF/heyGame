from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index') # root of the app from index view
]