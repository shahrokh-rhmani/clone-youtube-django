from django.urls import path
from . import views


urlpatterns = [
    path('', views.listview, name='listview'),
]