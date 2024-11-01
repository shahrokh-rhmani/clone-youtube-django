from django.urls import path
from . import views


urlpatterns = [
    path('playlists/', views.playlist_list, name='playlist_list'),
    path('playlists/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
    path('playlists/create/', views.create_playlist, name='create_playlist'),
    path('video/<int:video_id>/add-to-playlist/', views.add_to_playlist, name='add_to_playlist'),
    path('watch-later/', views.watch_later_list, name='watch_later_list'),
    path('watch-later/add/<int:video_id>/', views.add_to_watch_later, name='add_to_watch_later'),
]