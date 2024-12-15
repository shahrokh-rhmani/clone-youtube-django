from django.urls import path
from . import views


urlpatterns = [
    path('', views.listview, name='listview'),
    path('<ch_name>/video/<int:video_id>/', views.detailview, name='detailview'),
    path('search/', views.search, name='search'),
]