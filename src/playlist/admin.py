from django.contrib import admin
from .models import Playlist, PlaylistItem, WatchLater

admin.site.register(Playlist)
admin.site.register(PlaylistItem)
admin.site.register(WatchLater)
